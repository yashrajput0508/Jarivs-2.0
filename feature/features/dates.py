import datetime
from datetime import date
import Speech

class dates:
    def __init__(self):
        self.dt=datetime
        self.sp=Speech.speech()
    def time(self):
        now = self.dt.datetime.now()
        current_time = now.strftime("%H hour,%M minute")
        self.sp.text_to_speech("The current time is,"+current_time)
    def date(self):
        todays_date = date.today()
        self.sp.text_to_speech("Today date is"+str(todays_date.day)+","+str(todays_date.month)+","+str(todays_date.year))
    def day(self):
        self.sp.text_to_speech(str(datetime.datetime.today().strftime('%A')))