#!/usr/bin/env python3

import requests
import time


def ktoc(k):
    return k - 273.15


def ktof(k):
    return (9 / 5) * ktoc(k) + 32


def get_weather(zipcode):
    # try:
    #     with open("weather_cache", "r") as cache_file:
    #         cache = cache_file.readlines()
    #         if len(cache) != 0:
    #             if (time.time() - float(cache[0].strip())) < 10 * 60:
    #                 return "".join(cache[1:]) + "\n(cached)"
    # except FileNotFoundError:
    #     pass
    #
    with open("weather_api_key", "r") as api_key:
        APPID = api_key.readlines()[0].strip()

    url = "http://api.openweathermap.org/data/2.5/weather?zip={},us".format(zipcode)
    url += "&APPID={}".format(APPID)

    request = requests.get(url)
    json = request.json()

    output = "Current weather in {}\n".format(zipcode) + \
             "\t{:.1f}°F\t{:.1f}°C\n".format(ktof(json["main"]["temp"]), ktoc(json["main"]["temp"])) + \
             "\t{}% humidity, {}".format(json["main"]["humidity"], json["weather"][0]["description"])

    # with open("weather_cache", "w") as cache_file:
    #     cache_file.write(str(time.time()) + '\n')
    #     cache_file.write(output)

    return output


def weather(bot, message):
    zipcode = message.text.split(" ")[2]
    print(zipcode)
    bot.send_message(message.chat.id, get_weather(zipcode))


def main():
    print(get_weather(77840))


if __name__ == "__main__":
    main()
