# 學生系統

class Student:
	def __init__(self,name,age,grades=None):
		self.__name = name
		self.__age = age
		self.__grades = grades if grades else {}


	def set_grade(self,subject,grade):
		self.__grades[subject] = grade

	def get_grade(self):
		return self.__grades

	def average_grade(self):		
		if not self.__grades:	# 如果分母(資料數量s)為0則return 0
			return 0
		return sum(self.__grades.values())/len(self.__grades)
	
	def introduce(self):
		return f"Hi, I'm {self.__name} and I'm {self.__age} years old."
		
class GraduateStudent(Student):
	def __init__(self,name,age,grades = None,thesis_title = ""):
		super().__init__(name,age,grades)
		self.__thesis_title = thesis_title

	def set_thesis_title(self,title):
		self.__thesis_title = title

	def get_thesis_title(self):
		return self.__thesis_title
	
	def introduce(self):
		base_introduction = super().introduce()
		return f"{base_introduction} And I'm working on my thesis titled '{self.__thesis_title}'."

class Classroom:
	def __init__(self,class_name,student_list=None):
		self.__class_name = class_name
		self.__student_list = student_list if student_list else []
		
	def add_student(self,student):
		self.__student_list.append(student)
	# 因為這個方法只是將student加入classroom這個物件的student_list屬性裡所以不需要return
			
	def class_average(self):
		if not self.__student_list:
			return 0
		# 判斷student_list是否為空 空的就代表沒意義所以return 0
		return sum(student.average_grade() for student in self.__student_list)/ len(self.__student_list)  # 計算全班的平均成績
	

def student_introduction(student):
	print(student.introduce())


#test
s = Student("John",20,{"math":85,"english":90})
gs = GraduateStudent("Oscar",22,{"math":100,"english":100},"Quantum Physics")

student_introduction(s)
student_introduction(gs)