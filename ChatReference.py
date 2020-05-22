"""
    Chatbot & OS Assistant
    Developed By: Osama Yousef
"""

__version__ = '1.0.0'
__author__ = 'Osama Yousef'
__email__ = 'su.osamayousef@gmail.com'
__url__ = 'https://github.com/osamayo'


class ChatBotReference:
    main_reference = {"Unknown Value": ["Sorry, Couldn't get what you said can you repeat please!",
                                        "I am really sorry! can you say it again",
                                        "Didn't got you, can you repeat please!"],
                      "Network Error": ["There 's an error in your internet connection! please check out your connection",
                                        "Oops an error in your Internet connection 've been occurred, Please try again later",
                                        "Oops it seems like your are offline right now!",
                                        "I am really sorry! Can you check your internet connection"],
                      }

    howAreYou = ["How are you?", "How’s it going?", "Are you well?", "What’s up?", "All right?"]
    expressHappiness = ["Excellent, Glad to hear that.", "I'm really happy for you.", "Nice to hear that.", "Good to hear that."]
    expressSadness = ["I'm really sorry for you.", "I feel bad for you"]

    goodMorning = "Good morning, How are you?"
    goodAfternoon = "Good afternoon, How are you?"
    goodEvening = "Good evening, How are you?"
    goodNight = "Good night, How are you?"
    greetings = [goodAfternoon, goodEvening, goodNight, goodMorning]
    assistantName = "I'm just a robot"
    aboutAssistant = "I'm your assistant here. You can ask me to do something for you."
    defaultAboutAssistant = "I am just an artificial intelligence."
    robotAge = "I'm a your robot! You should know my age."
    gladFeeling = "Excellent, Glad to hear that."
    badFeeling = "I'm really sorry for you."
    time = "Asking about the time"
    date = "Asking about the date"
    weather = "Asking about the weather"
    
    usual_talk = [
            ["Good morning", goodMorning],
            ["Good afternoon", goodAfternoon],
            ["Good evening", goodEvening],
            ["Good night", goodNight],
            ["What's your name?", assistantName],
            ["Tell me your name", assistantName],
            ["Who 're you?", aboutAssistant],
            ["Who are you?", aboutAssistant],
            ["How old are you?", robotAge],
            ["What age are you?", robotAge],
            ["I'm fine", gladFeeling],
            ["Fine", gladFeeling],
            ["I'm good", gladFeeling],
            ["I feel awesome", gladFeeling],
            ["I'm happy", gladFeeling],
            ["I'm ok", gladFeeling],
            ["I'm cool", gladFeeling],
            ["Not good", badFeeling],
            ["I'm sad", badFeeling],
            ["I feel depressed", badFeeling],
            ["What time is it?", time],
            ["What is the time?", time],
            ["What's the date?", date],
            ["What date is it?", date],
            ["What's it like outside?", weather],
            ["How's the weather?", weather],
            ["What's the temperature?", weather]
    ]

    usual_talk_re = [
        ["[a-z ]*good morning[a-z ]*", goodMorning],
        ["[a-z ]*good afternoon[a-z ]*", goodAfternoon],
        ["[a-z ]*good evening[a-z ]*", goodEvening],
        ["[a-z ]*good night[a-z ]*", goodNight],
        ["[a-z ]*what('s| is) your[a-z ]*name[a-z ?]*", assistantName],
        ["[a-z ]*tell[a-z ]*your[a-z ]*name[a-z ?]*", assistantName],
        ["[a-z ]*what time is it[a-z ]*", time],
        ["[a-z ]*what('s| is) the time[a-z ]*", time],
        ["[a-z ]*what('s| is) (the date|today's date|date)[a-z ]*", date],
        ["[a-z ]*what (date|day|month|year|season) (is it|are we|we are|we 're|are|is)[a-z ]*", date],
        ["[a-z ]*how old are you[a-z ]*", robotAge],
        ["[a-z ]*what age are you[a-z ]*", robotAge],
        ["[a-z ]*(i'm|i am|am|i feel|feel)[a-z ]*(fine|good|awesome|happy|ok|cool)[a-z ]*", gladFeeling],
        ["[a-z ]*(fine|good|awesome|happy|ok|cool)[a-z ]*", gladFeeling],
        ["[a-z ]*(not|am not|i'm not|i am not|don't feel|i don't feel)[a-z ]*(good|fine|ok)[a-z ]*", badFeeling],
        ["[a-z ]*(i feel|am|i'm|feel)[a-z ]*(bad|depressed|unhappy|upset|sad)[a-z ]*", badFeeling],
        ["[a-z ]*what('s| is) it (look like|like) outside[a-z ]*", weather],
        ["[a-z ]*how('s| is)( the| )( |)weather[a-z ]*", weather],
        ["[a-z ]*what('s| is)( the| )( |)temperature[a-z ]*", weather]
    ]

    config = "Opening the configuration"
    music = "Opening the music"
    settings = "Opening the settings"
    camera = "Opening the camera"
    videos = "Opening the videos"
    bridge = "Opening the bridge"
    calculator = "Opening the calculator"
    lock_system = "Locking the system"
    terminal = "Opening the terminal"
    pictures = "Opening the pictures"
    screenshot = "Taking a screenshot"
    shutdown = "Shutdown"
    sleep = "Sleep"
    restart = "Restart"
    youtube = "Opening youtube"
    stackoverflow = "Opening stackoverflow"
    messenger = "Opening messenger"
    whatsapp = "Opening whatsapp"
    facebook = "Opening facebook"
    notes = "Opening notepad"
    exit_assistant = "Closing the assistant, Good bye!"
    
    OS_Commands = [
        ["Open the configuration", config],
        ["Open the music", music],
        ["Open the settings", settings],
        ["Open the camera", camera],
        ["Open the videos", videos],
        ["Open the bridge", bridge],
        ["Open the calculator", calculator],
        ["Lock the system", lock_system],
        ["Open the terminal", terminal],
        ["Open the cmd", terminal],
        ["Open the command prompt", terminal],
        ["Open the pictures", pictures],
        ["Take a screenshot", screenshot],
        ["Shutdown the system", shutdown],
        ["Sleep the system", sleep],
        ["Restart the system", restart],
        ["Open youtube", youtube],
        ["Open stackoverflow", stackoverflow],
        ["Open messenger", messenger],
        ["Open whatsapp", whatsapp],
        ["Open facebook", facebook],
        ["Open the note", notes],
        ["Close the assistant", exit_assistant],
        ["Exit from the assistant", exit_assistant]
    ]

    OS_Commands_Re = [
        ["[a-z ]*(show|open)[a-z ]*(configuration|config)[a-z ]*", config],
        ["[a-z ]*(open|get)[a-z ]*music[a-z ]*", music],
        ["[a-z ]*(open|get)[a-z ]*(settings|setting)[a-z ]*", settings],
        ["[a-z ]*(open|get)[a-z ]*camera[a-z ]*", camera],
        ["[a-z ]*(open|get)[a-z ]*videos[a-z ]*", videos],
        ["[a-z ]*(open|get)[a-z ]*pictures[a-z ]*", pictures],
        ["[a-z ]*(open|get)( the|) bridge[a-z ]*", bridge],
        ["[a-z ]*(open|get)( the|) calculator[a-z ]*", calculator],
        ["[a-z ]*(open|get)( the|) youtube[a-z ]*", youtube],
        ["[a-z ]*(open|get)( the|) stackoverflow[a-z ]*", stackoverflow],
        ["[a-z ]*(open|get)( the|) messenger[a-z ]*", messenger],
        ["[a-z ]*(open|get)( the|) whatsapp[a-z ]*", whatsapp],
        ["[a-z ]*(open|get)( the|) facebook[a-z ]*", facebook],
        ["[a-z ]*(open|get)( the|) (terminal|cmd|command prompt)[a-z ]*", terminal],
        ["[a-z ]*(open|get)( the|) (note|notes|notepad)[a-z ]*", notes],
        ["[a-z ]*(lock|lockdown|lock down)( the | )(system|os|operating system|windows)[a-z ]*", lock_system],
        ["[a-z ]*take[a-z ]*screenshot[a-z ]*", screenshot],
        ["[a-z ]*(shutdown|poweroff|power off) (the |)(system|os|operating system|windows)[a-z ]*", shutdown],
        ["[a-z ]*sleep (the |)(system|os|operating system|windows)[a-z ]*", sleep],
        ["[a-z ]*(restart|reboot) (the |)(system|os|operating system|windows)[a-z ]*", restart],
        ["[a-z ]*(close|exit)[a-z ]*assistant[a-z ]*", exit_assistant]
    ]

    confirm_re = ["yes", "confirm"]
    reject_re = ["no", "cancel"]

    times = ["The current time is: ", "The time now is: ", "Time now: "]
    dates = ["Today is: "]
    weather = ["Today The Weather is: "]

