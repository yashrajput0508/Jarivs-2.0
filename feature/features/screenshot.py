import pyautogui
import time
import Speech

"""IT takes the current screen shot of your current desktop"""

class screenshot:
    def __init__(self):
        self.sp=Speech.speech()

    def image(self):
        self.sp.text_to_speech("screenshot taking ,sir")
        times=time.time()
        name_img=r"C:\Users\Yash\PycharmProjects\Jarvis\sshot\{}.png".format(str(times))
        img=pyautogui.screenshot(name_img)
        self.sp.text_to_speech("screenshot is taken, sir")
        img.show()