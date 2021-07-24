import requests
import Speech
"""It tells the current covid-19 cases ,death, recovered"""
class covid:
    def __init__(self):
        self.sp=Speech.speech()

    def covid19(self):
        r=requests.get("https://coronavirus-19-api.herokuapp.com/all")
        json=r.json()
        self.sp.text_to_speech("Total Cases are {}, Total death are {}, Total recovered are {}".format(json['cases'],json['deaths'],json['recovered']))
