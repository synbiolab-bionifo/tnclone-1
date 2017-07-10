#!/usr/bin/python

from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
class MplCanvas(FigureCanvas):
	def __init__(self):
		#self.fig = Figure()
		self.fig = plt.figure(figsize=(10,8.5))
		self.ax = self.fig.add_subplot(111)
		FigureCanvas.__init__(self, self.fig)
		FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

class matplotlibWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.canvas = MplCanvas()
		self.vbl = QtGui.QVBoxLayout()
		self.vbl.addWidget(self.canvas)
		self.setLayout(self.vbl)


