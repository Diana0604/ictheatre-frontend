import requests


def getCompaniesArray():
    companiesJson = requests.get(
        "http://raspberrypi:3000/mysql/companies").json()
    return companiesJson


def getStockPrice(company):
    return '$000.00'
