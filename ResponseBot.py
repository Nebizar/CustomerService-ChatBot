# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:03:20 2019

@author: apasi
"""
import random
import json

class ResponseBot():
    
    #TODO
    # basic responses - probably better way to do it
    GREET = [
            'hello',
            'hi',
            'Welcome!',
            "What's up ?",
            "Good morning"]
    
    GOODBYE = [
            'See you later!',
            'Goodbye',
            'Bye',
            'Come again']
    
    HOW_ARE_YOU = [
            'Fine, thanks',
            'Very good',
            'Good, you are really nice',
            'Awesome',
            "It's ok"]
    
    MY_NAME_IS = [
            'Nice to meet you {}',
            'Hi, {}, whats up ?',
            'Hi {}, my name is Bot',
            'Hi {}, I am Bot',
            'Hi {}, you can call me Bot',
            ]
    
    UNKNOWN = [
            'Sorry, I do not understand',
            'Try tell me somthin different',
            'I will get some help because I do not understand',
            'Sorry I do not get you. I will do better next time']
    
    # return response as json file for every intent and if not recognized option
    def greet_message(self):
        respond = {}
        respond['respond'] = random.choice(self.GREET)
        result_json = json.dumps(respond)
        return result_json
    
    def goodbye_message(self):
        respond = {}
        respond['respond'] = random.choice(self.GOODBYE)
        result_json = json.dumps(respond)
        return result_json
    
    def howAreYou_message(self):
        respond = {}
        respond['respond'] = random.choice(self.HOW_ARE_YOU)
        result_json = json.dumps(respond)
        return result_json
    
    def myNameIs_message(self, name):
        respond = {}
        respond['respond'] = random.choice(self.MY_NAME_IS).format(name)
        result_json = json.dumps(respond)
        return result_json
    
    def unknown_message(self):
        respond = {}
        respond['respond'] = random.choice(self.UNKNOWN)
        result_json = json.dumps(respond)
        return result_json