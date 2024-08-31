import requests


class Company:
    def __init__(self, url):
        self.url = url
    def create_company(self, token, body):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/company', headers=headers, json=body)
        return response.json()["id"]
class Employee:
    def __init__(self, url):
        self.url = url

    def get_employees(self, company_id):
        company = {'company': company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    def add_new(self, token, body):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/employee', headers=headers, json=body)
        return response.json()

    def get_employee_info(self, employee_id):
        response = requests.get(self.url + '/employee/' + str(employee_id))
        return response.json()

    def change_employee_info(self, token: str, employee_id, body):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + '/employee/' + str(employee_id), headers=headers, json=body)
        return response