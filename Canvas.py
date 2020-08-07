from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




class Canvas(QLabel):

    drawing = False
    brushSize = 2
    brushColor = Qt.black
    lastPoint = QPoint()
    background_color = QColor(Qt.white)
    chosen_points = []
    def initialize(self):
        self.setPixmap(QPixmap(self.size()))
        # Clear the canvas.
        print( self.size())
        self.pixmap().fill(self.background_color)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(8)
        painter.setPen(pen)
       # painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        #painter.drawPoint(300, 300)
       # painter.drawLine(100, 100, 400, 400)
        perivous_x = None
        perivous_y = None
      
        for pos in self.chosen_points:
            painter.drawPoint(pos)
            current_x = pos.x()
            current_y = pos.y()
            print('the current',current_x)
           
           # painter.drawLine(self.pos.x(), self.pos.y(),current_x,current_y)
            if perivous_y and perivous_x:
                painter.drawLine(current_x,current_y,perivous_x,perivous_y)
                
            perivous_x = current_x
            perivous_y = current_y
    def mouseReleaseEvent(self, cursor_event):
        self.chosen_points.append(cursor_event.pos())
        # self.chosen_points.append(self.mapFromGlobal(QtGui.QCursor.pos()))
        self.update()
    def mouseMoveEvent(self, event):
      #  distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
        self.postion = event.pos()
        print(self.postion.x())
        self.update()

