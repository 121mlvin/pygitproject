from unittest import TestCase
import employee_18


class TestEmployee(TestCase):

    def setUp(self):
        self.employee1 = employee_18.Employee(email='abd@mail', name='Sarah', salary_per_day=500)
        self.employee2 = employee_18.Employee(email='bbbb@mail', name='Phill', salary_per_day=400)

    def test_work(self):
        self.assertEqual(self.employee1.work(), 'I come at the office')

    def test_check_salary(self):
        self.assertEqual(self.employee1.check_salary(10), f'Amount of money 5000 for 10 days, and 4000 already earned '
                                                          f'for today 2023-10-10')

    def test_magic_gt(self):
        self.assertTrue(self.employee1 > self.employee2)

    def test_magic_eq(self):
        self.assertFalse(self.employee1 == self.employee2)


class TestRecruiter(TestCase):

    def setUp(self):
        self.recruiter = employee_18.Recruiter('Joker', 450, 'hahah@mail')

    def test_work(self):
        self.assertEqual(self.recruiter.work(), 'I come to the office and start to hiring')

    def test_magical_str(self):
        self.assertEqual(str(self.recruiter), 'Recruiter name:Joker')


class TestDeveloper(TestCase):

    def setUp(self):
        self.developer1 = employee_18.Developer(tech_stack=['JavaScript', 'Django'], name='Ivan',
                                                salary_per_day=1000, email='zxc@mail')
        self.developer2 = employee_18.Developer(tech_stack=['JavaScript', 'Django', 'Linux'], name='Vasya',
                                                salary_per_day=1200, email='skrpow@mail')

    def test_work(self):
        self.assertEqual(self.developer1.work(), 'I come to the office and start to coding.')

    def test_add(self):
        self.developer3 = self.developer1 + self.developer2
        self.assertEqual((self.developer3.tech_stack, self.developer3.name,
                          self.developer3.salary_per_day, self.developer3.email),
                         (['JavaScript', 'Django', 'Linux'], 'IvanVasya',
                          1200, 'zxc@mailskrpow@mail'))
        self.assertIsInstance(self.developer3, employee_18.Developer)

    def test_magical_str(self):
        self.assertEqual(str(self.developer1), 'Developer name:Ivan')

    def test_magical_lt(self):
        self.assertTrue(self.developer1.salary_per_day < self.developer2.salary_per_day)

    def test_magical_eq(self):
        self.assertFalse(self.developer1.salary_per_day == self.developer2.salary_per_day)


class TestCandidate(TestCase):

    def setUp(self):
        self.candidate1 = employee_18.Candidate('Masha', 'Abc', 'ma@mail', ['JavaScript'], 'JavaScript', 'Junior')
        self.candidate2 = employee_18.Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw'
                                                                    '/4f59074e6fbb552398f87636b5bf089a1618da0a'
                                                                    '/candidates.csv')

    def test_full_name(self):
        self.assertTrue(self.candidate1.full_name, 'Masha Abc')

    def test_generate_candidates(self):
        self.assertEqual(self.candidate2[0], 'Ivan')


