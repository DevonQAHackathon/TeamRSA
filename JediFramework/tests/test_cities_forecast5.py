from drivers.http.httpdriver import HttpDriver
from testutils.get_random_city import RandomCityChooser
from testconfig import config
from nose.plugins.attrib import attr
class TestCitiesTemperature:


    def host(self):
        return self.__host
    def appId(self):
        return self.__appId


    @classmethod
    def setupClass(cls):
        cls.__host = (config['open-weather']['url'])
        cls.__appId = (config['open-weather']['appId'])
        cls.__httpClient = HttpDriver(host=cls.__host, protocol="http")

    def invokeGetApi(self, url, params):
        httpResponse = self.__httpClient.Get(url=url, params=params)
        jsonResponse = self.__httpClient.GetJsonResponse(httpResponse)
        return jsonResponse

    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_forecast5_city_id(self):
        cityInfo1 = RandomCityChooser.getRandomCity()
        cityInfo2 = RandomCityChooser.getRandomCity()
        params = {"id": cityInfo1['id'], "appid": self.__appId}
        print("Running 5 day forecast test for city id = %s" %cityInfo1['id'])
        response1 = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        params = {"id": cityInfo1['id'], "appid": self.__appId}
        print("Running 5 day forecast test for city id = %s" %cityInfo2['id'])
        response2 = self.invokeGetApi(url="/data/2.5/forecast", params=params)


    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_forecast5_city_name(self):
        cityInfo1 = RandomCityChooser.getRandomCity()
        cityInfo2 = RandomCityChooser.getRandomCity()
        params = {"q": cityInfo1['name'], "appid": self.__appId}
        print("Running 5 day forecast test for city = %s" %cityInfo1['name'])
        response1 = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        params = {"q": cityInfo2['name'], "appid": self.__appId}
        print("Running 5 day forecast test for city = %s" %cityInfo2['name'])
        response2 = self.invokeGetApi(url="/data/2.5/forecast", params=params)

    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_call_latlong(self):
        cityInfo1 = RandomCityChooser.getRandomCity()
        cityInfo2 = RandomCityChooser.getRandomCity()
        citylong1 = cityInfo1['coord']['lon']
        cityLat1 = cityInfo1['coord']['lat']
        citylong2 = cityInfo2['coord']['lon']
        cityLat2 = cityInfo2['coord']['lat']
        params = {"lat": cityLat1, "lon": citylong1, "appid": self.__appId}
        print("Running 5 day forecast test for Lattitude = %s and Longitude = %s" %(cityLat1,citylong1))
        response1 = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        params = {"lat": cityLat2, "lon": citylong1, "appid": self.__appId}
        print("Running 5 day forecast test for Lattitude = %s and Longitude = %s" %(cityLat2,citylong2))
        response2 = self.invokeGetApi(url="/data/2.5/forecast", params=params)


    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_call_zipcode(self):
        zipCode1 = RandomCityChooser.getRandomZip()['Zipcode']
        zipCode2 = RandomCityChooser.getRandomZip()['Zipcode']
        params = {"zip": zipCode1, "appid": self.__appId}
        print("Running 5 day forecast test for ZipCode = %s" %(zipCode1))
        response1 = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        params = {"zip": zipCode2, "appid": self.__appId}
        print("Running 5 day forecast test for ZipCode = %s" %(zipCode2))
        response2 = self.invokeGetApi(url="/data/2.5/forecast", params=params)
