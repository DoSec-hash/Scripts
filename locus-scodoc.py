# coding: utf-8
import locust.events
import time
import atexit
import requests
import json
import os
import graphyte
from locust import HttpLocust, TaskSet, task, events, web
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import html
from socket import *


class UserBehavior(TaskSet):


   def on_start(self):
        self.login_url = "https://localhost:1443"
        self.client.verify = False
        self.payload = {
        '__ac_name' : "pouchou",
        '__ac_password' : 'iutbrt',
        'destination' : '.',
        }
        
        self.dem()


   @task(1)
   def dem(self):
        # GET login page to get csrftoken from it
        #response = self.client.get('/fr/users/sign_in')
        response = self.client.get('/ScoDoc')

   @task(2)
   def login(self):
        response=self.client.post('/ScoDoc/doLogin',
                         self.payload)

   @task(3)
   def get_etudiants(self):
       self.client.verify = False
       response=self.client.post('/ScoDoc/RLicPro/Scolarite/Notes/formsemestre_recapcomplet?formsemestre_id=SEM131',self.payload)
       #print("Create; Response status code:", response.status_code)
       #print("Create; Response content:", response.content)


class MyLocust(HttpLocust):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    task_set = UserBehavior
    host = "https://localhost:1443"
    sock = None

    def __init__(self):

        super(MyLocust, self).__init__()
        #self.sock=socket()
        #self.sock.connect( ("localhost", 2003) )
        graphyte.init('localhost',interval=60)
        
        locust.events.request_success += self.hook_request_success
        locust.events.request_failure += self.hook_request_fail
        self.request_fail_stats= list()

        atexit.register(self.exit_handler)


    def hook_request_success(self, request_type, name, response_time, response_length):
        #print(50*'#')
        #print(message,response_length,response_time,time.time())
        #print(50*'#')
        name = name.split('?')[0].replace('/', '-')[1:]
        #print(name)
        graphyte.send(name,response_time,  time.time())

    def hook_request_fail(self, request_type, name, response_time, exception):
        self.request_fail_stats.append([name, request_type, response_time, exception])
        print(self.request_fail_stats[-1])
        #print(self.request_fail_stats)

    def exit_handler(self):
        pass
        #self.sock.shutdown(socket.SHUT_RDWR)
        #self.sock.close()
