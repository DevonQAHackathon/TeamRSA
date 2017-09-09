"""Driver for http/https based web-servers"""

import requests
from requests.packages import urllib3

from drivers.http.exception import HttpDriverException


class HttpDriver(object):
    """An HttpConnection implementation using the popular requests module.

    Making as generic as possible for connecting to al possible http servers using different
    architectures (SOAP, REST..). Instead of using the get, post methods from request module
    itself we are using the Session object to persist the authentication and session data.
    """

    def __init__(self, host, protocol='http', port=None, auth=None, ssl_verify=False
                 , http_adapter=None):
        """Initialize the connection to an http server

        Args:
            protocol: Protocol to use http/https (str)
            host: a host address/name of the server to connect (str)
            auth: An authentication tuple (username, password) if required  or a defined
                  type of authentication (tuple)
            ssl_verify: If the server is on SSL verify certificate or not (bool)
            http_adapter: An adapter for http connection.
        """

        urllib3.disable_warnings()
        self.__protocol = protocol
        self.__host = host
        self.__port = port
        if port:
            self.__base_url = '%s://%s:%s' % (self.__protocol, self.__host, self.__port)
        else:
            self.__base_url = '%s://%s' % (self.__protocol, self.__host)
        self.__ssl_verify = ssl_verify
        self.__session = requests.session()
        if auth:
            self.__session.auth = auth
        if http_adapter:
            self.__session.mount('{%s}://'.format(protocol), http_adapter)
        self.__session.verify = self.__ssl_verify
        self.__connected = False
        # A default parameter list maintaining for the the request if server always need it,
        # For example in some POST calls, if the server always expects 'ctoken' as a parameter we
        #  can get it and save to default_params, so whenever we make a connection these
        # parameters will be automatically send
        self.__default_params = {}
        # When we create the connection object itself will make sure we can connect to the server
        #  this ensure that we wont go further when the server is not available
        self.__connect__()

    @property
    def protocol(self):
        return self.__protocol

    @property
    def host(self):
        return self.__host

    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, base_url):
        self.__base_url = base_url

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def session(self):
        return self.__session

    @property
    def connected(self):
        return self.__connected

    @property
    def default_params(self):
        return self.__default_params

    def __connect__(self):
        """Start an HTTP Session to the host, to make sure we can connect to it"""

        try:
            self.Get('')
            self.__connected = True
        except Exception as e:
            raise HttpDriverException('ConnectionError', self.base_url, str(e))

    def SetDefaultParams(self, params):
        """Set the default params if any

        Args:
            params: Default Parameters to set (dict)
        """

        if params is not None:
            for key, value in params.items():
                self.__default_params[key] = value

    def __merge_default_params__(self, params):
        """Merge the given parameters to DefaultParams (private use for HTTP methods

        Args:
            params: Parameters to merge with default params (dict)
        """

        if params is not None:
            for key, value in self.__default_params.items():
                if key not in params:
                    params[key] = value
            return params
        else:
            return self.__default_params

    @staticmethod
    def GetRawResponse(response):
        resp_code = response.status_code
        if resp_code == 200:
            return response.content

        else:
            raise HttpDriverException('UnknownResponseError', response.url, 'ERROR RESPONSE: %s'
                                      % resp_code)

    @staticmethod
    def GetJsonResponse(response):
        """A method for accepting response from GET/POST/PUT requests and verifying the response
           code and result returned.
        Args:
            response: json response from requests (obj)
        Returns:
            validated json response (json)
        Raises:
            UnknownResponseError if response doesnt have any JSON (HttpDriverException)
        """

        resp_code = response.status_code
        if resp_code == 200:
            return response.json()

        else:
            raise HttpDriverException('UnknownResponseError', response.url, 'ERROR RESPONSE: %s'
                                      % resp_code)

    def Get(self, url, params=None, headers=None, timeout=300):
        """A wrapper method for sending HTTP GET Requests to the Server

        Args:
            url: A Resource Reference Path to send the request (str)
            params: parameters for the request (dict)
            headers: header information for http requests
        Returns:
            response (object)
        Raises:
            GetRequestError if response doesnt have any JSON (HttpDriverException)
        """

        request_url = self.base_url + url
        params = self.__merge_default_params__(params)
        try:
            response = self.session.get(request_url, params=params, headers=headers,
                                        timeout=timeout)
            return response
        except Exception as e:
            raise HttpDriverException('GetRequestError', request_url, str(e))

    def Post(self, url, params=None, data=None, payload=None, files=None, headers=None,
             timeout=300):
        """A wrapper method for sending HTTP POST Requests to the Server

        Args:
            url: A Resource Reference Path to send the request (str)
            params: parameters for the request (dict)
            data: payload for the POST request that will be sent either in form-urlencoded encoding
                if it is a dict, or without any encoding if it is a str. This is to align with the
                'data' parameter in the underlying session.post() call. (dict or str)
            payload: payload for the POST request, Request will be loading the payload as JSON while
                     sending the call so the format should be in JSON decodable (dict)
            files: If any file data to be send (obj)
            headers: HTTP Post headers (str)

        Returns:
            response (object)

        Raises:
            PostRequestError if response doesnt have any JSON (HttpDriverException)
        """

        request_url = self.base_url + url
        params = self.__merge_default_params__(params)
        try:
            response = self.session.post(request_url, params=params, data=data, json=payload
                                         , files=files, headers=headers, timeout=timeout)
            return response
        except Exception as e:
            raise HttpDriverException('PostRequestError', request_url, str(e))

    def Delete(self, url, params=None, payload=None, timeout=300):
        """A wrapper method for sending HTTP DELETE Requests to the Server

        Args:
            url: A Resource Reference Path to send the request
            params: parameters for the request
            payload: payload for the DELETE request, Request will be loading the payload as
            JSON while sending the call so the format should be in JSON decodable (dict)
        Returns:
            response (object)
        Raises:
            DeleteRequestError if response doesnt have any JSON (HttpDriverException)
        """

        request_url = self.base_url + url
        params = self.__merge_default_params__(params)
        try:
            response = self.session.delete(request_url, params=params, json=payload,
                                           timeout=timeout)
            return response
        except Exception as e:
            raise HttpDriverException('DeleteRequestError', request_url, str(e))

    def Put(self, url, params=None, payload=None, timeout=300):
        """A wrapper method for sending HTTP PUT Requests to the Server

        Args:
            url: A Resource Reference Path to send the request
            params: parameters for the request (Dict)
            payload: payload for the PUT request, Request will be loading the payload as JSON
               while sending the call so the format should be in JSON decodable (Dict)
        Returns:
            response (object)
        Raises:
            PutRequestError if response doesnt have any JSON (HttpDriverException)
        """

        request_url = self.base_url + url
        params = self.__merge_default_params__(params)
        try:
            response = self.session.put(request_url, params=params, json=payload, timeout=timeout)
            return response
        except Exception as e:
            raise HttpDriverException('PutRequestError', request_url, str(e))
