
import pandas as pd

from Student_and_Course_Class_V2 import Course, StudentInfo


def main():

    course = Course()
    student = StudentInfo()

    course.addCourse('BSIS','BS in Info System' )
    course.addCourse('BSIT','BS in Info Tech' )
    course.addCourse('BSCA','BS in Computer Applications')
    course.addCourse('BSCA','BS in Computer Application')
    course.deleteCourse('BSCA')
    course.displayList()
    course.searchCourse('BSIT')
    course.searchCourse('BSMS')
    course.searchCourse('BS in I')
    #course.updateCourse('BSIT', 0, 'BSIIT')
    course.addCourse('BSCT','BS in Computer Application')

    student.addStudent("126","John","Male","3","BSIT")  # works
    student.addStudent("2021-3131","John Doe","Male","1","BSCT") 
    student.addStudent("126","John","Male","3","BSIT") 
    course.updateCourse('BSCT', 0, 'BSCA')
    student.addStudent("145","Lizard","Male","2","BSCS") 
    student.deleteStudent("145") 
    student.searchStudent("Male")
    student.displayList()
    
    student.updateStudent("Rhea", 1,"Rhea Salve")
    #student.updateStudent("Rhea Salve", 1,"Rhea")
'''    
    student.addStudent("John", "126", "BSIT")
    student.updateStudent("R", "Rhea", 'BSCS')  # id issue same SOLVED
    student.addStudent("R", "2021-2362", "BSCS")
    student.searchStudent('I')
    student.searchStudent("12445")  # not found  SOLVED
    student.updateStudent("R", "Rhea", 'BSCS')
    course.addCourse('BS in Computer Science', 'BSCS')
    student.addStudent("R", "2021-2362", "BSCS")
    course.displayList()

    course.updateCourse('BSIT', 'BS in Information Technology')
    course.searchCourse('BSIT')
    course.searchCourse('BS in Information Technology')
    course.searchCourse('BS in Info Tech')
    course.searchCourse('BSME')
    course.displayList()

'''




main()
