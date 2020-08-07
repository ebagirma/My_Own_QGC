################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.0
##
################################################################################

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt

from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from Canvas import Canvas
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Canvas_box.removeWidget(self.ui.Canvas_label)
        self.ui.Canvas_label = Canvas()
        self.ui.Canvas_label.initialize()
        # We need to enable mouse tracking to follow the mouse without the button pressed.
       # self.ui.Canvas_label.setMouseTracking(True)
        # Enable focus to capture key inputs.
        #self.ui.Canvas_label.setFocusPolicy(Qt.StrongFocus)

        self.ui.Canvas_box.addWidget(self.ui.Canvas_label)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Drawing_page)
        
        # For the Drawing page
        self.ui.Drawing.clicked.connect(self.Drawing_page)
       
        # For the Home Page
        self.ui.Home.clicked.connect(self.Home_page)

        # For the Video
        self.ui.Video.clicked.connect(self.Camera_feed)
       
        

        #This is for the subition on the Canvas
        self.ui.sub.clicked.connect(self.sub_btn)


        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.RightButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS Elizabeth Eckford, one of the Little Rock Nine, is flanked by an angry mob as she makes her way to the entrance of Little Rock Central High School in Arkansas in 1957.
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
   
   
    def Drawing_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Drawing_page)

    def Home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
    def Camera_feed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Camera_Feed)    

    # Exporting the points to the  matplotlib
    def sub_btn(self):
        #print(Canvas().chosen_points)
        perivous_x = None
        perivous_y = None
        for pos in Canvas().chosen_points:
            current_x = pos.x()
            current_y = pos.y()
            if perivous_y and perivous_x:
                plt.plot([current_x,current_y],[perivous_x,perivous_y])
            perivous_x = current_x
            perivous_y = current_y
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
