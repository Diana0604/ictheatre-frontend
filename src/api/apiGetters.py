import requests
#from constants import apiConstants

#BASEURL = "http://raspbx.local:3000/mysql"  # for dev in non raspbery computer
BASEURL = "http://localhost:3000/mysql"  # for dev in non raspbery computer


# get array with info on all companies (except for player company)
def getCompaniesArray():
    try:
        companies = requests.get(f"{BASEURL}/companies")
        companiesJson = companies.json()
        companiesNewJson = {}
        for company in companiesJson:
            companiesNewJson[company['id']] = company
        return companiesNewJson
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
        playerCompany = requests.get(f"{BASEURL}/companies/playercompany")
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
        sellersList = requests.get(f"{BASEURL}/sellers")
        sellersListJson = sellersList.json()
        return sellersListJson
    except:
        print("not able to connect to database")
        return {"name": "Demo Broker"}