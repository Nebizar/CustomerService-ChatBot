# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:13:01 2019

@author: Krzysztof Pasiewicz
"""

from nlu import NLU

"""
# Main loop of chatbot - do while intent is not 'goodbye'
"""
def main():
    rasa_nlu = NLU()
    rasa_nlu.training()
    while True:
        message = input("User: ")
        print('User: {}'.format(message))
        respond = rasa_nlu.get_response(message)
        print('Chatbot: {}'.format(respond))
        if rasa_nlu.parse_msg(message)['intent']['name'] == 'goodbye':
            break
        
if __name__ == "__main__":
    main()