"""
    Chatbot & OS Assistant
    Developed By: Osama Yousef
"""

__version__ = '1.0.0'
__author__ = 'Osama Yousef'
__email__ = 'su.osamayousef@gmail.com'
__url__ = 'https://github.com/osamayo'

import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from tempfile import TemporaryFile
from pygame import mixer
import random
from ChatReference import ChatBotReference


class Speech:

    def __init__(self, language):
        self.lang = language

    @staticmethod
    def Say(text, lang):
        s = gTTS(text, lang=lang)
        temp = TemporaryFile()
        s.write_to_fp(temp)
        temp.seek(0)
        mixer.init()
        mixer.music.load(temp)
        mixer.music.play(0)

    @staticmethod
    def translate(text, dest_lang):
        translator = Translator()
        text = translator.translate(text, dest=dest_lang).text
        # print("Translate: {}".format(text))
        return text

    def getAudio(self):
        recoginzer = sr.Recognizer()
        with sr.Microphone() as mic:
            # print("Listening ..")
            audio = recoginzer.listen(mic)
            try:
                message = recoginzer.recognize_google(audio, language=self.lang)
                # print(message)
                return message
            except sr.UnknownValueError:
                message = ChatBotReference.main_reference['Unknown Value'][random.randint(0, len(ChatBotReference.main_reference['Unknown Value'])-1)]
                # print(message)
                return message
            except sr.RequestError:
                message = ChatBotReference.main_reference['Network Error'][random.randint(0, len(ChatBotReference.main_reference['Network Error'])-1)]
                # print(message)
                return message

