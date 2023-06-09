# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V2gui_ssis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 740)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../CCC151-V1 Simple-Student-Information-System/winIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #f6fafd\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 70, 321, 521))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(10, 20, 311, 281))
        self.frame.setStyleSheet("background-color: #f6fafd\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 200, 301, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(29)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_course = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_course.setFont(font)
        self.label_course.setStyleSheet("color: #006fbe")
        self.label_course.setObjectName("label_course")
        self.horizontalLayout_4.addWidget(self.label_course)
        self.chooseCourse = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooseCourse.setFont(font)
        self.chooseCourse.setStyleSheet("QComboBox {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: #e2eff9;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    border-left-width: 0px;\n"
"    border-left-color: #cce4f5;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background-color: #e2eff9;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Documents/codes/python/CCC151- SSIS V2/down-arrow.png);\n"
"    width: 15px;  \n"
"    height: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    selection-background-color: #7dbae5;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"")
        self.chooseCourse.setObjectName("chooseCourse")
        self.chooseCourse.addItem("")
        self.chooseCourse.addItem("")
        self.horizontalLayout_4.addWidget(self.chooseCourse)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_id_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_id_2.setFont(font)
        self.label_id_2.setStyleSheet("color: #006fbe")
        self.label_id_2.setObjectName("label_id_2")
        self.horizontalLayout_3.addWidget(self.label_id_2)
        self.enterID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enterID.setFont(font)
        self.enterID.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"}\n"
"")
        self.enterID.setObjectName("enterID")
        self.horizontalLayout_3.addWidget(self.enterID)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(36)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: #006fbe")
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.enterSName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enterSName.setFont(font)
        self.enterSName.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"}\n"
"")
        self.enterSName.setClearButtonEnabled(False)
        self.enterSName.setObjectName("enterSName")
        self.horizontalLayout.addWidget(self.enterSName)
        self.addStudentButton = QtWidgets.QPushButton(self.frame)
        self.addStudentButton.setGeometry(QtCore.QRect(80, 250, 144, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addStudentButton.setFont(font)
        self.addStudentButton.setStyleSheet("QPushButton {\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"    min-width: 8em;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.addStudentButton.setObjectName("addStudentButton")
        self.label_StudentInformation = QtWidgets.QLabel(self.frame)
        self.label_StudentInformation.setGeometry(QtCore.QRect(20, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_StudentInformation.setFont(font)
        self.label_StudentInformation.setStyleSheet("color: #006fbe")
        self.label_StudentInformation.setObjectName("label_StudentInformation")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 120, 301, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(29)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_gender = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_gender.setFont(font)
        self.label_gender.setStyleSheet("color: #006fbe")
        self.label_gender.setObjectName("label_gender")
        self.horizontalLayout_7.addWidget(self.label_gender)
        self.chooseGender = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooseGender.setFont(font)
        self.chooseGender.setStyleSheet("QComboBox {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: #e2eff9;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    border-left-width: 0px;\n"
"    border-left-color: #cce4f5;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background-color: #e2eff9;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Documents/codes/python/CCC151- SSIS V2/down-arrow.png);\n"
"    width: 15px;  \n"
"    height: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    selection-background-color: #7dbae5;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"\n"
"")
        self.chooseGender.setObjectName("chooseGender")
        self.chooseGender.addItem("")
        self.chooseGender.addItem("")
        self.horizontalLayout_7.addWidget(self.chooseGender)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 160, 301, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(8)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_yearlvl = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_yearlvl.setFont(font)
        self.label_yearlvl.setStyleSheet("color: #006fbe")
        self.label_yearlvl.setObjectName("label_yearlvl")
        self.horizontalLayout_11.addWidget(self.label_yearlvl)
        self.chooseYearLvl = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooseYearLvl.setFont(font)
        self.chooseYearLvl.setStyleSheet("QComboBox {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: #e2eff9;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    border-left-width: 0px;\n"
"    border-left-color: #cce4f5;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background-color: #e2eff9;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Documents/codes/python/CCC151- SSIS V2/down-arrow.png);\n"
"    width: 15px;  \n"
"    height: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    selection-background-color: #7dbae5;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"    font: Helvetica;\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"\n"
"")
        self.chooseYearLvl.setObjectName("chooseYearLvl")
        self.chooseYearLvl.addItem("")
        self.chooseYearLvl.addItem("")
        self.horizontalLayout_11.addWidget(self.chooseYearLvl)
        self.horizontalLayout_11.setStretch(1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(0, 320, 311, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addCourseButton = QtWidgets.QPushButton(self.frame_2)
        self.addCourseButton.setGeometry(QtCore.QRect(90, 150, 144, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addCourseButton.setFont(font)
        self.addCourseButton.setStyleSheet("QPushButton {\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"    min-width: 8em;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.addCourseButton.setObjectName("addCourseButton")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 60, 301, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_CourseName = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_CourseName.setFont(font)
        self.label_CourseName.setStyleSheet("color: #006fbe")
        self.label_CourseName.setObjectName("label_CourseName")
        self.horizontalLayout_5.addWidget(self.label_CourseName)
        self.enterCourse = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enterCourse.setFont(font)
        self.enterCourse.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"\n"
"}\n"
"")
        self.enterCourse.setClearButtonEnabled(False)
        self.enterCourse.setObjectName("enterCourse")
        self.horizontalLayout_5.addWidget(self.enterCourse)
        self.label_Courses = QtWidgets.QLabel(self.frame_2)
        self.label_Courses.setGeometry(QtCore.QRect(100, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_Courses.setFont(font)
        self.label_Courses.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Courses.setStyleSheet("color:#006fbe")
        self.label_Courses.setObjectName("label_Courses")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 100, 301, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_CourseCode = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.label_CourseCode.setFont(font)
        self.label_CourseCode.setStyleSheet("color: #006fbe")
        self.label_CourseCode.setObjectName("label_CourseCode")
        self.horizontalLayout_6.addWidget(self.label_CourseCode)
        self.enterCode = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enterCode.setFont(font)
        self.enterCode.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"\n"
"}\n"
"")
        self.enterCode.setClearButtonEnabled(False)
        self.enterCode.setObjectName("enterCode")
        self.horizontalLayout_6.addWidget(self.enterCode)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(340, 0, 761, 731))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_6)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 771, 701))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.tabWidget.setSizeIncrement(QtCore.QSize(20000, 3392))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 2px solid #006fbe;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; \n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
";\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    width: 90px;\n"
"    min-width: 10ex;\n"
"    padding: 8px;\n"
"    background-color: #7dbae5;\n"
"    color: white;\n"
"    font: Bold 14px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border: 2px;\n"
"    border-color: #7dbae5;\n"
"    border-bottom-color:  #006fbe;\n"
"    background-color: #7dbae5;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 3px; /* make non-selected tabs look smaller */\n"
"    background-color: #b5d8f0;\n"
"    border-color: #9B9B9B;\n"
"}\n"
"\n"
"QTabBar::tab::hover {\n"
"    background-color: #7dbae5;\n"
"\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 761, 52))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.searchInputStudent = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.searchInputStudent.setFont(font)
        self.searchInputStudent.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"}\n"
"")
        self.searchInputStudent.setText("")
        self.searchInputStudent.setClearButtonEnabled(False)
        self.searchInputStudent.setObjectName("searchInputStudent")
        self.horizontalLayout_14.addWidget(self.searchInputStudent)
        self.searchStudentButton = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchStudentButton.setFont(font)
        self.searchStudentButton.setStyleSheet("QPushButton{\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"    min-width: 8em;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.searchStudentButton.setObjectName("searchStudentButton")
        self.horizontalLayout_14.addWidget(self.searchStudentButton)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.StudentTable = QtWidgets.QTableView(self.tab)
        self.StudentTable.setEnabled(True)
        self.StudentTable.setGeometry(QtCore.QRect(10, 50, 741, 551))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.StudentTable.setFont(font)
        self.StudentTable.setStyleSheet("QTableView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #cce4f5;\n"
"    font: Helvetica;\n"
"    color: #006fbe;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #b5d8f0; /* Background color of selected item */\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: #006fbe;\n"
"    font-weight: bold; \n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #e2eff9;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #b5d8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #b5d8f0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: #e2eff9;\n"
"    height: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #b5d8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #b5d8f0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: none;\n"
"}\n"
"")
        self.StudentTable.setObjectName("StudentTable")
        self.statusUpdateS = QtWidgets.QTextEdit(self.tab)
        self.statusUpdateS.setGeometry(QtCore.QRect(10, 620, 621, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusUpdateS.setFont(font)
        self.statusUpdateS.setStyleSheet("QTextEdit {\n"
"    border: 1px solid #f6fafd;\n"
"\n"
"    padding: 2px 10px;\n"
"    background-color: #f6fafd;\n"
"    font: 9px;\n"
"     border-bottom-color:  #006fbe;\n"
"    color: #006fbe;\n"
"}\n"
"")
        self.statusUpdateS.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusUpdateS.setReadOnly(True)
        self.statusUpdateS.setAcceptRichText(True)
        self.statusUpdateS.setObjectName("statusUpdateS")
        self.deleteStudentButton = QtWidgets.QPushButton(self.tab)
        self.deleteStudentButton.setGeometry(QtCore.QRect(640, 610, 111, 30))
        self.deleteStudentButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.deleteStudentButton.setFont(font)
        self.deleteStudentButton.setStyleSheet("QPushButton {\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.deleteStudentButton.setObjectName("deleteStudentButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 761, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.searchInputCourse = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.searchInputCourse.setFont(font)
        self.searchInputCourse.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #cce4f5;\n"
"    border-radius: 6px;\n"
"    padding: 2px 10px;\n"
"    background-color: white;\n"
"    font: 14px;\n"
"    color: #006fbe;\n"
"}\n"
"background-color: white\n"
"\n"
"")
        self.searchInputCourse.setText("")
        self.searchInputCourse.setClearButtonEnabled(False)
        self.searchInputCourse.setObjectName("searchInputCourse")
        self.horizontalLayout_9.addWidget(self.searchInputCourse)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.searchCourseButton = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchCourseButton.setFont(font)
        self.searchCourseButton.setStyleSheet("QPushButton{\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"    min-width: 8em;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.searchCourseButton.setObjectName("searchCourseButton")
        self.horizontalLayout_10.addWidget(self.searchCourseButton)
        self.CourseTable = QtWidgets.QTableView(self.tab_2)
        self.CourseTable.setEnabled(True)
        self.CourseTable.setGeometry(QtCore.QRect(10, 50, 741, 551))
        self.CourseTable.setStyleSheet("QTableView {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #cce4f5;\n"
"    font: Helvetica;\n"
"    color: #006fbe;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #b5d8f0; /* Background color of selected item */\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: #006fbe;\n"
"    font-weight: bold; \n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #e2eff9;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #b5d8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #b5d8f0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: #e2eff9;\n"
"    height: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #b5d8f0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #b5d8f0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: none;\n"
"}\n"
"")
        self.CourseTable.setObjectName("CourseTable")
        self.statusUpdateC = QtWidgets.QTextEdit(self.tab_2)
        self.statusUpdateC.setGeometry(QtCore.QRect(10, 620, 621, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusUpdateC.setFont(font)
        self.statusUpdateC.setStyleSheet("QTextEdit {\n"
"    border: 1px solid #f6fafd;\n"
"\n"
"    padding: 2px 10px;\n"
"    background-color: #f6fafd;\n"
"    font: 9px;\n"
"     border-bottom-color:  #006fbe;\n"
"    color: #006fbe;\n"
"}\n"
"")
        self.statusUpdateC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusUpdateC.setReadOnly(True)
        self.statusUpdateC.setObjectName("statusUpdateC")
        self.deleteCourseButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteCourseButton.setGeometry(QtCore.QRect(640, 610, 111, 30))
        self.deleteCourseButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.deleteCourseButton.setFont(font)
        self.deleteCourseButton.setStyleSheet("QPushButton {\n"
"    background-color: #7dbae5;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 8px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5aa7de;\n"
"    border-style: inset;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5aa7de;\n"
"    border-style: outset;\n"
"}")
        self.deleteCourseButton.setObjectName("deleteCourseButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Student Information System"))
        self.label_course.setText(_translate("MainWindow", "Course:"))
        self.chooseCourse.setCurrentText(_translate("MainWindow", "rwe"))
        self.chooseCourse.setItemText(0, _translate("MainWindow", "rwe"))
        self.chooseCourse.setItemText(1, _translate("MainWindow", "fewf"))
        self.label_id_2.setText(_translate("MainWindow", "ID number:"))
        self.enterID.setPlaceholderText(_translate("MainWindow", "  Enter ID number of student"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.enterSName.setPlaceholderText(_translate("MainWindow", "  Enter name of student"))
        self.addStudentButton.setText(_translate("MainWindow", "Add Student"))
        self.label_StudentInformation.setText(_translate("MainWindow", "Student Information"))
        self.label_gender.setText(_translate("MainWindow", "Gender:"))
        self.chooseGender.setCurrentText(_translate("MainWindow", "rwe"))
        self.chooseGender.setItemText(0, _translate("MainWindow", "rwe"))
        self.chooseGender.setItemText(1, _translate("MainWindow", "fewf"))
        self.label_yearlvl.setText(_translate("MainWindow", "Year Level:"))
        self.chooseYearLvl.setCurrentText(_translate("MainWindow", "rwe"))
        self.chooseYearLvl.setItemText(0, _translate("MainWindow", "rwe"))
        self.chooseYearLvl.setItemText(1, _translate("MainWindow", "fewf"))
        self.addCourseButton.setText(_translate("MainWindow", "Add Course"))
        self.label_CourseName.setText(_translate("MainWindow", "Course Name:"))
        self.enterCourse.setPlaceholderText(_translate("MainWindow", "  Enter course"))
        self.label_Courses.setText(_translate("MainWindow", "Courses"))
        self.label_CourseCode.setText(_translate("MainWindow", "Course Code:"))
        self.enterCode.setPlaceholderText(_translate("MainWindow", "  Enter code"))
        self.searchInputStudent.setPlaceholderText(_translate("MainWindow", "  Search student..."))
        self.searchStudentButton.setText(_translate("MainWindow", "Search"))
        self.deleteStudentButton.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Student List"))
        self.searchInputCourse.setPlaceholderText(_translate("MainWindow", "  Search course..."))
        self.searchCourseButton.setText(_translate("MainWindow", "Search"))
        self.deleteCourseButton.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Course List"))
