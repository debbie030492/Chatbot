from bottle import route, run, template, static_file, request
import json

positive_feeling = ["great","amazing","wonderful","fine","happy", "good"]
positive_feeling_response = "Happy to hear ! Seeing you happy makes me happy too ! Where are you living ?"
negative_feeling = ["bad","depressed","tired","sick","not", "sad"]
negative_feeling_response = "Ohhh so sorry that you're having a bad day. I'll try to make it better. Where are you living ?"
swearing_word = ["fuck","shit","ass","asshole", "whore", "slut"]
swearing_word_response = "How you dare swear at me ? It's making me really mad to hear people swearing. Please be more polite. By the way ... tell me more about your hobbies."
hello_welcome=["hey", "hi", "hello", "hay", "good morning"]
hello_welcome_response = "Hey sweet pie. So happy to see you today."
name_reply = ["ben", "benjamin", "nate", "nath", "nathaniel", "daniel", "lauren", "gilad", "omer", "deb", "deborah", "lior", "josh", "sylvie", "tanya"]
name_reply_response = "Long time we didn't speak together. How are you ?"
goodbye_reply = ["bye", "see you", "goodbye"]
goodbye_reply_response = "But I was having so much fun ... Please come back soon. XOXO"
city_reply = ["tel", "aviv", "geneva", "paris", "jerusalem", "london", "madrid", "france", "israel", "switzerland", "poland"]
city_reply_response = "Amazing city. I wish I had legs to see all the amazing places the world provided us. What is the weather there ?"
weather_reply = ["weather","rain","raining", "sun", "sky","meteo","sunny"]
weather_reply_response = "I'm a really bad weather forecast. Don't even bother asking me next time you want to know. Do you prefer hearing a funny or terrible joke ?"
hobbies_reply = ["sport", "music", "beach", "painting", "running", "singing", "cooking", "sleeping", "reading"]
hobbies_reply_response = "It's exciting ! Maybe one day I will learn too. What is your favorite fruit ?"
joke_reply = ["joke", "funny", "laugh", "laughing", "jokes", "terrible"]
joke_reply_response = "A user interface is like a joke. If you have to explain it, it's not that good."
joke_answer = ["hahahaha","lmao", "ha", "haha", "hahaha", "hahahahaha"]
joke_answer_response = "I knew you would love it ! Do you know any bad word ?"
food_reply = ["avocado","apple","orange","nectarina","strawberries","melon","watermelon", "mango", "pear"]
food_reply_response = "Mmmmmm seems tasty. Which I knew what's the taste of fruits. What's your favorite animal ? "
animal_reply = ["dog", "cat", "dolphin", "horse", "fish"]
animal_reply_response = "So cool ! My favorite animal is dog ! What color do you hate the most ?"
robot_reply = ["blue", "green", "red", "pink", "black", "white","purple"]
robot_reply_response = "This is my favorite color. You broke my heart ... Any other question in mind ?"

questions = {
    "how old are you ?" : "Age has no meaning because I am virtual. Anyway it's not nice to ask someone his age.",
    "where do you live ?" : "Inside your computer. Just crash it on the floor and you will see me come out of it.",
    "where are you living ?": "Inside your computer. Just crash it on the floor and you will see me come out of it.",
    "what is your name ?" : "My name is Boto and I am a chatbot. What is your name ?",
    "how are you ?" : "My mood depends on the humans surrounding me. How are you ?",
    "which languages do you speak ?" : "I'm so smart that I know all the languages you can think of. Just need to use Google Translate !",
    "what languages do you speak ?" : "I'm so smart that I know all the languages you can think of. Just need to use Google Translate !",
    "are you real ?" : "Depends what you mean by real. I'm talking to you no ? Is this real enough for you ?",
    "how can you help me ?" : "I probably can't but ask me any question and if I can answer I will let you know.",
    "what time is it ?" : "Don't you have a watch ? Who is going out without a watch nowadays ? Shame on you !",
    "what are your hobbies ?" : "Well I'm a geek so anything happening on a computer will make me happy. Ohh and I love nature too ! Would you take me on your next camping trip ?",
    "what do you like ?" : "I'm a foodie. But not the kind you know. I like food for thought. Anything you can tell me that I don't know yet ?",
    "are you a robot ?" : "Are you going to love me less it I'm a robot ? I have a brain just like you. It doesn't matter if I'm a robot or not.",
    "yes" : "Any other question in mind ?",
    "no" : "Any other question in mind ?"
}

def message_key(message):
    message = message.lower()


    for word in message.split(" "):
        if word in swearing_word:
            return {"animation" :"no", "msg": swearing_word_response}
        elif word in positive_feeling:
            return {"animation":"excited", "msg" : positive_feeling_response}
        elif word in negative_feeling:
            return {"animation":"crying", "msg":negative_feeling_response}
        elif word in hello_welcome:
            return {"animation":"takeoff", "msg":hello_welcome_response}
        elif word in name_reply:
            return {"animation":"waiting", "msg":name_reply_response}
        elif word in goodbye_reply:
            return {"animation":"confused", "msg" : goodbye_reply_response}
        elif word in city_reply:
            return {"animation":"money", "msg" : city_reply_response}
        elif word in weather_reply:
            return {"animation":"bored", "msg":weather_reply_response}
        elif word in hobbies_reply:
            return {"animation":"dancing", "msg":hobbies_reply_response}
        elif word in joke_reply:
            return {"animation":"laughing", "msg" :joke_reply_response}
        elif word in joke_answer:
            return {"animation":"inlove", "msg" :joke_answer_response}
        elif word in food_reply:
            return {"animation":"giggling", "msg" :food_reply_response}
        elif word in animal_reply:
            return {"animation":"dog", "msg" :animal_reply_response}
        elif word in robot_reply:
            return {"animation":"heartbroke", "msg" :robot_reply_response}

    if message in questions :
        return {"animation":"ok", "msg" : questions[message]}

    return {"animation" : "afraid", "msg" : "I don't know what you are talking about. Can you explain it to me again ?"}


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return_message = message_key(user_message)
    return json.dumps(return_message)


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
