import mysql.connector


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
        #self.cursor.execute("SELECT * FROM courses")
    
    def returnCourseData(self):
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()
        return courses
    
    ## function to add a course to database, checks first if course code already exists
    def addCourse(self, code, value):
        self.cursor.execute("SELECT * FROM courses WHERE `Course Code` = %s", (code,))
        if self.cursor.fetchone():
            print(f"Course code already exists.")
            return
        else:
            self.cursor.execute("INSERT INTO courses (`Course Code`, `Course`) VALUES (%s, %s)", (code, value))
            connection.commit()
            print(f"Course '{value}' added.\n")

          
    ## function to delete a course from the database
    def deleteCourse(self, code):
        self.cursor.execute("SELECT * FROM courses WHERE `Course Code` = %s", (code,))
        if not self.cursor.fetchone():
            print(f"Course code {code} does not exist.\n")
        else:
            self.cursor.execute("DELETE FROM courses WHERE `Course Code` = %s", (code,))
            connection.commit()
            print(f"Course '{code}' has been deleted.\n")
        
     # function to display a course
    def displayCourse(self, index):
        self.cursor.execute("SELECT * FROM courses LIMIT %s",( 1, index))
        course = self.cursor.fetchone()
        if course:
            print(f"Course: {course[1]}")
            print(f"Course Code: {course[0]}")
        else:
            print("Invalid course index.")
          
    # function to display the course list
    def displayList(self):
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
    
    # function to update the course field/cell
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
            print(f"Row updated successfully: {unique_key} with new change: {new_value}")
        else:
            print("Invalid column selected.") 

    # Gets the Course code of a row using Course column
    def getCourseCode(self, course_name):
        self.cursor.execute("SELECT `Course Code` FROM courses WHERE `Course` = %s", (course_name,))
        row = self.cursor.fetchone()
        course_code = row[0]
        return course_code

    # Gets the Course of a row using Course Code column
    def getCourseName(self, course_code):
        self.cursor.execute("SELECT `Course` FROM courses WHERE `Course Code` = %s", (course_code,))
        row = self.cursor.fetchone()
        course_name = row[0]
        return course_name
        
    # gets the list of all courses under Course column
    def getCourseNames(self):
        self.cursor.execute("SELECT `Course` FROM courses")
        courses = self.cursor.fetchall()
        course_names = [str(course[0]) for course in courses]
        return course_names
    
    # checks if Course Code already exists in the database
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
        #self.cursor.execute("SELECT * FROM student_info")

    def returnStudentData(self):
        self.cursor.execute("SELECT * FROM student_info")
        student_data = self.cursor.fetchall()
        return student_data
    
    # function to add a student to database, checks first if student id already exists
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
    
    # function to delete a student from the database
    def deleteStudent(self, id):
        self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (id,))
        if not self.cursor.fetchone():
            print(f"Student with ID {id} does not exist.\n")
        else:
            self.cursor.execute("DELETE FROM student_info WHERE `Student ID` = %s", (id,))
            connection.commit()
            print(f"Student with ID '{id}' has been deleted.\n")    
    
    # function to display a student 
    def displayStudent(self, index):
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
    
    # function to display the student list
    def displayList(self):
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
        
    # function to search for student data
    def searchStudent(self, column, value):
        value = str(value).lower() + '%'
        
        if column is not None:
            if column == 'Gender':
                self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Gender`) LIKE %s", (f"%{value}",))
            elif column == 'Student ID':
                self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Student ID`) LIKE %s", (f"%{value}",))
            elif column == 'Name':
                self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Name`) LIKE %s", (f"%{value}",))
            elif column == 'Year Level':
                self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Year Level`) LIKE %s", (f"%{value}",))
            elif column == 'Course Code':
                self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Course Code`) LIKE %s", (f"%{value}",))
        else:
            self.cursor.execute("SELECT * FROM student_info WHERE LOWER(`Student ID`) LIKE %s OR LOWER(`Name`) LIKE %s OR LOWER(`Gender`) LIKE %s OR LOWER(`Year Level`) LIKE %s OR LOWER(`Course Code`) LIKE %s",
                                (f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}"))
        
        searchResults = self.cursor.fetchall()

        if len(searchResults) == 0:
            print("No matching student found.")
        else:
            print("Search results:\n")
            for student in searchResults:
                print(f"ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Gender: {student[2]}")
                print(f"Year Level: {student[3]}")
                print(f"Course: {student[4]}\n")

        return searchResults

    # function to update the student field/cell
    # checks what column is the selected cell and updates the cell accordingly while using the 
    #     primary key as an identifier of the row
    def updateStudent(self, unique_key, column, new_value):
        update_query = ""

        if column == 0:
            update_query = "UPDATE student_info SET `Student ID` = %s WHERE `Student ID` = %s"
        elif column == 1:
            update_query = "UPDATE student_info SET `Name` = %s WHERE `Student ID` = %s"
        elif column == 2:
            update_query = "UPDATE student_info SET `Gender` = %s WHERE `Student ID` = %s"
        elif column == 3:
            update_query = "UPDATE student_info SET `Year Level` = %s WHERE `Student ID` = %s"
        elif column == 4:
            update_query = "UPDATE student_info SET `Course Code` = %s WHERE `Student ID` = %s"

        if update_query:
            self.cursor.execute(update_query, (new_value, unique_key))
            connection.commit()
            print(f"Row updated successfully: {unique_key} with new change: {new_value}")
        else:
            print("Invalid column selected.")

    # gets the Student ID of a row using the Name column       
    def getStudentID(self, name):
        self.cursor.execute("SELECT `Student ID` FROM student_info WHERE `Name` = %s", (name,))
        row = self.cursor.fetchone()
        studentid = row[0]
        return studentid
    
    # gets the Name of the student in a row using the Student ID column
    def getStudentName(self, id):
        self.cursor.execute("SELECT `Name` FROM student_info WHERE `Student ID` = %s", (id,))
        row = self.cursor.fetchone()
        name = row[0]
        return name
    
    #checks if Student ID already exists in the database
    def studentIDExists(self, studentID):        
        self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (studentID,))
        if self.cursor.fetchone():
            return True
            
    def genderExistsInArray(self, new_value):
        return new_value in self.gender
    
    def yearExistsInArray(self, new_value):
        return new_value in self.year_level
            
    # array of gender and year_level for selection in GUI
    gender = ['Male', 'Female', 'Non-Binary','Transgender', 'Prefer Not to Say', 'Not Listed']
    year_level = ['1', '2', '3', '4', '5']        
    
    
        
courseObject = Course()
studentObject = StudentInfo()


