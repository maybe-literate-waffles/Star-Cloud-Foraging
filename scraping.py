import requests as rq

BASE_URL = "https://api.open-meteo.com/v1"
LATITUDE = "latitude=35.6762,51.5074,1.3521,40.7128,-33.8688"
LONGITUDE = "longitude=139.6503,-0.1278,103.8198,-74.0060,151.2093"
TIMEZONE = "timezone=Asia%2FTokyo,Europe%2FLondon,Asia%2FSingapore,America%2FNew_York,Australia%2FSydney"


def get_data():
    full_url = (
        f"{BASE_URL}/forecast?{LATITUDE}&{LONGITUDE}&current=temperature_2m&{TIMEZONE}"
    )
    response = rq.get(full_url)
    return response.json()


# test bench
# response = get_data()

# output = response[0]["current"][""]

# print(output)
