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
        self.issue_handling = 0
        self.issue_states = {
                '1': self.state_01,
                '2': self.state_02,
                '3': self.state_03,
                '4': self.state_03,
                '5': self.state_05,
                '6': self.state_06
                }
        self.dir = 'data/training'
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
    
    # issue handling state functions
    def state_01(self, parsed_msg):
        if parsed_msg['intent']['name'] == 'affirm' or parsed_msg['intent']['name'] == 'gratitude':
            self.issue_handling = 2
            return self.responser.get_helpdesk(self.equipment)
        if parsed_msg['intent']['name'] == 'deny':
            self.issue_handling = 3
            return self.responser.get_help()
        else:
            return self.responser.unknown_message()
    
    def state_02(self, parsed_msg):
        self.issue_handling = 0
        if parsed_msg['intent']['name'] == 'gratitude':
            return self.responser.no_problem()
        else:
            return self.responser.unknown_message()
        
    def state_03(self, parsed_msg):
        if parsed_msg['intent']['name'] == 'affirm' or parsed_msg['intent']['name'] == 'gratitude':
            self.issue_handling += 1
            return self.responser.helpQuestion_message(self.issue_handling)
        if parsed_msg['intent']['name'] == 'deny':
            if self.issue_handling == 3:
                self.issue_handling = 0
                return self.responser.denied_message()
            else:
                self.issue_handling = 6
                return self.responser.encourage_message()
        else:
            return self.responser.unknown_message()
        
    def state_05(self, parsed_msg):
        if parsed_msg['intent']['name'] == 'affirm' or parsed_msg['intent']['name'] == 'gratitude':
            self.issue_handling = 6
            return self.responser.plug_message()
        if parsed_msg['intent']['name'] == 'deny':
            self.issue_handling = 0
            return self.responser.issue_message()
        else:
            return self.responser.unknown_message()
    
    def state_06(self, parsed_msg):
        self.issue_handling = 0
        if parsed_msg['intent']['name'] == 'affirm' or parsed_msg['intent']['name'] == 'gratitude':
            return self.responser.gratitude_message()
        else:
            return self.responser.unknown_message()
            
    
    # parse incoming message    
    def parse_msg(self, msg):
        return self.interpreter.parse(msg)
        
    # get relevant response basing on input intent
    def get_response(self, message):
        parsed_msg = self.parse_msg(message)
        #print(parsed_msg)
        
        if self.issue_handling != 0:
            return self.issue_states[str(self.issue_handling)](parsed_msg)
        
        if parsed_msg['intent']['name']=='greet':
            return self.responser.greet_message()
        
        if parsed_msg['intent']['name']=='ask_for_help':
            return self.responser.askForHelp_message()
        
        if parsed_msg['intent']['name']=='goodbye':
            return self.responser.goodbye_message()

        if parsed_msg['intent']['name']=='gratitude':
            return self.responser.gratitude_message()
        
        if parsed_msg['intent']['name']=='how_are_you':
            return self.responser.howAreYou_message()
        
        if parsed_msg['intent']['name']=='my_name_is':
            print(parsed_msg)
            if len(parsed_msg['entities']) > 0:
                return self.responser.myNameIs_message(parsed_msg['entities'][0]['value'])
            else:
                return self.responser.myNameIs_message("Stranger")
        
        if parsed_msg['intent']['name'] == 'issue':
            #TODO 
            #issue solving helpers
            self.equipment = parsed_msg['entities']
            self.issue_handling = 1
            return self.responser.initial_issue_message()

        if parsed_msg['intent']['name'] == 'affirm' or parsed_msg['intent']['name'] == 'deny':
            return self.responser.helpdesk_message()
        
        if parsed_msg['intent']['name'] == 'incomplete_order':
            return self.responser.incompleteOrder_message()
        
        if "intent" not in parsed_msg or parsed_msg['intent'] is None:
            return self.responser.unknown_message()
        
        else:
            return self.responser.unknown_message()
        
        