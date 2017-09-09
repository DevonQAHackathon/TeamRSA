from drivers.http.httpdriver import HttpDriver
from testconfig import config
from nose.plugins.attrib import attr
from utils.get_random_city import RandomCityChooser
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

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_city_country(self):
        cityInfo = RandomCityChooser.getRandomCity()
        cityCountry = cityInfo['name'] + "," + cityInfo['country']
        params = {"q": cityCountry, "appid": self.__appId}
        print("Running test for city and country = %s" %cityCountry)
        httpResponse = self.__httpClient.Get("/data/2.5/weather", params=params)
        jsonData = self.__httpClient.GetJsonResponse(httpResponse)
        print(jsonData)

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_city(self):
        cityInfo = RandomCityChooser.getRandomCity()
        cityName = cityInfo['name']
        params = {"q": cityName, "appid": self.__appId}
        print("Running test for city = %s" %cityName)
        httpResponse = self.__httpClient.Get("/data/2.5/weather", params=params)
        jsonData = self.__httpClient.GetJsonResponse(httpResponse)
        print(jsonData)

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_latlong(self):
        cityInfo = RandomCityChooser.getRandomCity()
        citylong = cityInfo['coord']['lon']
        cityLat = cityInfo['coord']['lat']
        params = {"lat": cityLat, "lon": citylong, "appid": self.__appId}
        print("Running test for Lattitude = %s and Longitude = %s" %(cityLat,citylong))
        httpResponse = self.__httpClient.Get("/data/2.5/weather", params=params)
        jsonData = self.__httpClient.GetJsonResponse(httpResponse)
        print(jsonData)

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_zipcode(self):
        zipCode = RandomCityChooser.getRandomZip()['Zipcode']
        params = {"zip": zipCode, "appid": self.__appId}
        print("Running test for ZipCode = %s" %(zipCode))
        httpResponse = self.__httpClient.Get("/data/2.5/weather", params=params)
        jsonData = self.__httpClient.GetJsonResponse(httpResponse)
        print(jsonData)

