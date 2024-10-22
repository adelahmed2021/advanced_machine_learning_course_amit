import random
import os

class chatbot:
    __responses = {
        "hello": ["Hello!", "Hi there!", "Greetings!"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
        "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
        "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
    }

    def __get_response(cls, user_input):
        for key in cls.__responses:
            if key in user_input:
                return random.choice(cls.__responses[key])
        return random.choice(cls.__responses["default"])

    def chatbot_generate(self):
        print("Chatbot: Hi! How can I assist you today?")
        while True:
            user_input = input("User: ").lower()
            if user_input == "goodbye":
                break
            response = self.__get_response(user_input)
            print("Chatbot:", response)


if __name__ == "__main__":
    c = chatbot()
    c.chatbot_generate()
