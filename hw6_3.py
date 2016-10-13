# i2p - Homework - 6; Challenging Version
# By: Roopa Prakash, submitted on: 06/08/2016

# Part 4
class Course(object):
	def __init__(self, name, max_students, students_list, room, schedule):
		self.name = name
		self.max_students = max_students
		self.students_list = students_list
		self.room = room
		self.schedule = schedule
		
		
	def AddStudent(self, student_ldap):
		if student_ldap not in self.students_list and len(self.students_list) < self.max_students:
			self.students_list.append(student_ldap)
			print 'Student: ' + student_ldap + ' is added to course ' + self.name
		else:
			print 'Adding Student: ' + student_ldap + ' to course ' + self.name + ' failed.'
		
	def DropStudent(self, student_ldap):
		if student_ldap in self.students_list:
			self.students_list.remove(student_ldap)
			print 'Student: ' + student_ldap + ' is dropped from course ' + self.name
		else:
			print 'Student: ' + student_ldap + ' not in Student List in course ' + self.name
	
	def Reschedule(self, new_schedule):
		new_schedule = new_schedule.strip()
		if(new_schedule):
			self.schedule = new_schedule
			print 'Rescheduled course: ' + self.name + ' to ' + self.schedule
		else:
			print 'Please set a valid schedule'
			
	def ChangeRoom(self, new_room):
		new_room = new_room.strip()
		if(new_room):
			self.room = new_room
			print 'Room for course: ' + self.name + ' changed to ' + self.room
		else:
			print 'Please set a valid Room'
		
	def GetNumberOfParticipants(self):
		return len(self.students_list)
		
		
class Intro2Programming(Course):
	def NagStudents(self):
		print 'Do your Homework! Start Early!'
	
	def CheckHomeWork(self):
		for student in self.students_list:
			print student + ', did you do your homework?!'
	

# Create object of Class Course
my_course = Course('Python Beginner', 3, ['a', 'b'], 'yoda', 'Friday 9 - 10')

print 'Parent Class -- Course ..'
# Calling AddStudent with existing student, new student and after max_students is reached
print 'AddStudent ..'
my_course.AddStudent('b')
my_course.AddStudent('c')
my_course.AddStudent('d')

print 'Student List after Adding'  + str(my_course.students_list)
print ''

# Calling DropStudent with existing student, not existing student
print 'DropStudent ..'
my_course.DropStudent('a')
my_course.DropStudent('e')

print 'Student List after Drop Student'  + str(my_course.students_list)
print ''

print 'Reschedule, ChangeRoom, GetNumberOfParticipants ..'
# Calling Reschedule - validates empty string and removes extra spaces
my_course.Reschedule('   Thursday 9 - 10   ')

# Calling ChangeRoom - validates empty string and removes extra spaces
my_course.ChangeRoom('   Frizzle  ')

# Calling GetNumberOfParticipants
print 'Number of students signed up to course ' + my_course.name + ' is ' + str(my_course.GetNumberOfParticipants())
print ''

print 'Child Class -- Intro2Programming ..'
# Create object of Class Course
my_course_new = Intro2Programming('i2p', 3, ['S1', 'S2'], 'Video Call', 'Friday 9 - 10')

# Calling AddStudent with existing student, new student and after max_students is reached
print 'AddStudent ..'
my_course_new.AddStudent('S1')
my_course_new.AddStudent('S3')
my_course_new.AddStudent('S4')

print 'Student List after Adding'  + str(my_course_new.students_list)
print ''

# Calling DropStudent with existing student, not existing student
print 'DropStudent ..'
my_course_new.DropStudent('S3')
my_course_new.DropStudent('S4')

print 'Student List after Drop Student'  + str(my_course_new.students_list)
print ''

print 'Reschedule, ChangeRoom, GetNumberOfParticipants ..'
# Calling Reschedule - validates empty string and removes extra spaces
my_course_new.Reschedule('   Thursday 9 - 10   ')

# Calling ChangeRoom - validates empty string and removes extra spaces
my_course_new.ChangeRoom('   Google Hangout  ')

# Calling GetNumberOfParticipants
print 'Number of students signed up to course ' + my_course_new.name + ' is ' + str(my_course_new.GetNumberOfParticipants())

# Calling NagStudents
my_course_new.NagStudents()

#Calling CheckHomeWork
my_course_new.CheckHomeWork()