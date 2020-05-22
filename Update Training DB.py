from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import json
from ChatReference import ChatBotReference

default_response = 'Sorry, couldn\'t get that!'


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

    chatbot_json = open("ChatBot Reference.json", "w")
    json_data = dict(ChatBot_Training_Files=False)
    json_text = json.dumps(json_data)
    chatbot_json.write(json_text)

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


if __name__ == '__main__':
    main()
