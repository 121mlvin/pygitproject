class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        return 'I come at the office'

    def __ge__(self, other):
        return self.salary_per_day >= other.salary_per_day


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring'

    def __str__(self):
        return f'Recruiter name:{self.name}'


class Developer(Employee):
    def work(self):
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f'Employee name:{self.name}'


recruiter = Recruiter('Max', 900)
print(recruiter)

developer = Developer('Ivan', 1000)
print(developer)
print(developer >= recruiter)