import allure
import pytest
import requests
from API import Company, Employee
from DB import DB

db_connect = ("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
URL = "https://x-clients-be.onrender.com"
@pytest.fixture()
def get_token(username= 'raphael', password= 'cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token

@allure.title("Заполнить форму")
@allure.description("Формирование компании")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_create_employee(get_token):
    company = Company(URL)
    body = {
  "name": "ООО Ромашка",
  "description": "Выращивание и продажа цветов"
}
    with allure.step("Проверить запрос"):
        id = company.create_company(str(get_token), body)
        assert id is not None
        db = DB(db_connect)
        result = db.sql_add_new_employee("Vladimir", "Vasiliev", "+79105551133", "qwerty@yandex.ru", id, True)
        employee = Employee(URL)
        employee_id = employee.get_employees(id)[0]
        assert employee_id['firstName'] == 'Vladimir'
        db = DB(db_connect)
        db.sql_delete_employee(employee_id["id"])

@allure.title("Заполнить форму")
@allure.description("Подготовка данных сотрудника")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_change_employer_info(get_token):
    company = Company(URL)
    body = {
        "name": "ООО Ромашка",
        "description": "Выращивание и продажа цветов"
    }
    with allure.step("Заполнение данных"):
        id = company.create_company(str(get_token), body)
    with allure.step("Проверить результат"):
        assert id is not None
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true',
    }
    employer = Employee(URL)
    just_employer = employer.add_new(str(get_token), body_employer)
    id = just_employer['id']
    with allure.step("Заполнение данных"):
        body_change_employer = {
        'lastName': 'Ivanov',
        'email': 'test1@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true',
    }
    employer_changed = employer.change_employee_info(str(get_token), id, body_change_employer)
    assert employer_changed.status_code == 200

    """Проверка что ID соответствует ID при создании сотрудника"""
    assert id == employer_changed.json()["id"]
    """Проверка изменения почты"""
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")
    db = DB(db_connect)
    db.sql_delete_employee(id)

@allure.title("Выгрузка списка сотрудниуов")
@allure.description("Детализированая проверка")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_get_employer(get_token):
        db = DB(db_connect)
        id = db.sql_last_company_id()

        with allure.step("Проверить результат"):
            assert id is not None
        """Список работников компании"""
        employer = Employee(URL)
        list_employers = employer.get_employees(id)
        """Проверка наличия списка"""
        assert isinstance(list_employers, list)