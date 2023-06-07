import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from V2gui_ssis import Ui_MainWindow
import Student_and_Course_Class_V2 as classObject

class MainWindow(QtWidgets.QMainWindow):
    studentModel = QtGui.QStandardItemModel()
    courseModel = QtGui.QStandardItemModel()

    def __init__(self, ui):
        super().__init__()
        self.courseObject = classObject.courseObject
        self.studentObject = classObject.studentObject
        self.gui_ssis = ui
        self.gui_ssis.setupUi(self)
        self.setStandardItemModel()
        self.gui_ssis.addCourseButton.clicked.connect(self.add_course_button_clicked)
        self.gui_ssis.enterCode.returnPressed.connect(self.add_course_button_clicked)
        self.gui_ssis.addStudentButton.clicked.connect(self.add_student_button_clicked)
        #comboBox
        self.setCoursesSelection()
        self.setGenderSelection()
        self.setYearLvlSelection()
        
        self.gui_ssis.deleteCourseButton.clicked.connect(self.delete_course_row)
        self.gui_ssis.deleteStudentButton.clicked.connect(self.delete_student_row)

        self.gui_ssis.searchCourseButton.clicked.connect(self.search_course_button_clicked)
        self.gui_ssis.searchInputCourse.returnPressed.connect(self.search_course_button_clicked)
        
        self.gui_ssis.searchStudentButton.clicked.connect(self.search_student_button_clicked)
        self.gui_ssis.searchInputStudent.returnPressed.connect(self.search_student_button_clicked)

        self.gui_ssis.CourseTable.doubleClicked.connect(self.course_table_cell_edit)
        self.gui_ssis.StudentTable.doubleClicked.connect(self.student_table_cell_edit)
        

    def setSModel(self, data, model):
        #rows = cursor.fetchall()
        for row_id, row in enumerate(data):
            for col_id, value in enumerate(row):
                text = str(value)
                item = QtGui.QStandardItem(text)
                model.setItem(row_id, col_id, item)
                #print(f"text: {text}")
                if col_id in [0, 1, 2, 3, 4]:
                    item.setEditable(False)
                if col_id in [0, 1, 2, 3, 4]:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                else:
                    item.setTextAlignment(QtCore.Qt.AlignLeft)
                model.setItem(row_id, col_id, item)
        return model
    
    def adjustTableColumns(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        if table == self.gui_ssis.StudentTable: # 699 total size
                header.resizeSection(0, 120)  
                header.resizeSection(1, 249)  
                header.resizeSection(2, 150) 
                header.resizeSection(3, 80)
                header.resizeSection(4, 100) 
        elif table == self.gui_ssis.CourseTable:
                header.resizeSection(0, 240)  
                header.resizeSection(1, 459)  

    def clearModel(self, model, rows=0, cols=0):
        model.clear()
        model.setRowCount(rows)
        model.setColumnCount(cols)
        
    def setStandardItemModel(self):
        self.studentModel = QtGui.QStandardItemModel()
        self.courseModel = QtGui.QStandardItemModel()
        self.studentModel = self.setSModel(self.studentObject.returnStudentData(), self.studentModel)
        self.courseModel = self.setSModel(self.courseObject.returnCourseData(), self.courseModel)
        
        self.studentModel.setHorizontalHeaderLabels(self.studentObject.columns)
        self.gui_ssis.StudentTable.setModel(self.studentModel)
        self.courseModel.setHorizontalHeaderLabels(self.courseObject.columns)
        self.gui_ssis.CourseTable.setModel(self.courseModel)
        
        self.adjustTableColumns(self.gui_ssis.StudentTable)
        self.adjustTableColumns(self.gui_ssis.CourseTable)
        
    def setCoursesSelection(self):
        self.gui_ssis.chooseCourse.clear() 
        self.gui_ssis.chooseCourse.addItems(self.courseObject.getCourseNames()) 
        
    def setGenderSelection(self):
        self.gui_ssis.chooseGender.clear() 
        self.gui_ssis.chooseGender.addItems(self.studentObject.gender) 
        
    def setYearLvlSelection(self):
        self.gui_ssis.chooseYearLvl.clear() 
        self.gui_ssis.chooseYearLvl.addItems([str(year) for year in self.studentObject.year_level])
        
    def add_course_button_clicked(self):
        course_name = self.gui_ssis.enterCourse.text()
        course_code = self.gui_ssis.enterCode.text()
        self.courseObject.addCourse(course_code, course_name)
        
        self.setStandardItemModel()
        self.gui_ssis.CourseTable.model().layoutChanged.emit()
        self.setCoursesSelection()
        self.gui_ssis.enterCourse.clear()
        self.gui_ssis.enterCode.clear()
    
    def add_student_button_clicked(self):
        student_name = self.gui_ssis.enterSName.text()
        student_id = self.gui_ssis.enterID.text()
        student_gender = self.gui_ssis.chooseGender.currentText()
        student_yearlvl = self.gui_ssis.chooseYearLvl.currentText()        
        student_course = self.gui_ssis.chooseCourse.currentText()


        student_course_code = self.courseObject.getCourseCode(student_course)

        self.studentObject.addStudent(student_id, student_name, student_gender, student_yearlvl, student_course_code)
        self.setStandardItemModel()
        self.gui_ssis.StudentTable.model().layoutChanged.emit()
        self.gui_ssis.enterSName.clear()
        self.gui_ssis.enterID.clear()
    
    def delete_course_row(self):
        selected_rows = self.gui_ssis.CourseTable.currentIndex().row()
        column_index = 0
        course = self.gui_ssis.CourseTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this course?\nThe students under this course will also be deleted.",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.courseObject.deleteCourse(course)

        self.courseModel = self.setSModel(self.courseObject.returnCourseData(), self.courseModel)
        self.setStandardItemModel()
        self.gui_ssis.CourseTable.model().layoutChanged.emit()
        self.setCoursesSelection()
        
    def delete_student_row(self):
        selected_rows = self.gui_ssis.StudentTable.currentIndex().row()
        column_index = 1
        student = self.gui_ssis.StudentTable.model().index(selected_rows, column_index).data()
        reply = QtWidgets.QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this student?",
                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.studentObject.deleteStudent(student)

        self.studentModel = self.setSModel(self.studentObject.returnStudentData(), self.studentModel)
        self.setStandardItemModel()
        self.gui_ssis.StudentTable.model().layoutChanged.emit()


    def search_course_button_clicked(self): 
        search_coursetxt = self.gui_ssis.searchInputCourse.text()
        CResults = self.courseObject.searchCourse(search_coursetxt)
        #print("Results:", CResults) 
        if CResults:
            self.clearModel(self.courseModel)
            self.courseModel = self.setSModel(CResults, self.courseModel)
            self.courseModel.setHorizontalHeaderLabels(self.courseObject.columns)
            self.gui_ssis.CourseTable.setModel(self.courseModel)
            self.adjustTableColumns(self.gui_ssis.CourseTable)
            self.gui_ssis.CourseTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for course '{search_coursetxt}'.")
            
    def search_student_button_clicked(self): 
        search_studenttxt = self.gui_ssis.searchInputStudent.text()
        SResults = self.studentObject.searchStudent(search_studenttxt)
        #print("Results:", SResults) 
        if SResults:
            self.clearModel(self.studentModel)
            self.studentModel = self.setSModel(SResults, self.studentModel)
            self.studentModel.setHorizontalHeaderLabels(self.studentObject.columns)
            self.gui_ssis.StudentTable.setModel(self.studentModel)
            self.adjustTableColumns(self.gui_ssis.StudentTable)
            self.gui_ssis.StudentTable.model().layoutChanged.emit()
        else:
            QtWidgets.QMessageBox.information(self, "No Results", f"No results found for course '{search_studenttxt}'.")
    
    
    def course_table_cell_edit(self, index):
        row = index.row()
        column = index.column()
        item = self.gui_ssis.CourseTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_ssis.CourseTable.model().item(row, 0).text() 
        new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Course", "Enter new text:", text=current_value)
        
        if ok and new_value and new_value != current_value:
            reply = QtWidgets.QMessageBox.question(self, "Save Changes", "Do you want to save the changes?", 
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if column == 0:
                    self.courseObject.updateCourse(unique_key, column, new_value)
                    self.setStandardItemModel()
                    self.gui_ssis.CourseTable.model().layoutChanged.emit()
                elif column == 1:
                    self.courseObject.updateCourse(unique_key, column, new_value)
                    self.setStandardItemModel()
                    self.gui_ssis.CourseTable.model().layoutChanged.emit()
                    self.setCoursesSelection()
            else:
                pass

                
    def student_table_cell_edit(self, index):
        column = index.column()
        row = index.row()
        item = self.gui_ssis.StudentTable.model().item(row, column)
        current_value = item.text()
        unique_key = self.gui_ssis.StudentTable.model().item(row, 0).text()  

        new_value, ok = QtWidgets.QInputDialog.getText(self, "Update Student", "Enter new text:", text=current_value)
        if ok and new_value and new_value != current_value:
            reply = QtWidgets.QMessageBox.question(self, "Save Changes", "Do you want to save the changes?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if column in [1, 3]:   
                    self.studentObject.updateStudent( unique_key, column, new_value)
                    self.setStandardItemModel()
                    self.gui_ssis.StudentTable.model().layoutChanged.emit()
                elif column in [0]:
                    if self.studentObject.studentIDExists(new_value) == True:
                        QtWidgets.QMessageBox.warning(self, "Student ID Exists", "Student ID already exists.")
                    else:
                        self.studentObject.updateStudent( unique_key, column, new_value)
                        self.setStandardItemModel()
                        self.gui_ssis.StudentTable.model().layoutChanged.emit()
                elif column in [2]:
                    if self.studentObject.genderExistsInArray(new_value) == False:
                        QtWidgets.QMessageBox.warning(self, "Input Error", "Gender not in selection. Please input based on here:\n   Male\n   Female\n   Non-Binary\n   Transgender\n   Prefer Not to Say\n   Not Listed")
                    else:
                        self.studentObject.updateStudent( unique_key, column, new_value)
                        self.setStandardItemModel()
                        self.gui_ssis.StudentTable.model().layoutChanged.emit()
                elif column in [4]:
                    if self.courseObject.courseCodeExists(new_value) == False:
                        QtWidgets.QMessageBox.warning(self, "Course Unavailable", "Course does not exist.")
                    else:
                        self.studentObject.updateStudent( unique_key, column, new_value)
                        self.setStandardItemModel()
                        self.gui_ssis.StudentTable.model().layoutChanged.emit()    
                else:
                    #QtWidgets.QMessageBox.warning(self, "Invalid Column", "Invalid column selected.")
                    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow(ui)
    window.show()
    sys.exit(app.exec_())

