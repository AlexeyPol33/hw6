from functools import reduce


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
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

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def midle_rate (self):
        onelist_rate = reduce(lambda x,y: x + y, list(self.grades.values()))
        sum_rate = reduce(lambda x,y: x + y, onelist_rate)
        return round(sum_rate / len(onelist_rate),1)

    def __str__(self) -> str:


        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + f'Средняя оценка за лекции: {self.midle_rate()}' 


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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','GIT']
best_student.finished_courses += ['Введение в программирование']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('sam', 'SN')
cool_lecturer.courses_attached += ['Python']

cool_revier = Reviewer('Some', 'Buddy')
cool_revier.courses_attached += ['Python']

cool_revier.rate_hw(best_student, 'Python', 7)
cool_revier.rate_hw(best_student, 'Python', 3)
cool_revier.rate_hw(best_student, 'Python', 1)

best_student.rate_lecturer (cool_lecturer, 'Python', 10)
best_student.rate_lecturer (cool_lecturer, 'Python', 10)
best_student.rate_lecturer (cool_lecturer, 'Python', 10)
 
print(best_student.grades)
print()
print(cool_lecturer.grades)
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