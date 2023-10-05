import traceback
from datetime import datetime


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, salary_per_day, email):
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = email
        self.save_email()

    def work(self):
        return 'I come at the office'

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

    def check_salary(self, days):
        current_datetime = datetime.now()
        day = current_datetime.day
        weeks = 0
        while day > 0:
            if day < 7:
                break
            day -= 7
            weeks += 1
        days_without_weekends = weeks * 5
        result = day * self.salary_per_day + days_without_weekends * self.salary_per_day

        return f'Amount of money {self.salary_per_day * days} for {days} days' \
               f', and {result} already earned for today {current_datetime.date()}'

    def save_email(self):
        with open('emails.csv', 'a+') as f:
            if not self.validate():
                pass
            else:
                f.write(self.email + '\n')

    def validate(self):
        current_date = datetime.now()

        try:
            with open('emails.csv', 'r') as f:
                if self.email in f.read():
                    raise EmailAlreadyExistsException
        except EmailAlreadyExistsException:
            print('Email already exists!')
            with open('logs.txt', 'a+') as logs:
                logs.write('%' + str(current_date.date()) + '% '
                           + '%' + str(current_date.time()) + '% | %'
                           + traceback.format_exc() + '%' + '\n')
            return False
        return True


class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start to hiring'

    def __str__(self):
        return f'Recruiter name:{self.name}'


class Developer(Employee):
    def __init__(self, tech_stack, name, salary_per_day, email):
        super().__init__(name, salary_per_day, email)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f'Developer name:{self.name}'

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other):
        biggest_salary = [self.salary_per_day, other.salary_per_day]
        for i in other.tech_stack:
            if i not in self.tech_stack:
                self.tech_stack.append(i)

        return Developer(self.tech_stack, self.name + other.name, max(biggest_salary), self.email + other.email)


recruiter = Recruiter('Max', 700, 'abc@mail')
print(recruiter.work())
print(recruiter)

developer_1 = Developer(['JavaScript', 'Django'], 'Ivan', 1000, 'zxc@mail')
print(developer_1)
print(developer_1 > recruiter)
print(developer_1.check_salary(22))

developer_2 = Developer(['JavaScript', 'Django', 'Linux'], 'Vasya', 1200, 'skrpow@mail')
print(developer_2)
print(developer_2 > developer_1)
print(developer_2.check_salary(22))

developer_3 = developer_2 + developer_1
print(developer_3.salary_per_day)
print(developer_3.name)
print(developer_3.tech_stack)
print(developer_3.check_salary(12))
