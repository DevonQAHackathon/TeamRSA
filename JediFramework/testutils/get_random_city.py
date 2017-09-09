import random
from testconfig import config

class RandomCityChooser(object):
    # gives a city from the city lost randomly
    @staticmethod
    def getRandomCity():
        cities = config['city_list']
        choosedIndex = random.randint(0,len(cities)-1)
        return cities[choosedIndex]

    @staticmethod
    def getRandomZip():
        zip = config['zipcodes']
        choosedIndex = random.randint(0, len(zip)-1)
        return zip[choosedIndex]
