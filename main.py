import application.db.people
import application.salary
import datetime
import requests

if __name__ == '__main__':
    print(f'Текущая дата {datetime.datetime.now().date()}')
    a = requests.get('https://api.ipify.org').text
    print(f'Текущий IP адрес: {a}')
    application.salary.calculate_salary()
    application.db.people.get_employees()
