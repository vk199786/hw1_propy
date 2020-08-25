from Application.Salary import calculate_salary
from Application.db.People import get_employees
import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.date.today())
