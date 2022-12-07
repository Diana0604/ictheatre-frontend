import requests
#from constants import apiConstants

BASEURL = "http://192.168.100.1:3000/mysql"  # for dev in non raspbery computer
#BASEURL = "http://localhost:3000/mysql"  # for dev in non raspbery computer


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
        return {
            1: {
                "name": "Demo Company One",
                "currentPricePerShare": 1.00,
                "id": 1,
            },
            2: {
                "name": "Demo Company Two",
                "currentPricePerShare": 0.00,
                "id": 2
            }
        }


# get array with info player company information
def getPlayerInfo():
    try:
        playerCompany = requests.get(f"{BASEURL}/companies/playercompany")
        playerJson = playerCompany.json()
        return playerJson
    except:
        print("not able to connect to database - player info")
        return {
            "name": "Best Company Ever",
            "stockValueScore": 0,
            "publicRelationsIndex": 0.5,
            "liquidAssets": 500000
        }


def getShowStatus():
    try:
        showStatus = requests.get(f"{BASEURL}/showstatus")
        showStatusJson = showStatus.json()
        return showStatusJson
    except:
        print("not able to connect to database - showstatus")
        return {
            "timeSinceStartup": 0,
            "isPlaying": False,
        }


def getSellersList():
    try:
        sellersList = requests.get(f"{BASEURL}/sellers")
        sellersListJson = sellersList.json()
        return sellersListJson
    except:
        print("not able to connect to database")
        return {
            "sellers": [{
                "name": "Demo Broker",
                "id": 3
            }],
            "shareBundles": [{
                "ownerId": 3,
                "companyId": 1,
                "quantity": 1,
            }, {
                "ownerId": 3,
                "companyId": 2,
                "quantity": 0
            }]
        }
