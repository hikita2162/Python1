import requests
import json
from Lesson_8.constants import X_client_URL

path = '/employee/'

class Company:
    def __init__(self, url=X_client_URL):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()
    
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        response = requests.get(
            self.url + '/company', params=active_params)
        return response.json()[-1]['id']
    
class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url

    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    def add_new(self, token: str, body: json):
        haeders = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=haeders, json=body)
        return response.json()
    
    def get_info(self, emloyee_id: int):
        response = requests.get(self.url + path + str(emloyee_id))
        return response
    
    def change_info(self, token:str, emloyee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(emloyee_id), headers=headers,
                                  json=body)
        return response
