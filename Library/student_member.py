from member import Member
import random

class StudentMember(Member):
    max_books = 5
    __student_id = 1
    def __init__(self,name,course,sem,borrowed_items = None):
        super().__init__(name,borrowed_items)
        self._student_id = StudentMember.__student_id
        StudentMember.__student_id+=1
        self.__course = course
        self.__sem = sem


    def get_student_id(self):
        return self._student_id

    def get_course(self):
        return self.__course

    def get_sem(self):
        return self.__sem

    @staticmethod
    def generate_random_code():
        return random.randrange(10,20)



s1 = StudentMember('Kamlesh','EC','5th')
print(s1.get_student_id(),s1.name,s1.get_course(),s1.get_sem())
print('static method usecase :',s1.generate_random_code())
