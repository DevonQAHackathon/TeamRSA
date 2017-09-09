from drivers.http.httpdriver import HttpDriver
from utils.get_random_city import RandomCityChooser
from testconfig import config
from nose.plugins.attrib import attr
import json
class TestCitiesTemperature:


    def host(self):
        return self.__host
    def appId(self):
        return self.__appId
    def cityId(self):
        return self.__cityId

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
        cityInfo = RandomCityChooser.getRandomCity()
        params = {"id": cityInfo['id'], "appid": self.__appId}
        print("Running 5 day forecast test for city id = %s" %cityInfo['id'])
        response = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        print(response)

    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_forecast5_city_name(self):
        cityInfo = RandomCityChooser.getRandomCity()
        params = {"q": cityInfo['name'], "appid": self.__appId}
        print("Running 5 day forecast test for city = %s" %cityInfo['name'])
        response = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        print(response)

    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_call_latlong(self):
        cityInfo = RandomCityChooser.getRandomCity()
        citylong = cityInfo['coord']['lon']
        cityLat = cityInfo['coord']['lat']
        params = {"lat": cityLat, "lon": citylong, "appid": self.__appId}
        print("Running 5 day forecast test for Lattitude = %s and Longitude = %s" %(cityLat,citylong))
        response = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        print(response)

    @attr(Priority='P0', Component='Forecast', Suite='Smoke')
    def test_api_call_zipcode(self):
        zipCode = RandomCityChooser.getRandomZip()['Zipcode']
        params = {"zip": zipCode, "appid": self.__appId}
        print("Running 5 day forecast test for ZipCode = %s" %(zipCode))
        response = self.invokeGetApi(url="/data/2.5/forecast", params=params)
        print(response)
