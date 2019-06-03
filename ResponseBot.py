# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:03:20 2019

@author: apasi
"""
import random
import json
import os

class ResponseBot():
    
    #TODO
    # basic responses - probably better way to do it
    def __init__(self):
        self.dir = "data/responses"
        self.file = "responses.json"
        self.path = os.path.join(self.dir, self.file)
        f = open(self.path)
        self.responses_dict = json.load(f)
        f.close()
    
    # return response as json file for every intent and if not recognized option
    def greet_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["GREET"])
        result_json = json.dumps(respond)
        return result_json
    
    def goodbye_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["GOODBYE"])
        result_json = json.dumps(respond)
        return result_json
    
    def howAreYou_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["HOW_ARE_YOU"])
        result_json = json.dumps(respond)
        return result_json
    
    def myNameIs_message(self, name):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["MY_NAME_IS"]).format(name)
        result_json = json.dumps(respond)
        return result_json
    
    def unknown_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["UNKNOWN"])
        result_json = json.dumps(respond)
        return result_json
    
    def issue_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["ISSUE"])
        result_json = json.dumps(respond)
        return result_json
    
    def gratitude_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["GRATITUDE"])
        result_json = json.dumps(respond)
        return result_json
    
    def no_problem(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["NO_PROBLEM"])
        result_json = json.dumps(respond)
        return result_json

    def askForHelp_message(self):
        respond={}
        respond['respond']=random.choice(self.responses_dict["ASK_FOR_HELP"])
        result_json = json.dumps(respond)
        return result_json
    
    def initial_issue_message(self):
        respond = {}
        #respond['respond'] = "I can contact you with our specific helpdesk"
        respond['respond'] = "I can contact you with our specific helpdesk"
        result_json = json.dumps(respond)
        return result_json
    # TODO
    # here return contact to specific helpdesk department depending on found entities
    def get_helpdesk(self, equipment):
        respond = {}
        if len(equipment)>0:
            respond['respond'] = random.choice(self.responses_dict["GET_HELPDESK"]).format(equipment[0]['value'], "DO NUMBER TODO")
        else:
            respond['respond'] = "To contact our general helpdesk call: 666-666-666"
        result_json = json.dumps(respond)
        return result_json

    def helpdesk_message(self):
        respond = {}
        respond['respond'] = "I can contact you with our specific helpdesk"
        result_json = json.dumps(respond)
        return result_json
        
    def get_help(self):
        respond = {}
        respond['respond'] = "Maybe I can help you"
        result_json = json.dumps(respond)
        return result_json
    
    def incompleteOrder_message(self):
        respond = {}
        respond['respond'] = random.choice(self.responses_dict["INCOMPLETE_ORDER"])
        result_json = json.dumps(respond)
        return result_json