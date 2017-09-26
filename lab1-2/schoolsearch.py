# Dane Mortensen and Kartik Mendiratta

import re
import sys

class Student:
   def __init__(self, last_name, first_name, grade, classroom, bus, gpa):
      self.last_name = last_name
      self.first_name = first_name
      self.grade = grade
      self.classroom = classroom
      self.bus = bus
      self.gpa = gpa

class Teacher:
   def __init__(self, last_name, first_name, classroom):
      self.last_name = last_name
      self.first_name = first_name
      self.classroom = classroom

# assumes there are no duplicates in file
def record_students(students):
   try:
      with open("list.txt") as f:
         for line in f:
            info = re.split(", |,", line.strip())
            students.append(Student(info[0], info[1], int(info[2]), int(info[3]),\
                  int(info[4]), float(info[5])))
   except:
      sys.exit()

def record_teachers(teachers):
   try:
      with open("teachers.txt") as f:
         for line in f:
            info = re.split(", |,", line.strip())
            print info
            teachers.append(Teacher(info[0], info[1], int(info[2])))
   except:
      sys.exit()

def classroom_to_teacher(teachers, classroom):
   for teacher in teachers:
      if teacher.classroom == classroom:
         return teacher

def student_search(students, teachers, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: grade = {2}, ".format(student.last_name,\
               student.first_name, student.grade),
         teacher = classroom_to_teacher(teachers, student.classroom)
         print "classroom = {0}, teacher = {1}, {2}".format(teacher.classroom,\
               teacher.last_name, teacher.first_name)

def student_bus_search(students, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: bus route = {2}".format(student.last_name,\
               student.first_name, student.bus)

def classroom_search(students, classroom):
   for student in students:
      if student.classroom == classroom:
         print "{0}, {1}".format(student.last_name, student.first_name)

def classroom_teacher_search(teachers, classroom):
   for teacher in teachers:
      if teacher.classroom == classroom:
         print "{0}, {1}".format(teacher.last_name, teacher.first_name)

def grade_teacher_search(students, teachers, grade):
   classrooms = []

   for student in students:
      if student.grade == grade and student.classroom not in classrooms:
         classrooms.append(student.classroom)

   for teacher in teachers:
      if teacher.classroom in classrooms:
         print "{0}, {1}".format(teacher.last_name, teacher.first_name)

def enrollment(students):
   classrooms = []

   for student in students:
      if student.classroom not in classrooms:
         classrooms.append(student.classroom)

   classrooms.sort()

   for classroom in classrooms:
      print "classroom = {0}:".format(classroom)
      for student in students:
         if student.classroom == classroom:
            print "\t{0}, {1}".format(student.last_name, student.first_name)

def handle_command(students, teachers, cmd):
   STUDENT = "Student"
   TEACHER = "Teacher"
   GRADE = "Grade"
   BUS = "Bus"
   AVERAGE = "Average"
   INFO = "Info"
   INVALID = "Invalid command"
   CLASSROOM = "Classroom"
   ENROLLMENT = "Enrollment"

   # S[tudent]: <last_name> [b[us]]
   if cmd[0] == STUDENT[:len(cmd[0])]:
      # S[tudent]: <last_name>
      if len(cmd) == 2:
         student_search(students, teachers, cmd[1])
      # S[tudent]: <last_name> B[us]
      elif len(cmd) == 3 and cmd[2] == BUS[:len(cmd[2])]:
         student_bus_search(students, cmd[1])
      else:
         print INVALID
   elif cmd[0] == TEACHER[:len(cmd[0])]:
      # T[eacher]: <last_name>
      if len(cmd) == 2:
         teacher_search(students, cmd[1])
      else:
         print_invalid()
   elif cmd[0] == GRADE[:len(cmd[0])]:
      # G[rade]: <grade> T[eacher]
      if len(cmd) == 3 and cmd[1].isdigit() and cmd[2] == TEACHER[:len(cmd[2])]:
         grade_teacher_search(students, teachers, int(cmd[1]))
      elif len(cmd) == 3 and cmd[2] == HIGH[:len(cmd[2])] and cmd[1].isdigit():
         grade_high_search(students, int(cmd[1]))
      elif len(cmd) == 3 and cmd[2] == LOW[:len(cmd[2])] and cmd[1].isdigit():
         grade_low_search(students, int(cmd[1]))
      elif len(cmd) == 2 and cmd[1].isdigit():
         grade_search(students, int(cmd[1]))
      else:
         print_invalid()
   elif cmd[0] == BUS[:len(cmd[0])]:
      if len(cmd) == 2 and cmd[1].isdigit():
         bus_search(students, int(cmd[1]))
      else:
         print_invalid()
   elif cmd[0] == AVERAGE[:len(cmd[0])]:
      if len(cmd) == 2 and cmd[1].isdigit():
         average_search(students, int(cmd[1]))
      else:
         print_invalid()
   elif cmd[0] == INFO[:len(cmd[0])]:
      if len(cmd) == 1:
         info_search(students)
      else:
         print_invalid()
   # C[lassroom]: <classroom> [T[eacher]]
   elif cmd[0] == CLASSROOM[:len(cmd[0])]:
      # C[lassroom]: <classroom>
      if len(cmd) == 2:
         classroom_search(students, int(cmd[1]))
      elif cmd[2] == TEACHER[:len(cmd[2])]:
         classroom_teacher_search(teachers, int(cmd[1]))
      else:
         print INVALID
   elif cmd[0] == ENROLLMENT[:len(cmd[0])]:
      enrollment(students)
   else:
      print_invalid()

def main():
   students = []
   teachers = []

   QUIT = "Quit"

   # scrapes files for student and teacher information
   record_students(students)
   record_teachers(teachers)

   # user input
   while 1:
      line = raw_input("Enter a command: ")
      # ignores empty lines and comments
      while len(line.strip()) == 0 or line.strip()[0] == "#":
         line = raw_input("Enter a command: ")
      # quit
      if line == QUIT[:len(line)]:
         break
      cmd = re.split(": | ", line)
      handle_command(students, teachers, cmd)

   return 0

if __name__ == "__main__":
   main()
