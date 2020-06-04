import random
import resource
from locust import HttpUser, task, between
resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    def on_start(self):
        self.login_url="https://192.168.1.114:443"
        self.client.verify = False
        self.payload = {
          '__ac_name' : "pouchou",
          '__ac_password' : 'iutbrt',
          'destination' : '.',
        }
        self.dem()


    @task(1)
    def dem(self):
      response = self.client.get('/ScoDoc')

    @task(2)
    def login(self):
        response=self.client.post('/ScoDoc/doLogin',
        self.payload)

    @task(3)
    def get_etudiants(self):
        self.client.verify = False
        response=self.client.post('/ScoDoc/ScoDoc/RT/Scolarite/Notes/formsemestre_status?formsemestre_id=SEM140',self.payload)
