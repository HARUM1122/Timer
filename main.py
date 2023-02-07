from PyQt5 import QtWidgets as q,uic,QtCore
from sys import exit as e,argv
class Functions:
    def __init__(self):
        self.startTimer=False
        self.dic={
            "hours":0,
            "mins":0,
            "seconds":0}
    def increment(self,label,b):
        if self.dic[b]<59 and b!='hours':
            self.dic[b]+=1
        elif self.dic[b]<24 and b=="hours":
            self.dic[b]+=1
        else:
            self.dic[b]=0
        label.setText(f"{'0' if self.dic[b]<10 else '' }{self.dic[b]}")
    def decrement(self,label,b):
        if self.dic[b]!=0:
            self.dic[b]-=1 
        else:
            self.dic[b]=59 if b!="hours" else 24
        label.setText(f"{'0' if self.dic[b]<10 else '' }{self.dic[b]}")
    def reset(self):
        for i in self.dic.keys():
            self.dic[i]=0
        self.hoursLabel_3.setText("00")
        self.minsLabel_3.setText("00")
        self.secondsLabel_3.setText("00")
        self.hoursLabel_4.setText("00")
        self.minsLabel_4.setText("00")
        self.secondsLabel_4.setText("00")
        self.startTimer=False
        self.stackedWidget.setCurrentWidget(self.page)
    def timer_(self):
        if self.startTimer:
            if self.dic['seconds']==0:
                if not self.dic['mins'] and not self.dic['hours']:
                    self.startTimer=False
                    print("DONE")
                else:
                    self.dic['mins']-=1 if self.dic['mins']!=0 else 0
                    self.dic['seconds']=59
            if self.dic['mins']==0:
                if self.dic['hours']:
                    self.dic['hours']-=1 if self.dic['hours']!=0 else 0
                    self.dic['mins']=59
            self.hoursLabel_4.setText(f"{'0' if self.dic['hours']<10 else '' }{self.dic['hours']}")
            self.minsLabel_4.setText(f"{'0' if self.dic['mins']<10 else '' }{self.dic['mins']}")
            self.secondsLabel_4.setText(f"{'0' if self.dic['seconds']<10 else '' }{self.dic['seconds']}")
            self.dic['seconds']-=1 if self.dic['seconds']!=0 else 0
    def start_(self):
        if self.dic['hours']==0 and self.dic['mins']==0 and self.dic['seconds']==0:
            return
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.hoursLabel_4.setText(self.hoursLabel_3.text())
        self.minsLabel_4.setText(self.minsLabel_3.text())
        self.secondsLabel_4.setText(self.secondsLabel_3.text())
        self.startTimer=True
    def pauseResume(self):
        if not self.startTimer:
            self.pauseResumeButton.setText(f"PAUSE")
        else:
            self.pauseResumeButton.setText(f"RESUME")
        self.startTimer=not self.startTimer

class Buttons(Functions):
    def addButtons(self):
        self.incrementHoursButton_3.clicked.connect(lambda:self.increment(self.hoursLabel_3,"hours"))       
        self.decrementHoursButton_3.clicked.connect(lambda:self.decrement(self.hoursLabel_3,"hours"))
        self.incrementMinutesButton_3.clicked.connect(lambda:self.increment(self.minsLabel_3,"mins"))       
        self.decrementMinutesButton_3.clicked.connect(lambda:self.decrement(self.minsLabel_3,"mins"))
        self.incrementSecondsButton_3.clicked.connect(lambda:self.increment(self.secondsLabel_3,"seconds"))       
        self.decrementSecondsButton_3.clicked.connect(lambda:self.decrement(self.secondsLabel_3,"seconds"))
        self.reset_button.clicked.connect(self.reset)
        self.resetButton_2.clicked.connect(self.reset)
        self.startButton.clicked.connect(self.start_)
        self.pauseResumeButton.clicked.connect(self.pauseResume)
class window(q.QMainWindow,Buttons):
    def __init__(self):
        super().__init__()
        uic.loadUi("MyTimer.ui",self)
        self.timer=QtCore.QTimer()
        self.header_frame.mouseMoveEvent=self.moveWindow
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.exit.clicked.connect(self.close)
        self.minimizeButton.clicked.connect(self.showMinimized)
        self.addButtons()
        self.timer.timeout.connect(self.timer_)
        self.timer.start(1000)
    def mousePressEvent(self,event):
        self.clickPosition=event.globalPos()
    def moveWindow(self,event):
        if event.buttons()==QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos()-self.clickPosition+event.globalPos())
            self.clickPosition=event.globalPos()
            event.accept()
if __name__=="__main__":
    app = q.QApplication(argv)
    w = window()
    w.show()
    e(app.exec_())
