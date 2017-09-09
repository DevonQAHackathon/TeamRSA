class HttpDriverException(Exception):
    """Raise this exception when connecting with an HTTP Server"""

    def __init__(self, etype, url, message):
        super().__init__('{}: ServerURL: {}\n ERROR: {}'.format(etype, url, message))


class HttpAuthenticationException(Exception):
    """Raise this exception when authentication to http server fails with response code 401"""
    pass


class HttpServerNotFoundException(Exception):
    """Raise this exception when http server not found with response code 404"""
    pass
