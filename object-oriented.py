# 學生系統

class Student:
	def __init__(self,name,age,grades=None):
		self.name = name
		self.age = age
		self.grades = grades if grades else {}

	def average_grade(self):		
		if not self.grades:	# 如果分母(資料數量s)為0則return 0
			return 0
		return sum(self.grades.values())/len(self.grades)
		
class Classroom:
	def __init__(self,class_name,student_list=None):
		self.class_name = class_name
		self.student_list = student_list if student_list else []
		
	def add_student(self,student):
		self.student_list.append(student)
	# 因為這個方法只是將student加入classroom這個物件的student_list屬性裡所以不需要return
			
	def class_average(self):
		if not self.student_list:
			return 0
		# 判斷student_list是否為空 空的就代表沒意義所以return 0
		return sum(student.average_grade() for student in self.student_list)/ len(self.student_list)  # 計算全班的平均成績