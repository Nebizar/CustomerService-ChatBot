# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:13:01 2019

@author: Krzysztof Pasiewicz
"""

from nlu import NLU
import warnings
import json

def convertResponse(response):
    response_dict = json.loads(response)
    return response_dict["respond"]
    

"""
# Main loop of chatbot - do while intent is not 'goodbye'
"""
def main():
    warnings.filterwarnings("ignore")
    rasa_nlu = NLU()
    rasa_nlu.training()
    while True:
        message = input("User: ")
        #print('User: {}'.format(message))
        response = rasa_nlu.get_response(message)
        response = convertResponse(response)
        print('Chatbot: {}'.format(response))
        if rasa_nlu.parse_msg(message)['intent']['name'] == 'goodbye':
            break
        
if __name__ == "__main__":
    main()