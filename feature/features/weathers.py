import Speech
import requests

class weather:
    def __init__(self):
        self.api_key="b10aa51d1aa1aa73f9eaf7e3186c410f"
        self.sp=Speech.speech()
        self.base_url = "http://api.openweathermap.org / data / 2.5 / weather?"

    def report(self):
        # Google Open weather website
        # to get API of Open weather
        # self.sp.text_to_speech(" City name ")
        # city_name = self.sp.speech_to_text()
        # complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city_name

        query = 'q=' + "bareilly"
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?'+str(query)+'&APPID=b10aa51d1aa1aa73f9eaf7e3186c410f&units=metric')
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            """print("Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
                weather_description))"""

            self.sp.text_to_speech("Today Temperature is"+str(current_temperature))
            self.sp.text_to_speech("today climate is"+str(weather_description))
        else:
            self.sp.text_to_speech(" City Not Found ")