import requests
from constants import apiConstants


# get array with info on all companies (except for player company)
def getCompaniesArray():
    try:
        companies = requests.get(f"{apiConstants.BASEURL}/companies")
        companiesJson = companies.json()
        return companiesJson
    except:
        print("not able to connect to database")
        return [{
            "name": "Demo Company",
            "currentPricePerShare": "0.00"
        }, {
            "name": "Demo Company",
            "currentPricePerShare": "0.00"
        }]


# get array with info player company information
def getPlayerInfo():
    try:
        playerCompany = requests.get(f"{apiConstants.BASEURL}/playercompany")
        playerJson = playerCompany.json()
        return playerJson
    except:
        print("not able to connect to database")
        return {
            "name": "Best Company Ever",
            "stockValueScore": 0,
            "publicRelationsIndex": 0.5,
            "liquidAssets": 500000
        }


def getSellersList():
    try:
        sellersList = requests.get(f"{apiConstants.BASEURL}/sellers")
        sellersListJson = sellersList.json()
        return sellersListJson
    except:
        print("not able to connect to database")
        return {"name": "Demo Broker"}