from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from math import *

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader=QUiLoader()
        self.ui=loader.load('untitled.ui')
        self.ui.show()
        
        self.ui.Zero_btn.clicked.connect(self.n0)
        self.ui.One_btn.clicked.connect(self.n1)
        self.ui.Two_btn.clicked.connect(self.n2)
        self.ui.Three_btn.clicked.connect(self.n3)
        self.ui.Four_btn.clicked.connect(self.n4)
        self.ui.Five_btn.clicked.connect(self.n5)
        self.ui.Six_btn.clicked.connect(self.n6)
        self.ui.Seven_btn.clicked.connect(self.n7)
        self.ui.Eight_btn.clicked.connect(self.n8)
        self.ui.Nine_btn.clicked.connect(self.n9) 
        self.ui.add_btn.clicked.connect(self.add)
        self.ui.sub_btn.clicked.connect(self.sub)
        self.ui.mul_btn.clicked.connect(self.mul)
        self.ui.divid_btn.clicked.connect(self.divid)
        self.ui.sin_btn.clicked.connect(self.sin)
        self.ui.cos_btn.clicked.connect(self.cos)
        self.ui.tan_btn.clicked.connect(self.tan)
        self.ui.cot_btn.clicked.connect(self.cot)
        self.ui.log_btn.clicked.connect(self.log)
        self.ui.sqr_btn.clicked.connect(self.sqrt)
        self.ui.dot_btn.clicked.connect(self.dot)
        self.ui.equal_btn.clicked.connect(self.equal)
        self.ui.delet_btn.clicked.connect(self.delet)

        
    def n0(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'0')
    def n1(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'1')
    def n2(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'2')
    def n3(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'3')
    def n4(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'4')
    def n5(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'5')
    def n6(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'6')
    def n7(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'7')
    def n8(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'8')
    def n9(self):
        self.ui.TextBox.setText(self.ui.TextBox.text()+'9')
        

    def add(self):
            self.num1=float(self.ui.TextBox.text())
            self.ui.TextBox.setText('')
            self.Operand='+'
            
    def sub(self):
            self.num1=float(self.ui.TextBox.text())
            self.ui.TextBox.setText('')
            self.Operand='-'   
            
    def mul(self):
            self.num1=float(self.ui.TextBox.text())
            self.ui.TextBox.setText('')
            self.Operand='*'              

    def divid(self):
            self.num1=float(self.ui.TextBox.text())
            self.ui.TextBox.setText('')
            self.Operand='/'
            
    def sin(self):
        self.num1=float(self.ui.TextBox.text())
        self.daraje=self.num1/360*2*pi
        self.result=sin(self.daraje)
        self.ui.TextBox.setText(str(self.result))
        
    def cos(self):
        self.num1=float(self.ui.TextBox.text())
        self.daraje=self.num1/360*2*pi
        self.result=cos(self.daraje)
        self.ui.TextBox.setText(str(self.result))

    def tan(self):
        self.num1=float(self.ui.TextBox.text())
        self.daraje=self.num1/360*2*pi
        self.result=tan(self.daraje)
        self.ui.TextBox.setText(str(self.result))
             
    def cot(self):
        self.num1=float(self.ui.TextBox.text())
        self.daraje=self.num1/360*2*pi
        self.result=1/tan(self.daraje)
        self.ui.TextBox.setText(str(self.result))
        
    def log(self):
        self.num1=float(self.ui.TextBox.text())
        self.result=log10(self.num1)
        self.ui.TextBox.setText(str(self.result))

    def sqrt(self):
        self.ui.TextBox.setText(str(sqrt(float(self.ui.TextBox.text()))))

    def dot(self):
        if '.' not in self.ui.TextBox.text():
            self.ui.TextBox.setText(self.ui.TextBox.text()+'.')

    def delet(self):
       self.ui.TextBox.setText('')
       
       
    def equal(self):
        self.num2=float(self.ui.TextBox.text())
        if self.Operand=='+':
            self.result=self.num1+self.num2
            self.ui.TextBox.setText(str(self.result))
            
        elif self.Operand=='-':
            self.result=self.num1-self.num2
            self.ui.TextBox.setText(str(self.result))
        
        elif self.Operand=='*':
            self.result= self.num1*self.num2
            self.ui.TextBox.setText(str(self.result))
        
        elif self.Operand=='/':
            
                self.result= self.num1/self.num2
                self.ui.TextBox.setText(str(self.result))
                
my_app=QApplication()
main_window=calculator()
my_app.exec()