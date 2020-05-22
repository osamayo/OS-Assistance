"""
    Chatbot & OS Assistant
    Developed By: Osama Yousef
"""

__version__ = '1.0.0'
__author__ = 'Osama Yousef'
__email__ = 'su.osamayousef@gmail.com'
__url__ = 'https://github.com/osamayo'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from ChatReference import ChatBotReference
from SpeechRecognition import Speech
import re
import random
from SystemCommands import SysCmds
import time as tm
import json


default_response = 'Sorry, couldn\'t get that!'
screenshot_path = r"C:Users\Osama Yousef\Desktop"


def main():
    bot = ChatBot(name="Assistant", read_only=True,
                  preprocessors=[
                    'chatterbot.preprocessors.clean_whitespace',
                  ], logic_adapters=[
                      {'import_path': 'chatterbot.logic.BestMatch',
                       'default_response': default_response,
                       'maximum_similarity_threshold': 0.90},
                      {'import_path': 'chatterbot.logic.MathematicalEvaluation',
                       'default_response': default_response,
                       'maximum_similarity_threshold': 0.90}
                    ], database_uri='sqlite:///database.db')

    training_db_exist = False
    chatbot_json = open("ChatBot Reference.json", "r+")
    json_text = chatbot_json.read()
    json_data = json.loads(json_text)
    if json_data["ChatBot_Training_Files"]:
        training_db_exist = True

    if not training_db_exist:
        trainerOne = ChatterBotCorpusTrainer(bot)
        trainerTwo = ListTrainer(bot)

        trainerOne.train('chatterbot.corpus.english')
        for i in ChatBotReference.usual_talk:
            trainerTwo.train(i)

        json_data["ChatBot_Training_Files"] = True
        json_text = json.dumps(json_data)
        chatbot_json.seek(0)
        chatbot_json.write(json_text)
        chatbot_json.write("\n")

    chatbot_json.close()

    sr = Speech("en")

    while True:
        # user_input = input("Osama Yousef> ")
        print("Listening ...")
        user_input = sr.getAudio()

        if user_input in ChatBotReference.main_reference["Unknown Value"]:
            output = ChatBotReference.main_reference["Unknown Value"][random.randint(0, len(ChatBotReference.main_reference["Unknown Value"]) - 1)]
            print("Bot> " + output)
            # output = sr.translate(output, "ar")
            sr.Say(output, "en")
            tm.sleep(6)
            continue

        elif user_input in ChatBotReference.main_reference["Network Error"]:
            output = ChatBotReference.main_reference["Network Error"][random.randint(0, len(ChatBotReference.main_reference["Network Error"]) - 1)]
            print("Bot> " + output)
            # output = sr.translate(output, "ar")
            sr.Say(output, "en")
            tm.sleep(6)
            continue

        print("Osama Yousef> " + user_input)
        user_input = user_input.lower()
        # user_input = sr.translate(user_input, "en")

        bot_response = str(bot.get_response(user_input))

        if bot_response == default_response:
            re_chatreference = ChatBotReference.usual_talk_re
            re_chatreference.extend(ChatBotReference.OS_Commands_Re)
            # retrieve response from the re chat reference
            for rule in re_chatreference:
                if re.match(rule[0], user_input):
                    bot_response = rule[1]
                    break

        # Object from SysCmds
        sys = SysCmds()
        if bot_response in ChatBotReference.greetings:

            bot_response = bot_response.split(",")[0] + " " + ChatBotReference.howAreYou[random.randint(0, len(ChatBotReference.howAreYou) - 1)]

        elif bot_response == ChatBotReference.gladFeeling:

            bot_response = ChatBotReference.expressHappiness[random.randint(0, len(ChatBotReference.expressHappiness) - 1)]

        elif bot_response == ChatBotReference.badFeeling:

            bot_response = ChatBotReference.expressSadness[random.randint(0, len(ChatBotReference.expressSadness) - 1)]

        elif bot_response == ChatBotReference.time:

            # get time
            time = sys.getTime()
            bot_response = ChatBotReference.times[random.randint(0, len(ChatBotReference.times) - 1)] + time

        elif bot_response == ChatBotReference.date:

            # get date
            date = sys.getDate()
            bot_response = ChatBotReference.dates[random.randint(0, len(ChatBotReference.dates) - 1)] + date

        elif bot_response == ChatBotReference.weather:

            # get weather
            weather = ""
            bot_response = ChatBotReference.weather[random.randint(0, len(ChatBotReference.weather) - 1)] + weather

        elif bot_response == ChatBotReference.config:

            # open config
            sys.openConfig()

        elif bot_response == ChatBotReference.music:

            # open music
            sys.openMusic()

        elif bot_response == ChatBotReference.settings:

            # open settings
            sys.openSettings()

        elif bot_response == ChatBotReference.camera:

            # open camera
            sys.openCamera()
            
        elif bot_response == ChatBotReference.videos:

            # open videos
            sys.openVideos()

        elif bot_response == ChatBotReference.bridge:

            # open bridge
            sys.openBridge()

        elif bot_response == ChatBotReference.calculator:

            # open calculator
            sys.openCalculator()
            
        elif bot_response == ChatBotReference.lock_system:

            # require confirmation
            while True:
                # confirm = sr.getAudio()
                print("Are you sure to lock the system?")
                sr.Say("Are you sure to lock the system?", "en")
                tm.sleep(3)

                print("Say \"yes\" or \"confirm\" to lock the system")
                sr.Say("Say \"yes\" or \"confirm\" to lock the system", "en")
                tm.sleep(3)

                print("Say \"no\" or \"cancel\" to cancel operation")
                sr.Say("Say \"no\" or \"cancel\" to cancel operation", "en")
                tm.sleep(3)

                # confirm = input("Confirm: ")
                confirm = sr.getAudio()
                confirm = confirm.lower()

                if confirm in ChatBotReference.confirm_re:
                    # lock system
                    print(confirm)
                    print("Locking the system ..")
                    sr.Say("Locking the system ..", "en")
                    sys.lockWindows()
                    break

                elif confirm in ChatBotReference.reject_re:
                    print(confirm)
                    print("Cancelling operation ..")
                    sr.Say(confirm, "en")
                    bot_response = "Lock Cancelled"
                    break

                elif confirm in ChatBotReference.main_reference["Unknown Value"]:
                    message = ChatBotReference.main_reference["Unknown Value"][random.randint(0, len(ChatBotReference.main_reference["Unknown Value"]) -1 )]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                elif confirm in ChatBotReference.main_reference["Network Error"]:
                    message = ChatBotReference.main_reference["Network Error"][
                        random.randint(0, len(ChatBotReference.main_reference["Network Error"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                else:
                    print("Failed to confirm the operation, Please try again.")

        elif bot_response == ChatBotReference.terminal:

            # open terminal
            sys.openTerminal()

        elif bot_response == ChatBotReference.pictures:

            # open pictures
            sys.openPictures()

        elif bot_response == ChatBotReference.screenshot:

            # take screenshot
            sys.takeScreenshot(screenshot_path)
            
        elif bot_response == ChatBotReference.shutdown:

            # require confirmation
            while True:
                # confirm = sr.getAudio()
                print("Are you sure to shutdown the system?")
                sr.Say("Are you sure to shutdown the system?", "en")
                tm.sleep(3)

                print("Say \"yes\" or \"confirm\" to shutdown the system")
                sr.Say("Say \"yes\" or \"confirm\" to shutdown the system", "en")
                tm.sleep(3)

                print("Say \"no\" or \"cancel\" to cancel operation")
                sr.Say("Say \"no\" or \"cancel\" to cancel operation", "en")
                tm.sleep(3)

                # confirm = input("Confirm: ")
                confirm = sr.getAudio()
                confirm = confirm.lower()

                if confirm in ChatBotReference.confirm_re:
                    # shutdown system
                    print(confirm)
                    print("Shutting down the system ..")
                    sr.Say("Shutting down the system ..", "en")
                    sys.shutdownWindows()
                    quit()

                elif confirm in ChatBotReference.reject_re:
                    print(confirm)
                    print("Cancelling operation ..")
                    sr.Say(confirm, "en")
                    bot_response = "Shutting down Cancelled"
                    break

                elif confirm in ChatBotReference.main_reference["Unknown Value"]:
                    message = ChatBotReference.main_reference["Unknown Value"][
                        random.randint(0, len(ChatBotReference.main_reference["Unknown Value"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                elif confirm in ChatBotReference.main_reference["Network Error"]:
                    message = ChatBotReference.main_reference["Network Error"][
                        random.randint(0, len(ChatBotReference.main_reference["Network Error"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                else:
                    print("Failed to confirm the operation, Please try again.")

        elif bot_response == ChatBotReference.sleep:

            # require confirmation
            while True:
                # confirm = sr.getAudio()
                print("Are you sure to sleep the system?")
                sr.Say("Are you sure to sleep the system?", "en")
                tm.sleep(3)

                print("Say \"yes\" or \"confirm\" to sleep the system")
                sr.Say("Say \"yes\" or \"confirm\" to sleep the system", "en")
                tm.sleep(3)

                print("Say \"no\" or \"cancel\" to cancel operation")
                sr.Say("Say \"no\" or \"cancel\" to cancel operation", "en")
                tm.sleep(3)

                # confirm = input("Confirm: ")
                confirm = sr.getAudio()
                confirm = confirm.lower()

                if confirm in ChatBotReference.confirm_re:
                    # sleep system
                    print(confirm)
                    print("Sleeping the system ..")
                    sr.Say("Sleeping down the system ..", "en")
                    sys.sleepWindows()
                    break

                elif confirm in ChatBotReference.reject_re:
                    print(confirm)
                    print("Cancelling operation ..")
                    sr.Say(confirm, "en")
                    bot_response = "Sleeping Cancelled"
                    break

                elif confirm in ChatBotReference.main_reference["Unknown Value"]:
                    message = ChatBotReference.main_reference["Unknown Value"][
                        random.randint(0, len(ChatBotReference.main_reference["Unknown Value"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                elif confirm in ChatBotReference.main_reference["Network Error"]:
                    message = ChatBotReference.main_reference["Network Error"][
                        random.randint(0, len(ChatBotReference.main_reference["Network Error"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                else:
                    print("Failed to confirm the operation, Please try again.")

        elif bot_response == ChatBotReference.restart:

            # require confirmation
            while True:
                # confirm = sr.getAudio()
                print("Are you sure to restart the system?")
                sr.Say("Are you sure to restart the system?", "en")
                tm.sleep(3)

                print("Say \"yes\" or \"confirm\" to restart the system")
                sr.Say("Say \"yes\" or \"confirm\" to restart the system", "en")
                tm.sleep(3)

                print("Say \"no\" or \"cancel\" to cancel operation")
                sr.Say("Say \"no\" or \"cancel\" to cancel operation", "en")
                tm.sleep(3)

                # confirm = input("Confirm: ")
                confirm = sr.getAudio()
                confirm = confirm.lower()

                if confirm in ChatBotReference.confirm_re:
                    # restart system
                    print(confirm)
                    print("Restarting the system ..")
                    sr.Say("Restarting the system ..", "en")
                    sys.restartWindows()
                    quit()

                elif confirm in ChatBotReference.reject_re:
                    print(confirm)
                    print("Cancelling operation ..")
                    sr.Say(confirm, "en")
                    bot_response = "Restarting Cancelled"
                    break

                elif confirm in ChatBotReference.main_reference["Unknown Value"]:
                    message = ChatBotReference.main_reference["Unknown Value"][
                        random.randint(0, len(ChatBotReference.main_reference["Unknown Value"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                elif confirm in ChatBotReference.main_reference["Network Error"]:
                    message = ChatBotReference.main_reference["Network Error"][
                        random.randint(0, len(ChatBotReference.main_reference["Network Error"]) - 1)]
                    print("Bot> " + message)
                    sr.Say(message, "en")

                else:
                    print("Failed to confirm the operation, Please try again.")

        elif bot_response == ChatBotReference.youtube:

            # open youtube
            sys.openYoutube()

        elif bot_response == ChatBotReference.facebook:

            # open facebook
            sys.openFacebook()

        elif bot_response == ChatBotReference.stackoverflow:

            # open stackoverflow
            sys.openStackoverflow()

        elif bot_response == ChatBotReference.messenger:

            # open messenger
            sys.openMessenger()

        elif bot_response == ChatBotReference.whatsapp:

            # open whatsapp
            sys.openWhatsapp()

        elif bot_response == ChatBotReference.notes:

            # open notepad
            sys.openNotes()

        elif bot_response == ChatBotReference.exit_assistant:

            # exit
            # bot_response = sr.translate(bot_response, "ar")
            print("Bot> " + bot_response)
            # sr.Say(str(bot_response), "en")

            break
        elif bot_response == default_response:

            bot_response = "Searching For: " + user_input
            sys.searchFor(user_input)

        elif bot_response == ChatBotReference.defaultAboutAssistant:
            bot_response = ChatBotReference.aboutAssistant

        else:
            pass

        # bot_response = sr.translate(bot_response, "ar")
        print("Bot> " + bot_response)
        sr.Say(str(bot_response), "en")
        tm.sleep(2)


if __name__ == '__main__':
    main()
