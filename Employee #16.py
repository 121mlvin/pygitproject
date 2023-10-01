from datetime import datetime


class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

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


class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start to hiring'

    def __str__(self):
        return f'Recruiter name:{self.name}'


class Developer(Employee):
    def __init__(self, tech_stack, name, salary_per_day):
        super().__init__(name, salary_per_day)
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
        name = self.name + other.name
        for i in other.tech_stack:
            if i not in self.tech_stack:
                self.tech_stack.append(i)
        if super().__gt__(other):
            return name, self.tech_stack, self.salary_per_day
        return name, self.tech_stack, other.salary_per_day


recruiter = Recruiter('Max', 700)
print(recruiter.work())
print(recruiter)

developer1 = Developer(['JavaScript', 'Django'], 'Ivan', 1000)
print(developer1)
print(developer1 > recruiter)
print(developer1.check_salary(22))

developer2 = Developer(['JavaScript', 'Django', 'Linux'], 'Vasya', 1200)
print(developer2)
print(developer2 > developer1)
print(developer2.check_salary(22))
print(developer2.__add__(developer1))
