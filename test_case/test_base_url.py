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
