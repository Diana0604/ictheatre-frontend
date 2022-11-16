import requests
from constants import apiConstants

# get array with info on all companies (except for player company)
def getCompaniesArray():
    try :
        companies = requests.get(
            f"{apiConstants.BASEURL}/companies")
        companiesJson = companies.json()
        return companiesJson
    except :
        print("not able to connect to database")
        return [{"name": "Demo Broker", "currentPricePerShare" : "0.00"} , { "name": "Demo Broker", "currentPricePerShare" : "0.00"}]
