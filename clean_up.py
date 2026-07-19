# from scraping import get_data


def clean(weather):
    clean_weath = []

    length = len(weather)

    # print(f"len: {length}")

    for i in range(length):
        # print(f"i1: {i}")

        temperature = weather[i]["current"]["temperature_2m"]
        temp_unit = weather[i]["current_units"]["temperature_2m"]
        time = weather[i]["current"]["time"]
        latitude = weather[i]["latitude"]
        longitude = weather[i]["longitude"]
        timezone = weather[i]["timezone"]

        # print(f"i2: {i}")

        clean_weath.append(
            {
                "temperature": temperature,
                "unit": temp_unit,
                "time": time,
                "latitude": latitude,
                "longitude": longitude,
                "timezone": timezone,
            }
        )

    return clean_weath


# test bench
# response = get_data()
# clean_response = clean(response)

# num = 5

# for i in range(num):
#     print(i)

# print(clean_response)
