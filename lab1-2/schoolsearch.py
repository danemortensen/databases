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
         teacher = classroom_to_teacher(teachers, student.classroom)
         print "{0}, {1}: grade = {2}, classroom = {3}, teacher = {4}, {5}".format(student.last_name,\
               student.first_name, student.grade, student.classroom, teacher.last_name,\
               teacher.first_name)

def student_bus_search(students, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: bus route = {2}".format(student.last_name,\
               student.first_name, student.bus)

def teacher_search(students, teachers, last_name):
   classrooms = []
   for teacher in teachers:
      if teacher.last_name == last_name:
         classrooms.append(teacher.classroom)

   for student in students:
      if student.classroom in classrooms:
         print "{0}, {1}".format(student.last_name, student.first_name)

def grade_high_search(students, teachers, grade):
   target = 0
   gpa = -1

   for student in students:
      if student.grade == grade and (gpa == -1 or student.gpa > gpa):
         target = student
         gpa = student.gpa

   if gpa >= 0:
      teacher = classroom_to_teacher(teachers, target.classroom)
      print "{0}, {1}: gpa = {2}, teacher = {3}, {4}, bus = {5}".format(target.last_name,\
         target.first_name, target.gpa, teacher.last_name, teacher.first_name, target.bus)

def grade_low_search(students, teachers, grade):
   target = 0
   gpa = -1

   for student in students:
      if student.grade == grade and (gpa == -1 or student.gpa < gpa):
         target = student
         gpa = student.gpa

   if gpa >= 0:
      teacher = classroom_to_teacher(teachers, target.classroom)
      print "{0}, {1}: gpa = {2}, teacher = {3}, {4}, bus = {5}".format(target.last_name,\
         target.first_name, target.gpa, teacher.last_name, teacher.first_name, target.bus)

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
      total = 0
      for student in students:
         if student.classroom == classroom:
            total += 1
      print "classroom = {0}: {1}".format(classroom, total)

def data_grade(students):
   gpa_totals = [0, 0, 0, 0, 0, 0, 0]
   student_totals = [0, 0, 0, 0, 0, 0, 0]

   for student in students:
      gpa_totals[student.grade] += student.gpa
      student_totals[student.grade] += 1

   for i in range(0, 7):
      if student_totals[i] > 0:
         print "grade {0}: avg gpa = {1}".format(i, gpa_totals[i] / student_totals[i])

def askey(teacher):
   return teacher.last_name + " " + teacher.first_name

def data_teacher(students, teachers):
   gpas = {}
   counts = {}

   for student in students:
      teacher = classroom_to_teacher(teachers, student.classroom)
      if counts.has_key(askey(teacher)):
         gpas[askey(teacher)] += student.gpa
         counts[askey(teacher)] += 1
      else:
         gpas[askey(teacher)] = student.gpa
         counts[askey(teacher)] = 1

   for key in counts.keys():
      last = key.split(" ")[0]
      first = key.split(" ")[1]
      print "{0}, {1}: avg gpa = {2}".format(last, first, gpas[key] / counts[key])

def data_bus(students):
   gpas = {}
   counts = {}

   for student in students:
      if counts.has_key(student.bus):
         gpas[student.bus] += student.gpa
         counts[student.bus] += 1
      else:
         gpas[student.bus] = student.gpa
         counts[student.bus] = 1

   for key in counts.keys():
      print "bus {0}: avg gpa = {1}".format(key, gpas[key] / counts[key])

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
   HIGH = "High"
   LOW = "Low"
   DATA = "Data"

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
         teacher_search(students, teachers, cmd[1])
      else:
         print INVALID
   elif cmd[0] == GRADE[:len(cmd[0])]:
      # G[rade]: <grade> T[eacher]
      if len(cmd) == 3 and cmd[1].isdigit() and cmd[2] == TEACHER[:len(cmd[2])]:
         grade_teacher_search(students, teachers, int(cmd[1]))
      # G[rade]: <grade> H[igh]
      elif len(cmd) == 3 and cmd[2] == HIGH[:len(cmd[2])] and cmd[1].isdigit():
         grade_high_search(students, teachers, int(cmd[1]))
      # G[rade]: <grade> L[ow]
      elif len(cmd) == 3 and cmd[2] == LOW[:len(cmd[2])] and cmd[1].isdigit():
         grade_low_search(students, teachers, int(cmd[1]))
      # G[rade]: <grade>
      elif len(cmd) == 2 and cmd[1].isdigit():
         grade_search(students, int(cmd[1]))
      else:
         print INVALID
   # B[us]: <bus>
   elif cmd[0] == BUS[:len(cmd[0])]:
      if len(cmd) == 2 and cmd[1].isdigit():
         bus_search(students, int(cmd[1]))
      else:
         print INVALID
   # A[verage]: <grade>
   elif cmd[0] == AVERAGE[:len(cmd[0])]:
      if len(cmd) == 2 and cmd[1].isdigit():
         average_search(students, int(cmd[1]))
      else:
         print INVALID
   # I[nfo]
   elif cmd[0] == INFO[:len(cmd[0])] and len(cmd) == 1:
      info_search(students)
   # C[lassroom]: <classroom> [T[eacher]]
   elif cmd[0] == CLASSROOM[:len(cmd[0])]:
      # C[lassroom]: <classroom>
      if len(cmd) == 2 and cmd[1].isdigit():
         classroom_search(students, int(cmd[1]))
      # C[lassroom]: <classroom> T[eacher]
      elif len(cmd) == 3 and cmd[1].isdigit() and cmd[2] == TEACHER[:len(cmd[2])]:
         classroom_teacher_search(teachers, int(cmd[1]))
      else:
         print INVALID
   # E[nrollment]
   elif cmd[0] == ENROLLMENT[:len(cmd[0])] and len(cmd) == 1:
      enrollment(students)
   elif cmd[0] == DATA[:len(cmd[0])] and len(cmd) == 2:
      # D[ata]: G[rade]
      if cmd[1] == GRADE[:len(cmd[1])]:
         data_grade(students)
      # D[ata]: T[eacher]
      elif cmd[1] == TEACHER[:len(cmd[1])]:
         data_teacher(students, teachers)
      # D[ata]: B[us]
      elif cmd[1] == BUS[:len(cmd[1])]:
         data_bus(students)
      else:
         print INVALID
   else:
      print INVALID

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
         line = raw_input()
      # quit
      if line == QUIT[:len(line)]:
         break
      cmd = re.split(": | ", line)
      handle_command(students, teachers, cmd)

   return 0

if __name__ == "__main__":
   main()
