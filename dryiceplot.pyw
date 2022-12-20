# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:56:19 2022

@author: WielensDH
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import pyqtgraph as pg
import os
from qtmimport.qtmimport import *
import datetime

# Stuff for PyQt5
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

# Change the working directory to the QTMtoolbox directory (where the script itself should be)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Plot class
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=9, height=6, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

# Create MainWindow
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('DryICE Logfile plotter (v1.1 - 2022-12-20)')
        
        layout_main = QHBoxLayout()
        
        layout_left = QVBoxLayout()
        
        # File selector section
        layout_file = QHBoxLayout()
        btn_fileOpen = QPushButton()
        btn_fileOpen.setIcon(QIcon('icons/folder-horizontal-open.png'))
        btn_fileOpen.setIconSize(QSize(16, 16))
        layout_file.addWidget(btn_fileOpen)
        layout_file.addWidget(QLabel('File path:'))
        self.file_path = QLineEdit()
        layout_file.addWidget(self.file_path)
        layout_left.addLayout(layout_file)
        
        # Plot section
        self.canvas = MplCanvas(self, width=9, height=6, dpi=100)
        self.canvas.axes.plot([0, 1, 2, 3, 4], [2, 4, 8, 16, 32])
        self.canvas.fig.tight_layout()
        toolbar = NavigationToolbar2QT(self.canvas, self)
        layout_plot = QVBoxLayout()
        layout_plot.addWidget(toolbar)
        layout_plot.addWidget(self.canvas)
        layout_left.addLayout(layout_plot)
        
        # File info section
        layout_right = QVBoxLayout()     
        lbl_fileInfo = QLabel('File info:')
        boldFont = QFont()
        boldFont.setBold(True)
        lbl_fileInfo.setFont(boldFont)
        layout_right.addWidget(lbl_fileInfo)
        self.lblStart = QLabel('Start time: ')
        self.lblEnd = QLabel('End time: ')
        layout_right.addWidget(self.lblStart)
        layout_right.addWidget(self.lblEnd)
        hsep = QFrame()
        hsep.setFrameShape(QFrame.HLine)
        layout_right.addWidget(hsep)
        # Add some blank space
        layout_right.addWidget(QLabel(' '))
        layout_right.addWidget(QLabel(' '))
        layout_right.addWidget(QLabel(' '))
        layout_right.addWidget(QLabel(' '))
        
        # Parameters
        layout_header = QHBoxLayout()
        layout_header.addWidget(QLabel(' '))
        layout_header.addWidget(QLabel('Name'))
        layout_header.addWidget(QLabel('Mult.'))
        layout_header.addWidget(QLabel('Off.'))
        layout_right.addLayout(layout_header)
        
        layout_param1 = QHBoxLayout()
        self.chk_param1 = QCheckBox()
        self.chk_param1.clicked.connect(lambda: self.chk1_changed(self.canvas.axes, self.canvas))
        layout_param1.addWidget(self.chk_param1)
        self.lbl_param1 = QLabel('Parameter 1')
        layout_param1.addWidget(self.lbl_param1)
        self.mult_param1 = QLineEdit('1')
        self.mult_param1.setFixedWidth(50)
        self.mult_param1.returnPressed.connect(lambda: self.mult1_changed(self.canvas.axes, self.canvas))
        layout_param1.addWidget(self.mult_param1)
        self.off_param1 = QLineEdit('0')
        self.off_param1.setFixedWidth(50)
        self.off_param1.returnPressed.connect(lambda: self.mult1_changed(self.canvas.axes, self.canvas))
        layout_param1.addWidget(self.off_param1)
        layout_right.addLayout(layout_param1)

        layout_param2 = QHBoxLayout()
        self.chk_param2 = QCheckBox()
        self.chk_param2.clicked.connect(lambda: self.chk2_changed(self.canvas.axes, self.canvas))
        layout_param2.addWidget(self.chk_param2)
        self.lbl_param2 = QLabel('Parameter 1')
        layout_param2.addWidget(self.lbl_param2)
        self.mult_param2 = QLineEdit('1')
        self.mult_param2.setFixedWidth(50)
        self.mult_param2.returnPressed.connect(lambda: self.mult2_changed(self.canvas.axes, self.canvas))
        layout_param2.addWidget(self.mult_param2)
        self.off_param2 = QLineEdit('0')
        self.off_param2.setFixedWidth(50)
        self.off_param2.returnPressed.connect(lambda: self.mult2_changed(self.canvas.axes, self.canvas))
        layout_param2.addWidget(self.off_param2)
        layout_right.addLayout(layout_param2) 

        layout_param3 = QHBoxLayout()
        self.chk_param3 = QCheckBox()
        self.chk_param3.clicked.connect(lambda: self.chk3_changed(self.canvas.axes, self.canvas))
        layout_param3.addWidget(self.chk_param3)
        self.lbl_param3 = QLabel('Parameter 1')
        layout_param3.addWidget(self.lbl_param3)
        self.mult_param3 = QLineEdit('1')
        self.mult_param3.setFixedWidth(50)
        self.mult_param3.returnPressed.connect(lambda: self.mult3_changed(self.canvas.axes, self.canvas))
        layout_param3.addWidget(self.mult_param3)
        self.off_param3 = QLineEdit('0')
        self.off_param3.setFixedWidth(50)
        self.off_param3.returnPressed.connect(lambda: self.mult3_changed(self.canvas.axes, self.canvas))
        layout_param3.addWidget(self.off_param3)
        layout_right.addLayout(layout_param3) 

        layout_param4 = QHBoxLayout()
        self.chk_param4 = QCheckBox()
        self.chk_param4.clicked.connect(lambda: self.chk4_changed(self.canvas.axes, self.canvas))
        layout_param4.addWidget(self.chk_param4)
        self.lbl_param4 = QLabel('Parameter 1')
        layout_param4.addWidget(self.lbl_param4)
        self.mult_param4 = QLineEdit('1')
        self.mult_param4.setFixedWidth(50)
        self.mult_param4.returnPressed.connect(lambda: self.mult4_changed(self.canvas.axes, self.canvas))
        layout_param4.addWidget(self.mult_param4)
        self.off_param4 = QLineEdit('0')
        self.off_param4.setFixedWidth(50)
        self.off_param4.returnPressed.connect(lambda: self.mult4_changed(self.canvas.axes, self.canvas))
        layout_param4.addWidget(self.off_param4)
        layout_right.addLayout(layout_param4) 

        layout_param5 = QHBoxLayout()
        self.chk_param5 = QCheckBox()
        self.chk_param5.clicked.connect(lambda: self.chk5_changed(self.canvas.axes, self.canvas))
        layout_param5.addWidget(self.chk_param5)
        self.lbl_param5 = QLabel('Parameter 1')
        layout_param5.addWidget(self.lbl_param5)
        self.mult_param5 = QLineEdit('1')
        self.mult_param5.setFixedWidth(50)
        self.mult_param5.returnPressed.connect(lambda: self.mult5_changed(self.canvas.axes, self.canvas))
        layout_param5.addWidget(self.mult_param5)
        self.off_param5 = QLineEdit('0')
        self.off_param5.setFixedWidth(50)
        self.off_param5.returnPressed.connect(lambda: self.mult5_changed(self.canvas.axes, self.canvas))
        layout_param5.addWidget(self.off_param5)
        layout_right.addLayout(layout_param5) 

        layout_param6 = QHBoxLayout()
        self.chk_param6 = QCheckBox()
        self.chk_param6.clicked.connect(lambda: self.chk6_changed(self.canvas.axes, self.canvas))
        layout_param6.addWidget(self.chk_param6)
        self.lbl_param6 = QLabel('Parameter 1')
        layout_param6.addWidget(self.lbl_param6)
        self.mult_param6 = QLineEdit('1')
        self.mult_param6.setFixedWidth(50)
        self.mult_param6.returnPressed.connect(lambda: self.mult6_changed(self.canvas.axes, self.canvas))
        layout_param6.addWidget(self.mult_param6)
        self.off_param6 = QLineEdit('0')
        self.off_param6.setFixedWidth(50)
        self.off_param6.returnPressed.connect(lambda: self.mult6_changed(self.canvas.axes, self.canvas))
        layout_param6.addWidget(self.off_param6)
        layout_right.addLayout(layout_param6) 

        layout_param7 = QHBoxLayout()
        self.chk_param7 = QCheckBox()    
        self.chk_param7.clicked.connect(lambda: self.chk7_changed(self.canvas.axes, self.canvas))
        layout_param7.addWidget(self.chk_param7)
        self.lbl_param7 = QLabel('Parameter 1')
        layout_param7.addWidget(self.lbl_param7)
        self.mult_param7 = QLineEdit('1')
        self.mult_param7.setFixedWidth(50)
        self.mult_param7.returnPressed.connect(lambda: self.mult7_changed(self.canvas.axes, self.canvas))
        layout_param7.addWidget(self.mult_param7)
        self.off_param7 = QLineEdit('0')
        self.off_param7.setFixedWidth(50)
        self.off_param7.returnPressed.connect(lambda: self.mult7_changed(self.canvas.axes, self.canvas))
        layout_param7.addWidget(self.off_param7)
        layout_right.addLayout(layout_param7) 

        layout_param8 = QHBoxLayout()
        self.chk_param8 = QCheckBox()
        self.chk_param8.clicked.connect(lambda: self.chk8_changed(self.canvas.axes, self.canvas))
        layout_param8.addWidget(self.chk_param8)
        self.lbl_param8 = QLabel('Parameter 1')
        layout_param8.addWidget(self.lbl_param8)
        self.mult_param8 = QLineEdit('1')
        self.mult_param8.setFixedWidth(50)
        self.mult_param8.returnPressed.connect(lambda: self.mult8_changed(self.canvas.axes, self.canvas))
        layout_param8.addWidget(self.mult_param8)
        self.off_param8 = QLineEdit('0')
        self.off_param8.setFixedWidth(50)
        self.off_param8.returnPressed.connect(lambda: self.mult8_changed(self.canvas.axes, self.canvas))
        layout_param8.addWidget(self.off_param8)
        layout_right.addLayout(layout_param8) 

        layout_param9 = QHBoxLayout()
        self.chk_param9 = QCheckBox()
        self.chk_param9.clicked.connect(lambda: self.chk9_changed(self.canvas.axes, self.canvas))
        layout_param9.addWidget(self.chk_param9)
        self.lbl_param9 = QLabel('Parameter 1')
        layout_param9.addWidget(self.lbl_param9)
        self.mult_param9 = QLineEdit('1')
        self.mult_param9.setFixedWidth(50)
        self.mult_param9.returnPressed.connect(lambda: self.mult9_changed(self.canvas.axes, self.canvas))
        layout_param9.addWidget(self.mult_param9)
        self.off_param9 = QLineEdit('0')
        self.off_param9.setFixedWidth(50)
        self.off_param9.returnPressed.connect(lambda: self.mult9_changed(self.canvas.axes, self.canvas))
        layout_param9.addWidget(self.off_param9)
        layout_right.addLayout(layout_param9) 

        layout_param10 = QHBoxLayout()
        self.chk_param10 = QCheckBox()
        self.chk_param10.clicked.connect(lambda: self.chk10_changed(self.canvas.axes, self.canvas))
        layout_param10.addWidget(self.chk_param10)
        self.lbl_param10 = QLabel('Parameter 1')
        layout_param10.addWidget(self.lbl_param10)
        self.mult_param10 = QLineEdit('1')
        self.mult_param10.setFixedWidth(50)
        self.mult_param10.returnPressed.connect(lambda: self.mult10_changed(self.canvas.axes, self.canvas))
        layout_param10.addWidget(self.mult_param10)
        self.off_param10 = QLineEdit('0')
        self.off_param10.setFixedWidth(50)
        self.off_param10.returnPressed.connect(lambda: self.mult10_changed(self.canvas.axes, self.canvas))
        layout_param10.addWidget(self.off_param10)
        layout_right.addLayout(layout_param10) 

        layout_param11 = QHBoxLayout()
        self.chk_param11 = QCheckBox()
        self.chk_param11.clicked.connect(lambda: self.chk11_changed(self.canvas.axes, self.canvas))
        layout_param11.addWidget(self.chk_param11)
        self.lbl_param11 = QLabel('Parameter 1')
        layout_param11.addWidget(self.lbl_param11)
        self.mult_param11 = QLineEdit('1')
        self.mult_param11.setFixedWidth(50)
        self.mult_param11.returnPressed.connect(lambda: self.mult11_changed(self.canvas.axes, self.canvas))
        layout_param11.addWidget(self.mult_param11)
        self.off_param11 = QLineEdit('0')
        self.off_param11.setFixedWidth(50)
        self.off_param11.returnPressed.connect(lambda: self.mult11_changed(self.canvas.axes, self.canvas))
        layout_param11.addWidget(self.off_param11)
        layout_right.addLayout(layout_param11) 

        layout_param12 = QHBoxLayout()
        self.chk_param12 = QCheckBox()
        self.chk_param12.clicked.connect(lambda: self.chk12_changed(self.canvas.axes, self.canvas))
        layout_param12.addWidget(self.chk_param12)
        self.lbl_param12 = QLabel('Parameter 1')
        layout_param12.addWidget(self.lbl_param12)
        self.mult_param12 = QLineEdit('1')
        self.mult_param12.setFixedWidth(50)
        self.mult_param12.returnPressed.connect(lambda: self.mult12_changed(self.canvas.axes, self.canvas))
        layout_param12.addWidget(self.mult_param12)
        self.off_param12 = QLineEdit('0')
        self.off_param12.setFixedWidth(50)
        self.off_param12.returnPressed.connect(lambda: self.mult12_changed(self.canvas.axes, self.canvas))
        layout_param12.addWidget(self.off_param12)
        layout_right.addLayout(layout_param12) 

        layout_param13 = QHBoxLayout()
        self.chk_param13 = QCheckBox()
        self.chk_param13.clicked.connect(lambda: self.chk13_changed(self.canvas.axes, self.canvas))
        layout_param13.addWidget(self.chk_param13)
        self.lbl_param13 = QLabel('Parameter 1')
        layout_param13.addWidget(self.lbl_param13)
        self.mult_param13 = QLineEdit('1')
        self.mult_param13.setFixedWidth(50)
        self.mult_param13.returnPressed.connect(lambda: self.mult13_changed(self.canvas.axes, self.canvas))
        layout_param13.addWidget(self.mult_param13)
        self.off_param13 = QLineEdit('0')
        self.off_param13.setFixedWidth(50)
        self.off_param13.returnPressed.connect(lambda: self.mult13_changed(self.canvas.axes, self.canvas))
        layout_param13.addWidget(self.off_param13)
        layout_right.addLayout(layout_param13) 

        layout_param14 = QHBoxLayout()
        self.chk_param14 = QCheckBox()
        self.chk_param14.clicked.connect(lambda: self.chk14_changed(self.canvas.axes, self.canvas))
        layout_param14.addWidget(self.chk_param14)
        self.lbl_param14 = QLabel('Parameter 1')
        layout_param14.addWidget(self.lbl_param14)
        self.mult_param14 = QLineEdit('1')
        self.mult_param14.setFixedWidth(50)
        self.mult_param14.returnPressed.connect(lambda: self.mult14_changed(self.canvas.axes, self.canvas))
        layout_param14.addWidget(self.mult_param14)
        self.off_param14 = QLineEdit('0')
        self.off_param14.setFixedWidth(50)
        self.off_param14.returnPressed.connect(lambda: self.mult14_changed(self.canvas.axes, self.canvas))
        layout_param14.addWidget(self.off_param14)
        layout_right.addLayout(layout_param14)         
        
        layout_param15 = QHBoxLayout()
        self.chk_param15 = QCheckBox()
        self.chk_param15.clicked.connect(lambda: self.chk15_changed(self.canvas.axes, self.canvas))
        layout_param15.addWidget(self.chk_param15)
        self.lbl_param15 = QLabel('Parameter 1')
        layout_param15.addWidget(self.lbl_param15)
        self.mult_param15 = QLineEdit('1')
        self.mult_param15.setFixedWidth(50)
        self.mult_param15.returnPressed.connect(lambda: self.mult15_changed(self.canvas.axes, self.canvas))
        layout_param15.addWidget(self.mult_param15)
        self.off_param15 = QLineEdit('0')
        self.off_param15.setFixedWidth(50)
        self.off_param15.returnPressed.connect(lambda: self.mult15_changed(self.canvas.axes, self.canvas))
        layout_param15.addWidget(self.off_param15)
        layout_right.addLayout(layout_param15) 
                
        # Construct main window layout
        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_right)
        
        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        
        btn_fileOpen.clicked.connect(lambda: self.openFileNameDialog(self.canvas.axes))
        
    def openFileNameDialog(self, axes):
        options = QFileDialog.Options()
        # Let's use the Native dialog as it is easier for the user
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open a DryICE logfile", "","tdms files (*.tdms);;All files (*)", options=options)
        if fileName:
            self.filename = fileName
            self.file_path.setText(self.filename)
        # Check if filename also has a corresponding .csv file - if so, the file is converted and can be loaded directly
        if not os.path.isfile(self.filename.split('.')[0] + '.csv'):
            # Convert data first, then parse
            self.lblStart.setText('Converting file to csv...')
            self.lblEnd.setText('This may take up to 30s.')
            self.convertData(self.filename)
        # Load data
        self.data = parse_data(self.filename.split('.')[0] + '.csv')
        axes.clear()
        # Plot only 'useful' columns
        xdata = self.data[1].data / 3600
        self.line1 = axes.plot(xdata, self.data[2].data, label=self.data[2].name, color='tab:red')
        self.line2 = axes.plot(xdata, self.data[3].data, label=self.data[3].name, color='tab:orange')
        self.line3 = axes.plot(xdata, self.data[4].data, label=self.data[4].name, color='black')
        self.line4 = axes.plot(xdata, self.data[5].data, label=self.data[5].name, color='tab:blue')
        self.line5 = axes.plot(xdata, self.data[6].data, label=self.data[6].name, color='tab:pink')
        self.line6 = axes.plot(xdata, self.data[7].data, label=self.data[7].name, color='tab:olive')
        self.line7 = axes.plot(xdata, self.data[8].data, label=self.data[8].name, color='tab:purple')
        self.line8 = axes.plot(xdata, self.data[9].data, label=self.data[9].name, color='tab:cyan')
        self.line9 = axes.plot(xdata, self.data[18].data, label=self.data[18].name, color='red', linestyle=':')
        self.line10 = axes.plot(xdata, self.data[19].data, label=self.data[19].name, color='tab:red', linestyle=':')
        self.line11 = axes.plot(xdata, self.data[20].data, label=self.data[20].name, color='green', linestyle='-')
        self.line12 = axes.plot(xdata, self.data[21].data, label=self.data[21].name, color='tab:green', linestyle='-')
        self.line13 = axes.plot(xdata, self.data[22].data, label=self.data[22].name, color='xkcd:lilac', linestyle='-.')
        self.line14 = axes.plot(xdata, self.data[23].data, label=self.data[23].name, color='xkcd:violet', linestyle='-.')
        self.line15 = axes.plot(xdata, self.data[24].data, label=self.data[24].name, color='xkcd:indigo', linestyle='-.')
        axes.legend()
        axes.set_xlabel('$t$ (hours) since "First point"')
        # Set checkboxes to ticked
        self.chk_param1.setCheckState(Qt.Checked)
        self.chk_param2.setCheckState(Qt.Checked)
        self.chk_param3.setCheckState(Qt.Checked)
        self.chk_param4.setCheckState(Qt.Checked)
        self.chk_param5.setCheckState(Qt.Checked)
        self.chk_param6.setCheckState(Qt.Checked)
        self.chk_param7.setCheckState(Qt.Checked)
        self.chk_param8.setCheckState(Qt.Checked)
        self.chk_param9.setCheckState(Qt.Checked)
        self.chk_param10.setCheckState(Qt.Checked)
        self.chk_param11.setCheckState(Qt.Checked)
        self.chk_param12.setCheckState(Qt.Checked)
        self.chk_param13.setCheckState(Qt.Checked)
        self.chk_param14.setCheckState(Qt.Checked)
        self.chk_param15.setCheckState(Qt.Checked)
        # Don't plot lines which only contain zeros
        line1_unique = np.unique(self.data[2].data)
        if len(line1_unique) == 1 and line1_unique[0] == 0.0:
            self.chk_param1.setCheckState(Qt.Unchecked)
            self.chk1_changed(self.canvas.axes, self.canvas)
        line2_unique = np.unique(self.data[3].data)
        if len(line2_unique) == 1 and line2_unique[0] == 0.0:
            self.chk_param2.setCheckState(Qt.Unchecked)
            self.chk2_changed(self.canvas.axes, self.canvas)
        line3_unique = np.unique(self.data[4].data)
        if len(line3_unique) == 1 and line3_unique[0] == 0.0:
            self.chk_param3.setCheckState(Qt.Unchecked)
            self.chk3_changed(self.canvas.axes, self.canvas)            
        line4_unique = np.unique(self.data[5].data)
        if len(line4_unique) == 1 and line4_unique[0] == 0.0:
            self.chk_param4.setCheckState(Qt.Unchecked)
            self.chk4_changed(self.canvas.axes, self.canvas)
        line5_unique = np.unique(self.data[6].data)
        if len(line5_unique) == 1 and line5_unique[0] == 0.0:
            self.chk_param5.setCheckState(Qt.Unchecked)
            self.chk5_changed(self.canvas.axes, self.canvas)
        line6_unique = np.unique(self.data[7].data)
        if len(line6_unique) == 1 and line6_unique[0] == 0.0:
            self.chk_param6.setCheckState(Qt.Unchecked)
            self.chk6_changed(self.canvas.axes, self.canvas)
        line7_unique = np.unique(self.data[8].data)
        if len(line7_unique) == 1 and line7_unique[0] == 0.0:
            self.chk_param7.setCheckState(Qt.Unchecked)
            self.chk7_changed(self.canvas.axes, self.canvas)
        line8_unique = np.unique(self.data[9].data)
        if len(line8_unique) == 1 and line8_unique[0] == 0.0:
            self.chk_param8.setCheckState(Qt.Unchecked)
            self.chk8_changed(self.canvas.axes, self.canvas)
        line9_unique = np.unique(self.data[18].data)
        if len(line9_unique) == 1 and line9_unique[0] == 0.0:
            self.chk_param9.setCheckState(Qt.Unchecked)
            self.chk9_changed(self.canvas.axes, self.canvas)
        line10_unique = np.unique(self.data[19].data)
        if len(line10_unique) == 1 and line10_unique[0] == 0.0:
            self.chk_param10.setCheckState(Qt.Unchecked)
            self.chk10_changed(self.canvas.axes, self.canvas)
        line11_unique = np.unique(self.data[20].data)
        if len(line11_unique) == 1 and line11_unique[0] == 0.0:
            self.chk_param11.setCheckState(Qt.Unchecked)
            self.chk11_changed(self.canvas.axes, self.canvas)
        line12_unique = np.unique(self.data[21].data)
        if len(line12_unique) == 1 and line12_unique[0] == 0.0:
            self.chk_param12.setCheckState(Qt.Unchecked)
            self.chk12_changed(self.canvas.axes, self.canvas)
        line13_unique = np.unique(self.data[22].data)
        if len(line13_unique) == 1 and line13_unique[0] == 0.0:
            self.chk_param13.setCheckState(Qt.Unchecked)
            self.chk13_changed(self.canvas.axes, self.canvas)
        line14_unique = np.unique(self.data[23].data)
        if len(line14_unique) == 1 and line14_unique[0] == 0.0:
            self.chk_param14.setCheckState(Qt.Unchecked)
            self.chk14_changed(self.canvas.axes, self.canvas)
        line15_unique = np.unique(self.data[24].data)
        if len(line15_unique) == 1 and line15_unique[0] == 0.0:
            self.chk_param15.setCheckState(Qt.Unchecked)
            self.chk15_changed(self.canvas.axes, self.canvas)            
        # Update labels
        self.lblStart.setText('First point: ' + datetime.datetime.fromtimestamp(self.data[0].data[0]).strftime('%Y-%m-%d %H:%M:%S'))
        self.lblEnd.setText('Last point: ' + datetime.datetime.fromtimestamp(self.data[0].data[-1]).strftime('%Y-%m-%d %H:%M:%S'))
        # Update labels of parameters
        self.lbl_param1.setText(self.data[2].name)
        self.lbl_param2.setText(self.data[3].name)
        self.lbl_param3.setText(self.data[4].name)
        self.lbl_param4.setText(self.data[5].name)
        self.lbl_param5.setText(self.data[6].name)
        self.lbl_param6.setText(self.data[7].name)
        self.lbl_param7.setText(self.data[8].name)
        self.lbl_param8.setText(self.data[9].name)
        self.lbl_param9.setText(self.data[18].name)
        self.lbl_param10.setText(self.data[19].name)
        self.lbl_param11.setText(self.data[20].name)
        self.lbl_param12.setText(self.data[21].name)
        self.lbl_param13.setText(self.data[22].name)
        self.lbl_param14.setText(self.data[23].name)
        self.lbl_param15.setText(self.data[24].name)
                
    def chk1_changed(self, axes, canvas):
        if self.chk_param1.checkState() == Qt.Checked:
            axes.lines[0].set_alpha(1)
            axes.lines[0].set_label(self.data[2].name)
        else:
            axes.lines[0].set_alpha(0)
            axes.lines[0].set_label('')
        axes.legend()
        canvas.draw_idle()
            
    def chk2_changed(self, axes, canvas):
        if self.chk_param2.checkState() == Qt.Checked:
            axes.lines[1].set_alpha(1)
            axes.lines[1].set_label(self.data[3].name)
        else:
            axes.lines[1].set_alpha(0)
            axes.lines[1].set_label('')
        axes.legend()    
        canvas.draw_idle()

    def chk3_changed(self, axes, canvas):
        if self.chk_param3.checkState() == Qt.Checked:
            axes.lines[2].set_alpha(1)
            axes.lines[2].set_label(self.data[4].name)
        else:
            axes.lines[2].set_alpha(0)
            axes.lines[2].set_label('')
        axes.legend()
        canvas.draw_idle()
            
    def chk4_changed(self, axes, canvas):
        if self.chk_param4.checkState() == Qt.Checked:
            axes.lines[3].set_alpha(1)
            axes.lines[3].set_label(self.data[5].name)
        else:
            axes.lines[3].set_alpha(0)
            axes.lines[3].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk5_changed(self, axes, canvas):
        if self.chk_param5.checkState() == Qt.Checked:
            axes.lines[4].set_alpha(1)
            axes.lines[4].set_label(self.data[6].name)
        else:
            axes.lines[4].set_alpha(0)
            axes.lines[4].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk6_changed(self, axes, canvas):
        if self.chk_param6.checkState() == Qt.Checked:
            axes.lines[5].set_alpha(1)
            axes.lines[5].set_label(self.data[7].name)
        else:
            axes.lines[5].set_alpha(0)
            axes.lines[5].set_label('')
        axes.legend()
        canvas.draw_idle()
            
    def chk7_changed(self, axes, canvas):
        if self.chk_param7.checkState() == Qt.Checked:
            axes.lines[6].set_alpha(1)
            axes.lines[6].set_label(self.data[8].name)
        else:
            axes.lines[6].set_alpha(0)
            axes.lines[6].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk8_changed(self, axes, canvas):
        if self.chk_param8.checkState() == Qt.Checked:
            axes.lines[7].set_alpha(1)
            axes.lines[7].set_label(self.data[9].name)
        else:
            axes.lines[7].set_alpha(0)
            axes.lines[7].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk9_changed(self, axes, canvas):
        if self.chk_param9.checkState() == Qt.Checked:
            axes.lines[8].set_alpha(1)
            axes.lines[8].set_label(self.data[18].name)
        else:
            axes.lines[8].set_alpha(0)
            axes.lines[8].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk10_changed(self, axes, canvas):
        if self.chk_param10.checkState() == Qt.Checked:
            axes.lines[9].set_alpha(1)
            axes.lines[9].set_label(self.data[19].name)
        else:
            axes.lines[9].set_alpha(0)
            axes.lines[9].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk11_changed(self, axes, canvas):
        if self.chk_param11.checkState() == Qt.Checked:
            axes.lines[10].set_alpha(1)
            axes.lines[10].set_label(self.data[20].name)
        else:
            axes.lines[10].set_alpha(0)
            axes.lines[10].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk12_changed(self, axes, canvas):
        if self.chk_param12.checkState() == Qt.Checked:
            axes.lines[11].set_alpha(1)
            axes.lines[11].set_label(self.data[21].name)
        else:
            axes.lines[11].set_alpha(0)
            axes.lines[11].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk13_changed(self, axes, canvas):
        if self.chk_param13.checkState() == Qt.Checked:
            axes.lines[12].set_alpha(1)
            axes.lines[12].set_label(self.data[22].name)
        else:
            axes.lines[12].set_alpha(0)
            axes.lines[12].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk14_changed(self, axes, canvas):
        if self.chk_param14.checkState() == Qt.Checked:
            axes.lines[13].set_alpha(1)
            axes.lines[13].set_label(self.data[23].name)
        else:
            axes.lines[13].set_alpha(0)
            axes.lines[13].set_label('')
        axes.legend()
        canvas.draw_idle()

    def chk15_changed(self, axes, canvas):
        if self.chk_param15.checkState() == Qt.Checked:
            axes.lines[14].set_alpha(1)
            axes.lines[14].set_label(self.data[24].name)
        else:
            axes.lines[14].set_alpha(0)
            axes.lines[14].set_label('')
        axes.legend()
        canvas.draw_idle()
        
    def mult1_changed(self, axes, canvas):
        mult_factor = float(self.mult_param1.text())
        off_factor = float(self.off_param1.text())
        axes.lines[0].set_ydata(self.data[2].data*mult_factor + off_factor)
        axes.lines[0].set_label(self.data[2].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult2_changed(self, axes, canvas):
        mult_factor = float(self.mult_param2.text())
        off_factor = float(self.off_param2.text())
        axes.lines[1].set_ydata(self.data[3].data*mult_factor + off_factor)
        axes.lines[1].set_label(self.data[3].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()
        
    def mult3_changed(self, axes, canvas):
        mult_factor = float(self.mult_param3.text())
        off_factor = float(self.off_param3.text())
        axes.lines[2].set_ydata(self.data[4].data*mult_factor + off_factor)
        axes.lines[2].set_label(self.data[4].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()
        
    def mult4_changed(self, axes, canvas):
        mult_factor = float(self.mult_param4.text())
        off_factor = float(self.off_param4.text())
        axes.lines[3].set_ydata(self.data[5].data*mult_factor + off_factor)
        axes.lines[3].set_label(self.data[5].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult5_changed(self, axes, canvas):
        mult_factor = float(self.mult_param5.text())
        off_factor = float(self.off_param5.text())
        axes.lines[4].set_ydata(self.data[6].data*mult_factor + off_factor)        
        axes.lines[4].set_label(self.data[6].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult6_changed(self, axes, canvas):
        mult_factor = float(self.mult_param6.text())
        off_factor = float(self.off_param6.text())
        axes.lines[5].set_ydata(self.data[7].data*mult_factor + off_factor)
        axes.lines[5].set_label(self.data[7].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult7_changed(self, axes, canvas):
        mult_factor = float(self.mult_param7.text())
        off_factor = float(self.off_param7.text())
        axes.lines[6].set_ydata(self.data[8].data*mult_factor + off_factor)
        axes.lines[6].set_label(self.data[8].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult8_changed(self, axes, canvas):
        mult_factor = float(self.mult_param8.text())
        off_factor = float(self.off_param8.text())
        axes.lines[7].set_ydata(self.data[9].data*mult_factor + off_factor)
        axes.lines[7].set_label(self.data[9].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult9_changed(self, axes, canvas):
        mult_factor = float(self.mult_param9.text())
        off_factor = float(self.off_param9.text())
        axes.lines[8].set_ydata(self.data[18].data*mult_factor + off_factor)
        axes.lines[8].set_label(self.data[18].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult10_changed(self, axes, canvas):
        mult_factor = float(self.mult_param10.text())
        off_factor = float(self.off_param10.text())
        axes.lines[9].set_ydata(self.data[19].data*mult_factor + off_factor)
        axes.lines[9].set_label(self.data[19].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult11_changed(self, axes, canvas):
        mult_factor = float(self.mult_param11.text())
        off_factor = float(self.off_param11.text())
        axes.lines[10].set_ydata(self.data[20].data*mult_factor + off_factor)
        axes.lines[10].set_label(self.data[20].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult12_changed(self, axes, canvas):
        mult_factor = float(self.mult_param12.text())
        off_factor = float(self.off_param12.text())
        axes.lines[11].set_ydata(self.data[21].data*mult_factor + off_factor)
        axes.lines[11].set_label(self.data[21].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult13_changed(self, axes, canvas):
        mult_factor = float(self.mult_param13.text())
        off_factor = float(self.off_param13.text())
        axes.lines[12].set_ydata(self.data[22].data*mult_factor + off_factor)
        axes.lines[12].set_label(self.data[22].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult4_changed(self, axes, canvas):
        mult_factor = float(self.mult_param14.text())
        off_factor = float(self.off_param14.text())
        axes.lines[13].set_ydata(self.data[23].data*mult_factor + off_factor)
        axes.lines[13].set_label(self.data[23].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()

    def mult15_changed(self, axes, canvas):
        mult_factor = float(self.mult_param15.text())
        off_factor = float(self.off_param15.text())
        axes.lines[14].set_ydata(self.data[24].data*mult_factor + off_factor)
        axes.lines[14].set_label(self.data[24].name + ' $\\times$' + str(mult_factor) + ' + ' + str(off_factor))
        axes.legend()
        canvas.draw_idle()
        
            
    def convertData(self, measfile):
        from nptdms import TdmsFile # pip install npTDMS
        from datetime import datetime
        tdms_file = TdmsFile.read(measfile)
        # Build header
        header = []
        measdata = np.array([])

        for group in tdms_file.groups():
            group_name = group.name

            for channel in group.channels():
                if len(header) == 0: # First column
                    header = channel.name
                    measdata = np.array(channel[:])
                else:
                    header = header + ', ' + channel.name
                    measdata = np.vstack((measdata, np.array(channel[:])))

        measdata = measdata.T

        with open( measfile.split('.')[0] + '.csv', 'w') as f:
            dtm = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            f.write(dtm + '\n')
            f.write('Data converted from DryICE file: ' + measfile + '\n')
            f.write(header + '\n')
            for i in range(np.size(measdata, 0)):
                datastr = np.array2string(measdata[i,:], separator=',')[1:-1].replace('\n','')
                f.write(datastr + '\n')
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
