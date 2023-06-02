import mysql.connector
import pandas as pd


connection = mysql.connector.connect(
    host="FROSTRANGERTUF",
    user="AdminSSIS",
    password="AdminSSIS123",
    database="ssis_db"
)


class Course:
    def __init__(self):
        self.columns = ['Course Code', 'Course']
        self.cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM courses")
        #self.courses_df = pd.DataFrame(cursor.fetchall(), columns=self.columns)
    
    def returnCourseData(self):
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()
        return courses
    
    ## function to add a course to database
    def addCourse(self, code, value):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM courses WHERE `Course Code` = %s", (code,))
        if self.cursor.fetchone():
            print(f"Course code already exists.")
            return
        else:
            self.cursor.execute("INSERT INTO courses (`Course Code`, `Course`) VALUES (%s, %s)", (code, value))
            connection.commit()
            print(f"Course '{value}' added.\n")
        #cursor.reset()
          
    ## function to delete a course from the database
    def deleteCourse(self, code):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM courses WHERE `Course Code` = %s", (code,))
        if not self.cursor.fetchone():
            print(f"Course code {code} does not exist.\n")
        else:
            self.cursor.execute("DELETE FROM courses WHERE `Course Code` = %s", (code,))
            connection.commit()
            print(f"Course '{code}' has been deleted.\n")
            # need studentundercourse method here laters
        #cursor.reset()
        
     # function to display a course
    def displayCourse(self, index):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM courses LIMIT %s",( 1, index ))
        course = self.cursor.fetchone()
        if course:
            print(f"Course: {course[1]}")
            print(f"Course Code: {course[0]}")
        else:
            print("Invalid course index.")
          
    # function to display the course list
    def displayList(self):
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()
        
        print("Displaying list of courses...")
        for course in courses:
            print(f"Course: {course[1]}")
            print(f"Course Code: {course[0]} \n")
        print("All courses displayed successfully.\n")
    
    # function to search for courses (by courseName and CouseCode)
    def searchCourse(self, course):
        value = str(course).lower() + '%'
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM courses WHERE LOWER(`Course Code`) LIKE %s OR LOWER(`Course`) LIKE %s", (f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        if len(searchResults) == 0:
            print("No matches courses found.")
        else:
            print("Seach results: \n")
            for result in searchResults:
                print(f"Course: {result[1]}")
                print(f"Course Code: {result[0]} \n")
        return searchResults
    
    # function to update the course name field
    # checks what column is the selected cell and updates the cell accordingly while using the 
    #     primary key as an identifier of the row
    def updateCourse(self, unique_key, column, new_value):
        if column == 0:
            if self.courseCodeExists(new_value):
                return False, "Course code already exists."
            else:
                update_query = "UPDATE courses SET `Course Code` = %s WHERE `Course Code` = %s" 
        elif column == 1:
            update_query = "UPDATE courses SET `Course` = %s WHERE `Course Code` = %s"
        
        if update_query:
            self.cursor.execute(update_query, (new_value, unique_key))
            connection.commit()
            print(f"Row updated successfully: {unique_key}")
        else:
            print("Invalid column selected.") 


    def getCourseCode(self, course_name):
        self.cursor.execute("SELECT `Course Code` FROM courses WHERE `Course` = %s", (course_name,))
        row = self.cursor.fetchone()
        course_code = row[0]
        return course_code

    def getCourseName(self, course_code):
        self.cursor.execute("SELECT `Course` FROM courses WHERE `Course Code` = %s", (course_code,))
        row = self.cursor.fetchone()
        course_name = row[0]
        return course_name
        
        
    def getCourseNames(self):
        self.cursor.execute("SELECT `Course` FROM courses")
        courses = self.cursor.fetchall()
        course_names = [str(course[0]) for course in courses]
        return course_names
    
    def courseCodeExists(self, courseCode):
        self.cursor.execute("SELECT `Course Code` FROM courses WHERE `Course Code` = %s", (courseCode,))
        if self.cursor.fetchone():
            return True 
        else:
            return False
        





class StudentInfo():
    def __init__(self):
        self.columns = ['Student ID', 'Name', 'Gender', 'Year Level', 'Course']
        self.cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM student_info")
        #cursor1 = connection.cursor(buffered=True)
        #cursor1.execute("SELECT * FROM courses")

    def returnStudentData(self):
        self.cursor.execute("SELECT * FROM student_info")
        student_data = self.cursor.fetchall()
        return student_data
    
    #
    def addStudent(self, id, name, gender, year, stud_course):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (id, ))
        if self.cursor.fetchone():
            print(f"Student with ID '{id}' already exists.")
            return
        else:
            self.cursor.execute("INSERT INTO student_info (`Student ID`, `Name`, `Gender`, `Year Level`, `Course Code`) VALUES (%s, %s, %s, %s, %s)", 
                           (id, name, gender, year, stud_course))
            connection.commit()
            print(f"Student '{name}' has been added.\n")
    
    #
    def deleteStudent(self, id):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (id,))
        if not self.cursor.fetchone():
            print(f"Student with ID {id} does not exist.\n")
        else:
            self.cursor.execute("DELETE FROM student_info WHERE `Student ID` = %s", (id,))
            connection.commit()
            print(f"Student with ID '{id}' has been deleted.\n")    
    
    #     
    def displayStudent(self, index):
        #cursor = connection.cursor(buffered=True)
        self.cursor.execute("SELECT * FROM student_info LIMIT %s",( 1, index))
        student = self.cursor.fetchone()
        if student:
            print(f"ID: {student[0]}")     
            print(f"Name: {student[1]}")
            print(f"Gender: {student[2]}")
            print(f"Year Level: {student[3]}")
            print(f"Course: {student[4]} \n")
        else:
            print("Invalid student index.")
    
    #
    def displayList(self):
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM student_info")
        students = self.cursor.fetchall()   
        
        print("Displaying list of students...")
        for student in students:
            print(f"ID: {student[0]}")     
            print(f"Name: {student[1]}")
            print(f"Gender: {student[2]}")
            print(f"Year Level: {student[3]}")
            print(f"Course: {student[4]} \n")      
        print("All students displayed successfully.\n")
        
    #
    def searchStudent(self, value):
        value = str(value).lower() + '%'
        #cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Student ID`) LIKE %s OR LOWER(`Name`) LIKE %s OR LOWER(`Gender`) LIKE %s OR LOWER(`Year Level`) LIKE %s OR LOWER(`Course Code`) LIKE %s", 
                    (f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        if len(searchResults) == 0:
            print("No matching student found.")
        else:
            print("Seach results: \n")
            for student in searchResults:
                print(f"ID: {student[0]}")     
                print(f"Name: {student[1]}")
                print(f"Gender: {student[2]}")
                print(f"Year Level: {student[3]}")
                print(f"Course: {student[4]} \n")
        return searchResults

    def updateStudent(self, unique_key, column, new_value):
        update_query = ""

        if column == 0:
            # Update Student ID
            update_query = "UPDATE student_info SET `Student ID` = %s WHERE `Student ID` = %s"
        elif column == 1:
            # Update Name
            update_query = "UPDATE student_info SET `Name` = %s WHERE `Student ID` = %s"
        elif column == 2:
            # Update Gender
            update_query = "UPDATE student_info SET `Gender` = %s WHERE `Student ID` = %s"
        elif column == 3:
            # Update Year Level
            update_query = "UPDATE student_info SET `Year Level` = %s WHERE `Student ID` = %s"
        elif column == 4:
            # Update Course Code
            update_query = "UPDATE student_info SET `Course Code` = %s WHERE `Student ID` = %s"

        if update_query:
            self.cursor.execute(update_query, (new_value, unique_key))
            connection.commit()
            print(f"Row updated successfully: {unique_key}")
        else:
            print("Invalid column selected.")

    #
    def updateStudent111(self, current_value,  uniqueKey, column, new_value): #lacks row
        #cursor = connection.cursor(buffered=True)
        if column == 4:
            self.cursor.execute("SELECT * FROM courses WHERE `Course Code` = %s", (new_value,))
            if self.cursor.fetchone():
                update_query = "UPDATE student_info SET `Course Code` = %s WHERE `Course Code` = %s AND `Student ID` =%s"
                self.cursor.execute(update_query, (new_value, current_value, self.getStudentID(uniqueKey)))
                connection.commit()
                print("Student's course updated successfully.\n")
            else:
                print(f"Course code '{new_value}' not found.")
                return
                
        elif column == 0:
            update_query = "UPDATE student_info SET `Student ID` = %s WHERE `Student ID` = %s AND `Name` =%s"
            self.cursor.execute(update_query, (new_value, current_value, self.getStudentName(uniqueKey)))
            connection.commit()
            print(f"Student ID '{current_value}' updated to '{new_value}' successfully.\n")
        elif column == 1:
            update_query = "UPDATE student_info SET `Name` = %s WHERE `Name` = %s AND `Student ID` =%s"  # checked
            self.cursor.execute(update_query, (new_value, current_value, self.getStudentID(uniqueKey)))
            connection.commit()
            print(f"Student name '{current_value}' updated to '{new_value}' successfully.\n")
        elif column== 2:
            update_query = "UPDATE student_info SET `Gender` = %s WHERE `Gender` = %s AND `Student ID` =%s"
            self.cursor.execute(update_query, (new_value, current_value, self.getStudentID(uniqueKey)))
            connection.commit()
            print(f"Student's gender '{current_value}' updated to '{new_value}' successfully.\n")
        elif column == 3:
            update_query = "UPDATE student_info SET `Year Level` = %s WHERE `Year Level` = %s AND `Student ID` =%s"
            self.cursor.execute(update_query, (new_value, current_value, self.getStudentID(uniqueKey)))
            connection.commit()
            print(f"Student's year level '{current_value}' updated to '{new_value}' successfully.\n")   
            
    def getStudentID(self, name):
        self.cursor.execute("SELECT `Student ID` FROM student_info WHERE `Name` = %s", (name,))
        row = self.cursor.fetchone()
        studentid = row[0]
        return studentid
    
    def getStudentName(self, id):
        self.cursor.execute("SELECT `Name` FROM student_info WHERE `Student ID` = %s", (id,))
        row = self.cursor.fetchone()
        name = row[0]
        return name
        
        
    def studentIDExists(self, studentID):        
        self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (studentID,))
        if self.cursor.fetchone():
            return True
            
            
    # array of gender and year_level for selection
    gender = ['Male', 'Female', 'Non-Binary','Transgender', 'Prefer Not to Say', 'Not Listed']
    year_level = ['1', '2', '3', '4', '5']        
    
    
        
courseObject = Course()
studentObject = StudentInfo()


