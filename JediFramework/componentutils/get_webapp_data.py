import time
from selenium import webdriver

class ReadTemperatureData:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def getCityData(self, fromCity, toCity):
        driver = self.driver
        driver.get("http://192.168.1.225:82/index.php")
        fromElem = driver.find_element_by_id('From')
        toElem = driver.find_element_by_id('To')
        submitElem = driver.find_element_by_id('Submit')
        fromElem.send_keys(fromCity)
        toElem.send_keys(toCity)
        submitElem.click()
        time.sleep(4)
        jsonData = {}
        cityData=[]
        for i in range(2,4):
            jsonData['city'] = driver.find_element_by_xpath("//*[@id='city_table']/tbody/tr["+str(i)+"]/td["+str(1)+"]").text
            jsonData['temp'] = driver.find_element_by_xpath("//*[@id='city_table']/tbody/tr["+str(i)+"]/td["+str(2)+"]").text
            jsonData['humidity'] = driver.find_element_by_xpath("//*[@id='city_table']/tbody/tr["+str(i)+"]/td["+str(3)+"]").text
            jsonData['min_temp'] = driver.find_element_by_xpath("//*[@id='city_table']/tbody/tr["+str(i)+"]/td["+str(4)+"]").text
            jsonData['max_temp'] = driver.find_element_by_xpath("//*[@id='city_table']/tbody/tr["+str(i)+"]/td["+str(5)+"]").text
            cityData.append(jsonData)
        driver.quit()
        return(cityData)

    def tearDown(self):
        self.driver.close()
#rd = ReadTemperatureData()
#print(rd.getCityData(fromCity="Frankfurt", toCity="Reston"))