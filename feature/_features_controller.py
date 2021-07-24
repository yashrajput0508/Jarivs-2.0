from feature.features import read_text, screenshot, covid, dates, file, jokes, emails, search_google,window_features,wishing,weathers,whatsapp


class features:
    def __init__(self,input,output):

        self.output=output
        self.input=input
        self.dates= dates.dates()
        self.covid= covid.covid()
        self.read_text= read_text.read()
        self.screenshot= screenshot.screenshot()
        self.email= emails
        self.jokes= jokes.jokes()
        self.google= search_google.searching()
        self.file= file.file()
        self.window=window_features.window()
        self.wishing=wishing.wish_me()
        self.weather=weathers.weather()
        self.whatsapp=whatsapp.whatsapps()
        self.operate()

    def operate(self):

        if "@time" in self.output:
            self.dates.time()
        elif "@date" in self.output:
            self.dates.date()
        elif "@day" in self.output:
            self.dates.day()
        elif "@covid" in self.output:
            self.covid.covid19()
        elif "@read" in self.output:
            self.read_text.readtext()
        elif "@screenshot" in self.output:
            self.screenshot.image()
        elif "@email" in self.output:
            self.email.email()
        elif "@joke" in self.output:
            self.jokes.tell_jokes()
        elif "@wiki" in self.output:
            self.google.find_wiki()
        elif "@google" in self.output:
            self.google.find_google()
        elif "@open" in self.output:
            self.file.open(self.input)
        elif "@close" in self.output:
            self.file.close_file(self.input)
        elif "@shutdown" in self.output:
            self.window.shutdown()
        elif "@restart" in self.output:
            self.window.restart()
        elif "@weather" in self.output:
            self.weather.report()
        elif "@wish" in self.output:
            self.wishing.wish()
        elif "@introduction" in self.output:
            self.wishing.introduction()
        elif "@whatsapp" in self.output:
            self.whatsapp.send_message()
