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

def teacher_search(teachers, classroom):
   for teacher in teachers:
      if teacher.classroom == classroom:
         print("classroom = {0}, teacher = {1}, {2}".format(classroom,\
               teacher.last_name, teacher.first_name))

def student_search(students, teachers, last_name):
   for student in students:
      if student.last_name == last_name:
         print "{0}, {1}: grade = {2}, ".format(student.last_name,\
               student.first_name, student.grade),
         teacher_search(teachers, student.classroom)

def handle_command(students, teachers, cmd):
   STUDENT = "Student"

   if cmd[0] == STUDENT[:len(cmd[0])]:
      if len(cmd) == 2:
         student_search(students, teachers, cmd[1])

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
