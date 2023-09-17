# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(849, 568)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StrongBodyLabel = StrongBodyLabel(parent=Dialog)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.horizontalLayout.addWidget(self.StrongBodyLabel)
        self.ProgressBar = ProgressBar(parent=Dialog)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout.addWidget(self.ProgressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StrongBodyLabel_2 = StrongBodyLabel(parent=Dialog)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.horizontalLayout_2.addWidget(self.StrongBodyLabel_2)
        self.ProgressBar_2 = ProgressBar(parent=Dialog)
        self.ProgressBar_2.setObjectName("ProgressBar_2")
        self.horizontalLayout_2.addWidget(self.ProgressBar_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tableview = QtWidgets.QTableView(parent=Dialog)
        self.tableview.setObjectName("tableview")
        self.gridLayout.addWidget(self.tableview, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(160, 80, 181, 357))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pt_up = PushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pt_up.sizePolicy().hasHeightForWidth())
        self.pt_up.setSizePolicy(sizePolicy)
        self.pt_up.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pt_up.setStyleSheet("\"border:none;\"")
        self.pt_up.setFlat(True)
        self.pt_up.setObjectName("pt_up")
        self.verticalLayout_2.addWidget(self.pt_up)
        self.pt_down = PushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pt_down.sizePolicy().hasHeightForWidth())
        self.pt_down.setSizePolicy(sizePolicy)
        self.pt_down.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pt_down.setStyleSheet("\"border:none;\"")
        self.pt_down.setFlat(True)
        self.pt_down.setObjectName("pt_down")
        self.verticalLayout_2.addWidget(self.pt_down)
        self.m_pSearchLineEdit = LineEdit(parent=self.frame)
        self.m_pSearchLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.m_pSearchLineEdit.setToolTip("")
        self.m_pSearchLineEdit.setStyleSheet("")
        self.m_pSearchLineEdit.setText("")
        self.m_pSearchLineEdit.setObjectName("m_pSearchLineEdit")
        self.verticalLayout_2.addWidget(self.m_pSearchLineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.TreeWidget = TreeWidget(parent=self.frame)
        self.TreeWidget.setObjectName("TreeWidget")
        self.TreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.TreeWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pt_ok = PushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pt_ok.sizePolicy().hasHeightForWidth())
        self.pt_ok.setSizePolicy(sizePolicy)
        self.pt_ok.setStyleSheet("")
        self.pt_ok.setFlat(False)
        self.pt_ok.setObjectName("pt_ok")
        self.horizontalLayout_3.addWidget(self.pt_ok)
        self.pt_close = PushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pt_close.sizePolicy().hasHeightForWidth())
        self.pt_close.setSizePolicy(sizePolicy)
        self.pt_close.setStyleSheet("")
        self.pt_close.setFlat(False)
        self.pt_close.setObjectName("pt_close")
        self.horizontalLayout_3.addWidget(self.pt_close)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tableview.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.StrongBodyLabel.setText(_translate("Dialog", "当前文件进度"))
        self.StrongBodyLabel_2.setText(_translate("Dialog", "文件总进度"))
        self.pt_up.setText(_translate("Dialog", "升序"))
        self.pt_down.setText(_translate("Dialog", "降序"))
        self.pt_ok.setText(_translate("Dialog", "确定"))
        self.pt_close.setText(_translate("Dialog", "取消"))
from qfluentwidgets import LineEdit, ProgressBar, PushButton, StrongBodyLabel, TreeWidget
