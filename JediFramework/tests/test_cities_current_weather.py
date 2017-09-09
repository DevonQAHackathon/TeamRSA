from drivers.http.httpdriver import HttpDriver
from testconfig import config
from nose.plugins.attrib import attr
from testutils.get_random_city import RandomCityChooser
from componentutils.get_webapp_data import ReadTemperatureData

class TestCitiesTemperature:


    def host(self):
        return self.__host
    def appId(self):
        return self.__appId
    def httpClient(self):
        return self.__httpClient

    @classmethod
    def setupClass(cls):
        cls.__host = (config['open-weather']['url'])
        cls.__appId = (config['open-weather']['appId'])
        cls.__httpClient = HttpDriver(host=cls.__host, protocol="http")


    def invokeGetApi(self, url, params):
        httpResponse = self.__httpClient.Get(url=url, params=params)
        jsonResponse = self.__httpClient.GetJsonResponse(httpResponse)
        return jsonResponse

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_city_country(self):
        cityInfo1 = RandomCityChooser.getRandomCity()
        cityCountry1 = cityInfo1['name'] + "," + cityInfo1['country']
        cityInfo2 = RandomCityChooser.getRandomCity()
        cityCountry2 = cityInfo2['name'] + "," + cityInfo2['country']
        params = {"q": cityCountry1, "appid": self.__appId}
        print("Running test for city and country = %s" %cityCountry1)
        response1 = self.invokeGetApi(url='/data/2.5/weather', params=params)
        params = {"q": cityCountry2, "appid": self.__appId}
        print("Running test for city and country = %s" %cityCountry2)
        response2 = self.invokeGetApi(url='/data/2.5/weather', params=params)

    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_city(self):
        cityName1 = RandomCityChooser.getRandomCity()['name']
        cityName2 = RandomCityChooser.getRandomCity()['name']
        params = {"q": cityName1, "appid": self.__appId}
        print("Running test for city = %s" %cityName1)
        response1 = self.invokeGetApi("/data/2.5/weather", params=params)
        params = {"q": cityName2, "appid": self.__appId}
        print("Running test for city = %s" %cityName2)
        response2 = self.invokeGetApi("/data/2.5/weather", params=params)


    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_latlong(self):
        cityInfo1 = RandomCityChooser.getRandomCity()
        citylong1 = cityInfo1['coord']['lon']
        cityLat1 = cityInfo1['coord']['lat']
        cityInfo2 = RandomCityChooser.getRandomCity()
        uiD = ReadTemperatureData()
        uiData = uiD.getCityData(cityInfo1['name'],cityInfo2['name'])
        citylong2 = cityInfo2['coord']['lon']
        cityLat2 = cityInfo2['coord']['lat']
        params = {"lat": cityLat1, "lon": citylong1, "appid": self.__appId}
        print("Running test for Lattitude = %s and Longitude = %s" %(cityLat1,citylong1))
        response1 = self.invokeGetApi("/data/2.5/weather", params=params)
        params = {"lat": cityLat2, "lon": citylong2, "appid": self.__appId}
        print("Running test for Lattitude = %s and Longitude = %s" %(cityLat1,citylong1))
        response2 = self.invokeGetApi("/data/2.5/weather", params=params)
        assert str(uiData[0]['city']) == str(response1['name']).upper()
        assert str(uiData[1]['city']) == str(response2['name']).upper()


    @attr(Priority='P0', Component='Cities', Suite='Smoke')
    def test_api_call_zipcode(self):
        city1 = RandomCityChooser.getRandomZip()
        city2 = RandomCityChooser.getRandomZip()
        city1Name = city1['City']
        city2Name = city2['City']
        uiD = ReadTemperatureData()
        uiData = uiD.getCityData(city1Name,city2Name)
        zipCode1 = city1["Zipcode"]
        zipCode2 = city2["Zipcode"]
        params = {"zip": zipCode1, "appid": self.__appId}
        print("Running test for ZipCode = %s" %(zipCode1))
        response1 = self.invokeGetApi("/data/2.5/weather", params=params)
        params = {"zip": zipCode2, "appid": self.__appId}
        print("Running test for ZipCode = %s" %(zipCode2))
        response2 = self.invokeGetApi("/data/2.5/weather", params=params)
        assert str(uiData[0]['city']) == str(response1['name']).upper()
        assert str(uiData[1]['city']) == str(response2['name']).upper()




