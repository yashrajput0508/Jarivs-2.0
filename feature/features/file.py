import os
import Speech
import psutil
import webbrowser as wb
files={
"chrome":"C://Program Files (x86)//Google//Chrome//Application//chrome.exe",
'firefox':"C://Program Files//Mozilla Firefox//firefox.exe",
'microsoft edge':"C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe",
'adobe reader':"C://Program Files (x86)//Adobe//Reader 11.0//Reader//AcroRd32.exe",
'python':"C://Users//Yash//AppData//Local//Programs//Python//Python37//python.exe",
'typing trainer':"C://Program Files (x86)//Typing Trainer//TypingTrainer.exe",
'eclispe':"C://Users//Yash//eclipse//cpp-2020-092//eclipse//eclipse.exe",
'pycharm':"C://Program Files//JetBrains//PyCharm Community Edition 2019.2.3//bin//pycharm64.exe",
'intellij':"C://Program Files//JetBrains//IntelliJ IDEA Community Edition 2021.1.1//bin//idea64.exe",
'vs code':"C://Users//Yash//AppData//Local//Programs//Microsoft VS Code//Code.exe",
"type speed":"‪C://Users//Yash//Desktop//Type Speed.lnk",
'sublime text':"C://Program Files//Sublime Text 3//sublime_text.exe",
'atom':"C://Users//Yash//AppData//Local//atom//atom.exe",
'calculator':"‪C://Users//Yash//Desktop//Calculator.lnk",
'calender':"‪C://Users//Yash//Desktop//Calendar.lnk",
'notepad':"‪C://Users//Yash//Desktop//Notepad.lnk",
'task manager':"C://ProgramData//Microsoft//Windows//Start Menu//Programs//System Tools//Task Manager.lnk"
}

url_file={
    "youtube":"www.youtube.com",
    "stack overflow":"https://stackoverflow.com",
    "google":"www.google.com",
    "github":"https://github.com",
    "geeksofgeeks":"https://www.geeksforgeeks.org",
    "whatsapp":"https://web.whatsapp.com"
}

class file:

    def __init__(self):
        self.sp=Speech.speech()

    def open_file(self,file_add,file_name,isfile,isexists):
        """open the file which you want to open"""
        try:
            if isexists==True:
                if isfile==True:
                    self.sp.text_to_speech("opening "+file_name+", sir")
                    "Hidden secret is ? is """
                    os.startfile(file_add.replace("‪",""))
                    self.sp.text_to_speech("File is started , sir")
                elif isfile==False:
                    self.sp.text_to_speech("opening " + file_name + ", sir")
                    wb.open(file_add)
                    self.sp.text_to_speech("url is opened , sir")
            else:
                self.sp.text_to_speech("File not found, sir")
        except Exception as e:
            self.sp.text_to_speech("File not found, sir")


    def open(self,input):

        """Search the file index your want to found and open it"""
        self.sp.text_to_speech("Searching file , sir")
        for i in files.keys():
            if i in input:
                self.open_file(files[i],i,True,True)
                break
        else:
            for i in url_file.keys():
                if i in input:
                    self.open_file(url_file[i],i,False,True)
                    break
            else:
                self.open_file("", "", False, False)

    def close(self,input):
        self.sp.text_to_speech("Searching file , sir")
        for i in files.keys():
            if i in input:
                return [files[i],i,True]
        else:
            return ["", "", False]

    def close_file(self, input):
        try:
            result = self.close(input)
            if result[2] == True:
                self.sp.text_to_speech("closing " + result[1] + ", sir")
                "Hidden secret is ? is """
                try:
                    for process in psutil.process_iter():
                        if os.path.basename(result[0]).lower().replace("lnk",'exe')==process.name().lower():
                            process.kill()
                            break
                except Exception as e:
                    pass
                self.sp.text_to_speech("File is closed , sir")
            else:
                self.sp.text_to_speech("File not found, sir")
        except Exception as e:
            self.sp.text_to_speech("File not found, sir")