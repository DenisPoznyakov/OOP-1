class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        res = (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за домашние задания: {average_grade(self)} \n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
               f'Завершенные курсы: {", ".join(self.finished_courses)} ')
        return res

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student")
            return
        return average_grade(self) < average_grade(other)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def __str__(self):
        res = f'Имя:  {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_grade(self)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer")
            return
        return average_grade(self) < average_grade(other)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:  {self.name} \nФамилия: {self.surname}'
        return res

def average_grade(someone):
    total_grades = 0
    count = 0
    for value in someone.grades.values():
        total_grades += sum(value)
        count += len(value)
    average = total_grades / count
    return average

def average_rating_stud(st_list, course):
    lec_course = []
    total_grades = 0
    count_grades = 0
    for st in st_list:
        if course in st.courses_in_progress:
            lec_course.append(st)
    for obj in lec_course:
        for grade in obj.grades.values():
            total = sum(grade)
            total_grades += total
            count_grades += len(grade)
    student_average = total_grades / count_grades
    return student_average

def average_rating_lect(lec_list, course):
    lec_course = []
    total_grades = 0
    count_grades = 0
    for lec in lec_list:
        if course in lec.courses_attached:
            lec_course.append(lec)
    for obj in lec_course:
        for grade in obj.grades.values():
            total = sum(grade)
            total_grades += total
            count_grades += len(grade)
    lecturer_average = total_grades / count_grades
    return lecturer_average

st_list = []
lec_list = []

student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.finished_courses += ['Data Scientist']
student_1.courses_in_progress += ['Python', 'Git']
st_list.append(student_1)

student_2 = Student('Lisa', 'Lisova', 'female')
student_2.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Git', 'Аналитика', 'Python']
st_list.append(student_2)

lecturer_1 = Lecturer('Oleg', 'Olegov')
lecturer_1.courses_attached = ('Введение в программирование', 'Python', 'Git')
lec_list.append(lecturer_1)

lecturer_2 = Lecturer('Alex', 'Alexov')
lecturer_2.courses_attached = ('Git', 'Аналитика', 'Data Scientist', 'Python')
lec_list.append(lecturer_2)

reviewer_1 = Reviewer('Maria', 'Marina')
reviewer_1.courses_attached += ['Python', 'Git', 'Аналитика']

reviewer_2 = Reviewer('Victor', 'Victorov')
reviewer_2.courses_attached += ['Введение в программирование', 'Data Scientist', 'Java']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)

print(student_1)
print(student_1.grades)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1 < student_2)
print(lecturer_1 < lecturer_2)

print(f'Средняя оценка студентов на курсе Python: {average_rating_stud(st_list, "Python")}')
print(f'Средняя оценка преподавателей на курсе Python: {average_rating_lect(lec_list, "Python")}\n')