import psycopg2

from sqlalchemy import create_engine, text
db_connect = ("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
class DB:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def sql_last_company_id(self):
        self.db = create_engine(db_connect)
        with self.db.connect() as connection:
            result = connection.execute(
            text("select id from company order by id desc limit 1")
            )
            return result.fetchall()

    def sql_add_new_employee(self, first_name, last_name, phone, email, company_id, is_active):
        employee_data = {
            "first_name": first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'company_id': company_id,
            'is_active': is_active
        }
        with self.db.connect() as connection:
            rows = connection.execute(
                text(
                    "insert into employee (first_name, last_name, phone, email, company_id, is_active) values (:first_name, :last_name, :phone, :email, :company_id, :is_active)"),
                employee_data)
            return rows

    def sql_delete_employee(self, id):
        with self.db.connect() as connection:
            result = connection.execute(
                text("delete from employee where id =:id"), {"id": id})