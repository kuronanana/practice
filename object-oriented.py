# 學生系統

class student:
	def __init__(self,name,age,grades=None):
		self.name = name
		self.age = age
		if grades:
			self.grades = grades
		else:
			self.grades = None


	def average_grade(self):
		total = sum(self.grades.values())
		s = len(self.grades)
		if s == 0:
			return 0
		return total/s
		
# class classroom:
# 	def __init__(self,class_name,student_list(student)=None):
# 		def add_student()
			

# 		return
		
			
# 		def class_average()
			

# 		return