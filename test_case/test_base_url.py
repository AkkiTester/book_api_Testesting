import pytest
import requests
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def test_base_url():
    LogGen.loggen().info("************Test_Base_URL***********")
    response=requests.get(ReadConfig.getBaseURL())
    print(response.text)
    assert response.status_code==200
    LogGen.loggen().info("************Test_Base_URL_Passed***********")

def test_base_url_time():
    LogGen.loggen().info("************Test_Base_URL_time1sec***********")
    response=requests.get(ReadConfig.getBaseURL(),timeout=1.5)
    print(response.text)
    assert response.status_code==200
    LogGen.loggen().info("************Test_Base_URL_time1_Passed***********")



def test_url_status():
    LogGen.loggen().info("************Test_URL_status***********")
    response=requests.get(ReadConfig.getUrlStatus())
    print(response.text)
    assert response.status_code==200
    LogGen.loggen().info("************Test_URL_status_Passed***********")

def test_url_status_time():
    LogGen.loggen().info("************Test_URL_status_time***********")
    response=requests.get(ReadConfig.getUrlStatus(),timeout=1)
    print(response.text)
    assert response.status_code==200
    LogGen.loggen().info("************Test_URL_status_Passed***********")