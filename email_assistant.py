#!/usr/bin/env python3

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import json
from time import sleep

import speech_recognition as sr

recognizer= sr.Recognizer()

def recog():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            spokenInpt = recognizer.recognize_google(audio, language='en-Us')

        return spokenInpt

    except BaseException as err:
        print(f'an error occurred:\n{err}')


class email_assistantClass():
    def __init__(self):
        #from-adress informations
        self.email= ''
        self.pw= ''

        #email-text, subject, to-adress
        self.text= ''
        self.subject= ''
        self.to= None

        #contacts
        self.contacts= dict()

        #smtp
        self.host= ''
        self.port= 0

        #other settings
        self.encoding= ''
        self.subtype= ''

        #to check if the instance variables are already properly initialized with init_settings
        self.init_settingsB= False

    def init_settings(self):
        #open data.json, the settings file
        try:
            with open(r'C:\Users\johan\Documents\CODING_CODING_CODING\Python\PYTHON_Assistence\data.json', 'r') as settingsFile:
                #load data.json
                data= json.load(settingsFile)

                try:
                    #initialising the instance variables
                    self.email= data['email']['loginData']['fromEmail']
                    self.pw= data['email']['loginData']['password']

                    self.contacts= data['email']['contacts']

                    self.host= data['email']['smtp']['host']
                    self.port= data['email']['smtp']['port']

                    self.encoding= data['email']['settings']['encoding']
                    self.subtype= data['email']['settings']['subtype']

                    self.init_settingsB= True


                except BaseException as err:
                    print(f'an error occurred: {err}\nthere is a problem in data.json, u probably made some unlucky changes there')

        except BaseException as err:
            print(f'an error occurred: {err}\ncheck if data.json is in the same directory as the .py files')

    def showMail(self):
        if self.init_settingsB:
            print(f'from: {self.email} \nto: {self.to} \nsubject: {self.subject} \nmessage: {self.text}')
        else:
            print('init_settings not done before')

    def sendmail(self):
        if self.init_settingsB:
            try:
                #create email
                mail = MIMEText(self.text, self.subtype, self.encoding)
                mail['Subject'] = Header(self.subject, self.encoding)
                mail['From'] = self.email
                mail['To'] = self.to

                #login and sending email
                smtp = smtplib.SMTP(self.host, self.port)
                smtp.starttls()
                smtp.login(self.email, self.pw)
                smtp.sendmail(self.email, self.to, mail.as_string())
                smtp.quit()

            except Exception as err:
                print(f'an error occurred: {err}')

        else:
            print('init_settings not done before')

    def mailing(self):
        print('do  want to send an email to somebody? yes/no')
        inpt= recog()
        if 'yes' in inpt or 'yeah' in inpt or 'of course' in inpt:
            print('who do you want to write an email to?')
            person= recog().lower()
            print(person)
            for key in self.contacts.keys():
                print(key)
                if person in key:
                    self.to= self.contacts[key]
                    print(self.to)


            print(f'do you want to write an email to {self.to}? yes/no')
            inpt1= recog()
            if 'yes' in inpt1 or 'yeah' in inpt1 or 'of course' in inpt1:
                print('subject?')
                self.subject= recog()
                print(f'subject: {self.subject}')
                print('message?')
                self.text= recog()
                print(f'message: {self.text}')
                print('ok?')
                ok= recog()
                if 'show' in ok:
                    email_assistantClass.showMail(self)
                print('send?')
                ok1= recog()
                if 'yes' in ok1 or 'yeah' in ok1 or 'of course' in ok1:
                    email_assistantClass.sendmail(self)

                else:
                    print(f"you don't want to send {self.to} an email")



            else:
                print(f"you don't want to send {self.to} an email")

        else:
            print('ok')







