# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:28:17 2019

@author: Krzysztof Pasiewicz
"""
import os
from rasa_nlu.training_data import load_data
#from rasa_nlu.converters import load_rasa_data
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.config import load
from ResponseBot import ResponseBot

class NLU():
    
    # Init - get trainig data from dir, create responser object, train Rasa_NLU on data
    def __init__(self):
        self.dir = 'data'
        self.file = 'testData.json'
        self.data = os.path.join(self.dir, self.file)
        self.responser = ResponseBot()
        self.training()
        
    # simplest rasa_NLU training schema
    def training(self):
        training_data = load_data(self.data)
        config = load("config_spacy.yml")
        trainer = Trainer(config)
        trainer.train(training_data)
        model_directory = trainer.persist("projects")
        self.interpreter = Interpreter.load(model_directory)
        
    # parse incoming message    
    def parse_msg(self, msg):
        return self.interpreter.parse(msg)
        
    # get relevant response basing on input intent
    def get_response(self, message):
        parsed_msg = self.parse_msg(message)
        
        if parsed_msg['intent']['name']=='greet':
            return self.responser.greet_message()
        
        if parsed_msg['intent']['name']=='goodbye':
            return self.responser.goodbye_message()
        
        if parsed_msg['intent']['name']=='how_are_you':
            return self.responser.howAreYou_message()
        
        if parsed_msg['intent']['name']=='my_name_is':
            #print(parsed_msg)
            if len(parsed_msg['entities']) > 0:
                return self.responser.myNameIs_message(parsed_msg['entities'][0]['value'])
            else:
                return self.responser.myNameIs_message("Stranger")
        
        if not "intent" in parsed_msg or parsed_msg['intent'] is None:
            return self.responser.unknown_message()
        
        