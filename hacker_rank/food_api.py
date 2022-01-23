import requests


def getTopFoodRatedOutlets(city):
    response = requests.get("https://jsonmock.hackerrank.com/api/food_outlets?city=Seattle&page=1")
    result = response.json()
    total_pages = result['total_pages']
    obj = {}
    for i in range(1, total_pages + 1):
        query = {'city': city, 'page': i}
        response = requests.get("https://jsonmock.hackerrank.com/api/food_outlets", params=query)
        result = response.json()
        for j in range(len(result['data'])):
            obj[result['data'][j]['name']] = result['data'][j]['user_rating']['average_rating']

    print(obj)
    sorted_obj = sorted(obj.items(), key=lambda x:x[1], reverse=True)
    print(sorted_obj)


getTopFoodRatedOutlets("seattle")
