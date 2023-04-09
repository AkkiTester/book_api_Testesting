import pytest
import json
import requests
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import testDataGen

data = {
   "clientName": testDataGen.nameLen(),
   "clientEmail": testDataGen.emailgen()
    }
token=''
def test_token_gen():
    LogGen.loggen().info("************Test_Auth_URL***********")
    response=requests.post(ReadConfig.getAuth(),json=data)
    token=response.json()
    print(token)
    assert response.status_code==201
    LogGen.loggen().info("************Test_Auth_URL_Passed***********")

print(token)