import requests
from constants import apiConstants


def getCompaniesArray():
    companies = requests.get(
        f"{apiConstants.BASEURL}/companies")
    companiesJson = companies.json()
    return companiesJson
