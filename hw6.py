from functools import reduce


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.search_by_course = None
        
    
    def rate_lecturer(self, lecturer, course, grade):
        if  0 <= grade <= 10:
            pass
        else:
            return 'Оценка от 0 до 10'

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def midle_rate (self):
        onelist_rate = reduce(lambda x,y: x + y, list(self.grades.values()))
        sum_rate = reduce(lambda x,y: x + y, onelist_rate)
        return round(sum_rate / len(onelist_rate),1)

    def __str__(self) -> str:


        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + f'Средняя оценка за домашние задания: {self.midle_rate ()}' + '\n' + 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n' + 'Завершенные курсы: ' + ', '.join(self.finished_courses)

    def __lt__ (self, other):

        return self.midle_rate() < other.midle_rate()
    
    def __gt__ (self, other):

        return self.midle_rate() > other.midle_rate()
    
    def __add__ (self, other):
        if self.search_by_course == None or  other.search_by_course == None:
            raise IOError ('Курс поиска не назначин, сложение не возможно')
        if self.search_by_course not in self.courses_in_progress or other.search_by_course not in other.courses_in_progress:
            raise IOError ('Курс поиска отсутвует, сложение не возможно')


        return self.grades[self.search_by_course] + other.grades[self.search_by_course]
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.search_by_course = None

    def midle_rate (self):
        onelist_rate = reduce(lambda x,y: x + y, list(self.grades.values()))
        sum_rate = reduce(lambda x,y: x + y, onelist_rate)
        return round(sum_rate / len(onelist_rate),1)

    def __str__(self) -> str:


        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + f'Средняя оценка за лекции: {self.midle_rate()}'
    
    def __add__ (self, other):
        if self.search_by_course == None or  other.search_by_course == None:
            raise IOError ('Курс поиска не назначин, сложение не возможно')
        if self.search_by_course not in self.courses_attached or other.search_by_course not in other.courses_attached:
            raise IOError ('Курс поиска отсутвует, сложение не возможно')

        return self.grades[self.search_by_course] + other.grades[self.search_by_course]


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


def midle_rate (rmidle_rate_objects,key_serch):
    for i in range(len(rmidle_rate_objects)):
        rmidle_rate_objects[i].search_by_course = key_serch
    onelist_rate = reduce(lambda x,y: x + y, rmidle_rate_objects)
    sum_rate = reduce(lambda x,y: x + y, onelist_rate)
    return round(sum_rate / len(onelist_rate),1)
    
if __name__ == '__main__':
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python','GIT']
    best_student.finished_courses += ['Введение в программирование']
    second_student = Student('Ruoy', 'Eman', 'your_gender')
    second_student.courses_in_progress += ['Python','GIT']
    second_student.finished_courses += ['Введение в программирование']
 
    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python','GIT']
    second_mentor = Mentor('Some', 'Buddy')
    second_mentor.courses_attached += ['Python','GIT']

    cool_lecturer = Lecturer('SomeName', 'SomeSecondName')
    cool_lecturer.courses_attached += ['Python','GIT']
    second_lecturer = Lecturer('sam', 'SN')
    second_lecturer.courses_attached += ['Python','GIT']

    cool_revier = Reviewer('Some', 'Buddy')
    cool_revier.courses_attached += ['Python','GIT']
    second_revier = Reviewer('Name', 'SecondName')
    second_revier.courses_attached += ['Python','GIT']

    cool_revier.rate_hw(best_student, 'Python', 2)
    cool_revier.rate_hw(best_student, 'GIT', 1)
    cool_revier.rate_hw(best_student, 'Python', 0)
    cool_revier.rate_hw(best_student, 'GIT', 1)

    cool_revier.rate_hw(second_student, 'GIT', 9)
    cool_revier.rate_hw(second_student, 'Python', 10)
    cool_revier.rate_hw(second_student, 'GIT', 7)
    cool_revier.rate_hw(second_student, 'Python', 3)

    best_student.rate_lecturer (cool_lecturer, 'Python', 9)
    best_student.rate_lecturer (cool_lecturer, 'GIT', 0)
    best_student.rate_lecturer (cool_lecturer, 'Python', 5)
    best_student.rate_lecturer (cool_lecturer, 'GIT', 0)

    best_student.rate_lecturer (second_lecturer, 'Python', 7)
    best_student.rate_lecturer (second_lecturer, 'GIT', 8)
    best_student.rate_lecturer (second_lecturer, 'Python', 1)
    best_student.rate_lecturer (second_lecturer, 'GIT', 8)

    second_student.rate_lecturer (cool_lecturer, 'GIT', 5)
    second_student.rate_lecturer (cool_lecturer, 'GIT', 9)
    second_student.rate_lecturer (cool_lecturer, 'GIT', 6)

    second_student.rate_lecturer (second_lecturer, 'Python', 1)
    second_student.rate_lecturer (second_lecturer, 'Python', 0)
    second_student.rate_lecturer (second_lecturer, 'Python', 10)

    key_serch = 'GIT'

    best_student.search_by_course = key_serch
    second_student.search_by_course = key_serch
    second_lecturer.search_by_course = key_serch
    cool_lecturer.search_by_course = key_serch

    print(cool_lecturer + second_lecturer)
    print()
    print(best_student + second_student)
    print()
    print (f'Средняя оценка студентов за домашние задания по курсу {key_serch}: ' + str (midle_rate([best_student, second_student], key_serch)))
    print()
    print (f'Средняя оценка лекторов за лекции по курсу {key_serch}: ' + str (midle_rate([second_lecturer, cool_lecturer], key_serch)))
    print()
    print (cool_revier)
    print()
    print(cool_lecturer)
    print()
    print(best_student)
    print()
    print(best_student < cool_lecturer)
    print()
    print(best_student > cool_lecturer)
