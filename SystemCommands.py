"""
    Chatbot & OS Assistant
    Developed By: Osama Yousef
"""

__version__ = '1.0.0'
__author__ = 'Osama Yousef'
__email__ = 'su.osamayousef@gmail.com'
__url__ = 'https://github.com/osamayo'


from datetime import datetime
import subprocess
import webbrowser
import os
import re
import pyautogui
import ctypes
import time


class SysCmds:

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year_months = ["January", "February", "March", "April", "May", "June", "July", "August", "October", "September", "November", "December"]

    @staticmethod
    def getTime():
        hour = datetime.now().hour
        minutes = datetime.now().minute
        if hour > 12:
            hour -= 12
            if hour < 10:
                hour = "0" + str(hour)
            else:
                hour = str(hour)

            if minutes < 10:
                minutes = "0" + str(minutes)
            else:
                minutes = str(minutes)

            return hour + ":" + minutes + " PM"
        else:
            if hour < 10:
                hour = "0" + str(hour)
            else:
                hour = str(hour)

            if minutes < 10:
                minutes = "0" + str(minutes)
            else:
                minutes = str(minutes)
            return hour + ":" + minutes + " AM"

    @staticmethod
    def getDate():
        week_day = SysCmds.week_days[datetime.now().weekday()]
        month = SysCmds.year_months[datetime.now().month]
        day = int(datetime.now().day)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
        return week_day + " " + day + " " + month + " " + str(datetime.now().year)

    @staticmethod
    def getWeather():
        pass

    @staticmethod
    def openConfig():
        pass

    @staticmethod
    def openMusic():
        pass

    @staticmethod
    def openSettings():
        pass

    @staticmethod
    def openCamera():
        subprocess.run('start microsoft.windows.camera:', shell=True)


    @staticmethod
    def openVideos():
        pass

    @staticmethod
    def openPictures():
        pass

    @staticmethod
    def openBridge():
        pass

    @staticmethod
    def openCalculator():
        subprocess.Popen([r'C:\WINDOWS\system32\calc.exe'])


    @staticmethod
    def lockWindows():
        time.sleep(3)
        ctypes.windll.user32.LockWorkStation()

    @staticmethod
    def shutdownWindows():
        os.system("shutdown /s /t 5")


    @staticmethod
    def sleepWindows():
        time.sleep(3)
        os.system("shutdown /h")


    @staticmethod
    def restartWindows():
        os.system("shutdown /r /t 5")

    @staticmethod
    def openTerminal():
        subprocess.Popen([r'C:\WINDOWS\system32\cmd.exe'])

    @staticmethod
    def takeScreenshot(path):
        entries = os.listdir(path)
        image = "Screenshot-[0-9]*.png"
        lastNum = 0
        for file in entries:
            # print(file)
            if re.match(image, file):
                lastNum = int(str(file.split("-")[1]).split(".")[0]) + 1

        screenhot = pyautogui.screenshot()
        file_path = path + '\\' + "Screenshot-" + str(lastNum) + ".png"
        screenhot.save(file_path)


    @staticmethod
    def openNotes():
        subprocess.Popen([r'C:\WINDOWS\system32\notepad.exe'])


    @staticmethod
    def openFacebook():
        webbrowser.open("https://facebook.com/")

    @staticmethod
    def openYoutube():
        webbrowser.open("https://youtube.com/")

    @staticmethod
    def openStackoverflow():
        webbrowser.open("https://stackoverflow.com")

    @staticmethod
    def openMessenger():
        webbrowser.open("https://www.messenger.com/")

    @staticmethod
    def openWhatsapp():
        webbrowser.open("https://web.whatsapp.com/")

    @staticmethod
    def searchFor(text):
        text = "https://www.google.com/search?q=" + text
        webbrowser.open(text)
