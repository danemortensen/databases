# Dane Mortensen and Kartik Mendiratta

import sys

class Student:
   def __init__(self, first_name, last_name, grade, classroom, bus, gpa,\
      teacher_first, teacher_last):
      self.first_name = first_name
      self.last_name = last_name
      self.grade = grade
      self.classroom = classroom
      self.bus = bus
      self.gpa = gpa
      self.teacher_first = teacher_first
      self.teacher_last = teacher_last

def record_students(students):
   try:
      for line in open("students.txt"):
         info = line.strip().split(",")
         students.append(Student(info[1].strip(), info[0].strip(), int(info[2]), int(info[3]),\
            int(info[4]), float(info[5]), info[7].strip(), info[6].strip()))
   except:
      sys.exit()

def student_search(students, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: grade = {2}, classroom = {3}, teacher = {4}, {5}".format(student.last_name,\
            student.first_name, student.grade, student.classroom, student.teacher_last, student.teacher_first)

def student_bus_search(students, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: bus route = {2}".format(student.last_name,\
            student.first_name, student.bus)

def teacher_search(students, last_name):
   for student in students:
      if student.teacher_last == last_name:
         print "{0}, {1}".format(student.last_name, student.first_name)

def grade_high_search(students, grade):
   target = 0
   gpa = -1
   for student in students:
      if student.grade == grade and (gpa == -1 or student.gpa > gpa):
         target = student
         gpa = student.gpa

   if gpa >= 0:
      print "{0}, {1}: gpa = {2}, teacher = {3}, {4}, bus = {5}".format(target.last_name,\
         target.first_name, target.gpa, target.teacher_last, target.teacher_first, target.bus)

def grade_low_search(students, grade):
   target = 0
   gpa = -1
   for student in students:
      if student.grade == grade and (gpa == -1 or student.gpa < gpa):
         target = student
         gpa = student.gpa

   if gpa >= 0:
      print "{0}, {1}: gpa = {2}, teacher = {3}, {4}, bus = {5}".format(target.last_name,\
         target.first_name, target.gpa, target.teacher_last, target.teacher_first, target.bus)

def grade_search(students, grade):
   for student in students:
      if student.grade == grade:
         print "{0}, {1}".format(student.last_name, student.first_name)

def bus_search(students, bus):
   for student in students:
      if student.bus == bus:
         print "{0}, {1}: grade = {2}, classroom = {3}".format(student.last_name,\
            student.first_name, student.grade, student.classroom)

def average_search(students, grade):
   total = 0
   count = 0
   for student in students:
      if student.grade == grade:
         total += student.gpa
         count += 1

   if count > 0:
      print "Grade {0}: avg gpa = {1}".format(grade, total / count)

def info_search(students):
   grades = [0, 0, 0, 0, 0, 0, 0]
   for student in students:
      if student.grade >= 0 and student.grade <= 6:
         grades[student.grade] += 1

   for x in range(0, 7):
      print "{0}: {1}".format(x, grades[x])

def print_invalid():
   print("Invalid command")

def handle_command(students, cmd):
   STUDENT = "Student"
   BUS = "Bus"
   TEACHER = "Teacher"
   GRADE = "Grade"
   HIGH = "High"
   LOW = "Low"
   AVERAGE = "Average"
   INFO = "Info"

   if cmd[0] == STUDENT[:len(cmd[0])]:
      if len(cmd) == 2:
         student_search(students, cmd[1])
      elif len(cmd) == 3 and cmd[2] == BUS[:len(cmd[2])]:
         student_bus_search(students, cmd[1])
      else:
         print_invalid()
   elif cmd[0] == TEACHER[:len(cmd[0])]:
      if len(cmd) == 2:
         teacher_search(students, cmd[1])
      else:
         print_invalid()
   elif cmd[0] == GRADE[:len(cmd[0])]:
      if len(cmd) == 3 and cmd[2] == HIGH[:len(cmd[2])] and cmd[1].isdigit():
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
   else:
      print_invalid()

def main():
   QUIT = "Quit"

   students = []

   record_students(students)

   while 1:
      line = raw_input("Enter a command: ")
      while len(line.strip()) == 0 or line.strip()[0] == '#':
         line = raw_input()
      if line == QUIT[:len(line)]:
         break
      cmd = line.replace(": ", " ").split(" ")
      handle_command(students, cmd)

if __name__ == "__main__":
   main()
