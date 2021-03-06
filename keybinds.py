# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keybinds.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(420, 120)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(420, 120))
        MainWindow.setMaximumSize(QtCore.QSize(420, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 80, 261, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.stop_button.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontalLayout.addWidget(self.stop_button)
        self.skills_label = QtGui.QLabel(self.centralwidget)
        self.skills_label.setGeometry(QtCore.QRect(10, 10, 401, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.skills_label.setFont(font)
        self.skills_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.skills_label.setAutoFillBackground(False)
        self.skills_label.setStyleSheet(_fromUtf8("background: lightblue"))
        self.skills_label.setFrameShape(QtGui.QFrame.Box)
        self.skills_label.setFrameShadow(QtGui.QFrame.Plain)
        self.skills_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.skills_label.setObjectName(_fromUtf8("skills_label"))
        self.hits_label = QtGui.QLabel(self.centralwidget)
        self.hits_label.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.hits_label.setAutoFillBackground(False)
        self.hits_label.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.hits_label.setFrameShape(QtGui.QFrame.Box)
        self.hits_label.setLineWidth(1)
        self.hits_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hits_label.setObjectName(_fromUtf8("hits_label"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(174, 50, 241, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.reaction_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.reaction_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reaction_label.setAutoFillBackground(False)
        self.reaction_label.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.reaction_label.setText(_fromUtf8(""))
        self.reaction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reaction_label.setObjectName(_fromUtf8("reaction_label"))
        self.horizontalLayout_2.addWidget(self.reaction_label)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.avg_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.avg_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.avg_label.setAutoFillBackground(False)
        self.avg_label.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.avg_label.setText(_fromUtf8(""))
        self.avg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avg_label.setObjectName(_fromUtf8("avg_label"))
        self.horizontalLayout_2.addWidget(self.avg_label)
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.ratio_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.ratio_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ratio_label.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.ratio_label.setText(_fromUtf8(""))
        self.ratio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ratio_label.setObjectName(_fromUtf8("ratio_label"))
        self.horizontalLayout_2.addWidget(self.ratio_label)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(171, 50, 241, 31))
        self.widget.setStyleSheet(_fromUtf8("background: lightgrey"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.success_label = QtGui.QLabel(self.centralwidget)
        self.success_label.setGeometry(QtCore.QRect(10, 90, 151, 21))
        self.success_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.success_label.setStyleSheet(_fromUtf8("background:pink"))
        self.success_label.setFrameShape(QtGui.QFrame.Box)
        self.success_label.setText(_fromUtf8(""))
        self.success_label.setAlignment(QtCore.Qt.AlignCenter)
        self.success_label.setObjectName(_fromUtf8("success_label"))
        self.user_input = QtGui.QLabel(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(80, 50, 81, 31))
        self.user_input.setAutoFillBackground(False)
        self.user_input.setStyleSheet(_fromUtf8("background: white"))
        self.user_input.setFrameShape(QtGui.QFrame.Box)
        self.user_input.setFrameShadow(QtGui.QFrame.Sunken)
        self.user_input.setLineWidth(1)
        self.user_input.setText(_fromUtf8(""))
        self.user_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_input.setObjectName(_fromUtf8("user_input"))
        self.widget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.skills_label.raise_()
        self.hits_label.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.success_label.raise_()
        self.user_input.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSet_keybinds = QtGui.QAction(MainWindow)
        self.actionSet_keybinds.setObjectName(_fromUtf8("actionSet_keybinds"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Keybinding Practice", None))
        self.start_button.setText(_translate("MainWindow", "Start", None))
        self.stop_button.setText(_translate("MainWindow", "Stop", None))
        self.skills_label.setText(_translate("MainWindow", "Target 6 with an Obviously Too Long Skill Name!", None))
        self.hits_label.setText(_translate("MainWindow", "Hits:", None))
        self.label_4.setText(_translate("MainWindow", "Reaction:", None))
        self.label_3.setText(_translate("MainWindow", "Avg:", None))
        self.label_7.setText(_translate("MainWindow", "Ratio:", None))
        self.actionSet_keybinds.setText(_translate("MainWindow", "Set keybinds", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

