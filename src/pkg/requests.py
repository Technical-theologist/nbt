import requests
from constants import Constants

def fetchProducts():
    params = {"status": 1}

    response = requests.get(Constants.productsApi, params=params)

    if response.status_code == 200:
        successData = response.json()
        return successData.get("success"), 200
    else:
        return [], 400

def fetchTagModelsWithProductId(productId):
    params = {"productid": productId}
    response = requests.get(Constants.tagsApi, params=params)
    if response.status_code == 200:
        successData = response.json()
        print(response.url)
        return successData.get("success"), 200
    else:
        return [], 400