# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict_ui3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import sqlite3 as s
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Database:

    def __init__(self):
        # self.file = s.Connection(r'D:\my content\Education\Library\dict.db')
        self.file = s.Connection(r'dict.db')
        self.obj = self.file.cursor()

    def show(self,word):
    
        self.qry = f'SELECT word, def, exm from other WHERE serial = (SELECT serial FROM eng WHERE word = upper(\'{word}\'))'
        self.result = self.obj.execute(self.qry)
        
        l = []
        for i in self.result:
            l.append(i)

        return l

    def up(self,word):
    
        ts = time.strftime('%d-%m-%Y %H:%M:%S')
        l = self.show(word)
        data = l[0][0]
        qry = f'insert into history(word,mean,ts) values (\'{word}\',\'{data}\',\'{ts}\')'
        self.obj.execute(qry)
        self.file.commit()


class Ui_Dictionary(object):
    def setupUi(self, Dictionary):
        Dictionary.setObjectName("Dictionary")
        Dictionary.resize(499, 495)
        self.centralwidget = QtWidgets.QWidget(Dictionary)
        self.centralwidget.setObjectName("centralwidget")
        self.input_lab = QtWidgets.QLabel(self.centralwidget)
        self.input_lab.setGeometry(QtCore.QRect(40, 30, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_lab.setFont(font)
        self.input_lab.setObjectName("input_lab")
        self.word_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.word_entry.setGeometry(QtCore.QRect(40, 70, 290, 20))
        self.word_entry.setObjectName("word_entry")
        font.setPointSize(10)
        self.word_entry.setFont(font)
        self.l_tamil = QtWidgets.QLabel(self.centralwidget)
        self.l_tamil.setGeometry(QtCore.QRect(50, 130, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_tamil.setFont(font)
        self.l_tamil.setObjectName("l_tamil")
        self.l_definition = QtWidgets.QLabel(self.centralwidget)
        self.l_definition.setGeometry(QtCore.QRect(50, 240, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_definition.setFont(font)
        self.l_definition.setObjectName("l_definition")
        self.l_exam = QtWidgets.QLabel(self.centralwidget)
        self.l_exam.setGeometry(QtCore.QRect(50, 350, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_exam.setFont(font)
        self.l_exam.setObjectName("l_exam")
        self.translate = QtWidgets.QPushButton(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.translate.setObjectName("translate")
        self.out_def = QtWidgets.QTextBrowser(self.centralwidget)
        self.out_def.setGeometry(QtCore.QRect(40, 270, 410, 61))
        self.out_def.setObjectName("out_def")
        font.setPointSize(10)
        self.out_def.setFont(font)
        self.out_exam = QtWidgets.QTextBrowser(self.centralwidget)
        self.out_exam.setGeometry(QtCore.QRect(40, 380, 410, 61))
        self.out_exam.setObjectName("out_exam")
        self.out_exam.setFont(font)
        self.out_tamil = QtWidgets.QTextBrowser(self.centralwidget)
        self.out_tamil.setGeometry(QtCore.QRect(40, 160, 410, 61))
        self.out_tamil.setObjectName("out_tamil")
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.out_tamil.setFont(font)
        Dictionary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dictionary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        Dictionary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dictionary)
        self.statusbar.setObjectName("statusbar")
        Dictionary.setStatusBar(self.statusbar)

        self.retranslateUi(Dictionary)
        QtCore.QMetaObject.connectSlotsByName(Dictionary)

    def retranslateUi(self, Dictionary):
        _translate = QtCore.QCoreApplication.translate
        Dictionary.setWindowTitle(_translate("Dictionary", "Dictionary"))
        self.input_lab.setText(_translate("Dictionary", "Word"))
        self.l_tamil.setText(_translate("Dictionary", "Tamil Meaning"))
        self.l_definition.setText(_translate("Dictionary", "Defintion"))
        self.l_exam.setText(_translate("Dictionary", "Example"))
        self.translate.setText(_translate("Dictionary", "Translate"))
        
        


class App(Ui_Dictionary,QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)
        # print(dir(self.word_entry))
        # help(self.word_entry.focusWidget)
        # help(self.word_entry.selectAll)
        self.show()
        self.translate.clicked.connect(self.meaning)
        
    def meaning(self):
        a = Database()
        self.word = self.word_entry.text()
        # file = open("./mean.txt",'a')
        try:
            self.data = (a.show(self.word))[0][0]
            self.Def  = (a.show(self.word))[0][1].replace("[","").replace("]","")
            self.exam = (a.show(self.word))[0][2]
            self.out_tamil.setText(self.data)
            self.out_def.setText(self.Def)
            self.out_exam.setText(self.exam)
            # a.up(self.word)
            self.word_entry.setFocus()
            self.word_entry.selectAll()
            
        
            
        except:
            self.out_tamil.setText("No Meaning Found ")
            self.out_def.setText("No Defintion Found ")
            self.out_exam.setText("No Example Found ")
            self.word_entry.setFocus()
            self.word_entry.selectAll()
        

app = QtWidgets.QApplication([])
w = App()
sys.exit(app.exec_())

# a = Ui_Dictionary()
# dir(a.word_entry)

