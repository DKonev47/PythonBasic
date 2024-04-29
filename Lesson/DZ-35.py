class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} '


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        """

        :rtype: object
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.last_name} {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise UserException('Больше 10 студентов!!!')

    def delete_student(self, last_name):
        if self.find_student(last_name):
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f'{i.gender}, {i.age}, {i.first_name}, {i.last_name}, {i.record_book}\n'

        return f'Number:{self.number}\n{all_students} '


class UserException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


user_list = []
for i in range(10):
    user_list.append((Student("Female", i + 1, 'Steve', 'Jobs', 'AN142')))

for i in user_list:
    try:
        gr.add_student(i)
    except UserException as e:
        print(e.get_exception_message())