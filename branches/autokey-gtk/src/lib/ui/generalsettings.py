#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from uic/generalsettings.ui on Sat Aug  1 00:25:41 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 444)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.promptToSaveCheckbox = QtGui.QCheckBox(self.groupBox)
        self.promptToSaveCheckbox.setObjectName("promptToSaveCheckbox")
        self.verticalLayout.addWidget(self.promptToSaveCheckbox)
        self.showTrayCheckbox = QtGui.QCheckBox(self.groupBox)
        self.showTrayCheckbox.setObjectName("showTrayCheckbox")
        self.verticalLayout.addWidget(self.showTrayCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.allowKbNavCheckbox = QtGui.QCheckBox(self.groupBox_2)
        self.allowKbNavCheckbox.setObjectName("allowKbNavCheckbox")
        self.verticalLayout_2.addWidget(self.allowKbNavCheckbox)
        self.sortByUsageCheckbox = QtGui.QCheckBox(self.groupBox_2)
        self.sortByUsageCheckbox.setObjectName("sortByUsageCheckbox")
        self.verticalLayout_2.addWidget(self.sortByUsageCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enableUndoCheckbox = QtGui.QCheckBox(self.groupBox_3)
        self.enableUndoCheckbox.setObjectName("enableUndoCheckbox")
        self.verticalLayout_3.addWidget(self.enableUndoCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n("Form"))
        self.groupBox.setTitle(kdecore.i18n("Main Window"))
        self.promptToSaveCheckbox.setText(kdecore.i18n("Prompt for unsaved changes"))
        self.showTrayCheckbox.setText(kdecore.i18n("Show a tray icon (requires restart)"))
        self.groupBox_2.setTitle(kdecore.i18n("Popup Menu"))
        self.allowKbNavCheckbox.setText(kdecore.i18n("Allow keyboard navigation of popup menu"))
        self.sortByUsageCheckbox.setText(kdecore.i18n("Sort menu items with most frequently used first"))
        self.groupBox_3.setTitle(kdecore.i18n("Expansions"))
        self.enableUndoCheckbox.setText(kdecore.i18n("Enable undo by pressing backspace"))

