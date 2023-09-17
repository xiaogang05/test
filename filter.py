import sys

from PyQt6.QtGui import QCursor, QIcon, QStandardItemModel, QStandardItem, QPalette, QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QTableWidgetItem, QListWidgetItem, QCheckBox,
                             QAbstractItemView, QHeaderView, QMenu, QListWidget, QPushButton, QLineEdit, QHBoxLayout,
                             QMessageBox, QTreeView, QDialog, QToolButton, QTreeWidgetItem)
from PyQt6.QtCore import QPoint, Qt, QSize, pyqtSlot
from qfluentwidgets import PushButton, SplitPushButton, PrimarySplitToolButton, DropDownPushButton, DropDownToolButton, \
    ComboBox

import dialog_shaix
import main


#
# class MYQdialog(QDialog):
#     def __init__(self, parent=None):
#         super(QDialog, self).__init__(parent)
#         self.m_map = dict()
#         self.english_name = None
#         self.ui = dialog_shaix.Ui_Dialog()
#         self.ui.setupUi(self)
#
#         self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
#         self.setStyleSheet("background-color: white;")
#         self.ui.m_pSearchLineEdit.setPlaceholderText("搜索")
#
#         self.inittreeview()
#         self.ui.treeview.setHeaderHidden(True)
#         self.ui.treeview.expandAll()
#
#         self.ui.m_pSearchLineEdit.textChanged.connect(self.on_text_changed)
#         self.ui.pt_up.clicked.connect(self.pt_up_clicked)
#         self.ui.pt_down.clicked.connect(self.pt_down_clicked)
#         self.ui.pt_ok.clicked.connect(self.pt_ok_clicked)
#         self.ui.pt_close.clicked.connect(self.pt_close_clicked)
#
#     @pyqtSlot(str)
#     def on_text_changed(self, text):
#         print(text)
#
#     def inittreeview(self):
#         model = QStandardItemModel(self.ui.treeview)
#         first = QStandardItem("全选")
#         model.appendRow(first)
#         first.setCheckable(True)
#         first.setAutoTristate(True)
#
#         if self.english_name != '':
#             for i in self.m_map.keys():
#                 section = QStandardItem(self.m_map.keys())
#                 section.setCheckable(True)
#                 first.appendRow(section)
#                 first.setChild(section.index().row(), 0, section)
#
#         model.itemChanged.connect(self.treeItemChanged)
#         self.ui.treeview.setModel(model)
#         first.setCheckable(True)
#
#     def treeItemChanged(self, item: QStandardItem):  # 有变化时进行触发
#         if item == '':
#             return
#         if item.isCheckable():
#             state = item.checkState()
#             if item.isAutoTristate():
#                 if state != Qt.PartiallyChecked:
#                     self.treeItem_checkAllChild(item, state)
#
#     def treeItem_checkAllChild(self, item: QStandardItem, check: bool):
#         if item == '':
#             return
#         rowCount = item.rowCount()
#         for i in range(0, rowCount):
#             childItems = item.child(i)
#             self.treeItem_checkAllChild_recursion(childItems, check)
#         if item.isCheckable():
#             item.setCheckable(check)
#         pass
#
#
#
#     def treeItemChanged(self):
#         pass
#
#     def pt_up_clicked(self):
#         pass
#
#     def pt_down_clicked(self):
#         pass
#
#     def pt_ok_clicked(self):
#         self.close()
#         pass
#
#     def pt_close_clicked(self):
#         self.close()
#

class Mymainwindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.cnt = 0
        self.ui = main.Ui_Dialog()
        self.ui.setupUi(self)
        self.Edit_content = []
        self.checked_data = []
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        # self.setStyleSheet("background-color: white;")

        self.ui.tableview.verticalHeader().hide()
        self.ui.frame.hide()
        self.filter_flag = 0
        self.index = 0
        self.rowC = 0
        # self.ui.TableView.setColumnCount(5)
        # self.ui.TableView.setRowCount(60)

        songInfos = [
            ['かばん', 'aiko', 'かばん', '2004', '5:04'],
            ['爱你', '王心凌', '爱你', '2004', '3:39'],
            ['星のない世界', 'aiko', '星のない世界/横顔', '2007', '5:30'],
            ['横顔', 'aiko', '星のない世界/横顔', '2007', '5:06'],
            ['秘密', 'aiko', '秘密', '2008', '6:27'],
            ['シアワセ', 'aiko', '秘密', '2008', '5:25'],
            ['二人', 'aiko', '二人', '2008', '5:00'],
            ['スパークル', 'RADWIMPS', '君の名は。', '2016', '8:54'],
            ['なんでもないや', 'RADWIMPS', '君の名は。', '2016', '3:16'],
            ['前前前世', 'RADWIMPS', '人間開花', '2016', '4:35'],
            ['恋をしたのは', 'aiko', '恋をしたのは', '2016', '6:02'],
            ['夏バテ', 'aiko', '恋をしたのは', '2016', '4:41'],
            ['もっと', 'aiko', 'もっと', '2016', '4:50'],
            ['問題集', 'aiko', 'もっと', '2016', '4:18'],
            ['半袖', 'aiko', 'もっと', '2016', '5:50'],
            ['ひねくれ', '鎖那', 'Hush a by little girl', '2017', '3:54'],
            ['シュテルン', '鎖那', 'Hush a by little girl', '2017', '3:16'],
            ['愛は勝手', 'aiko', '湿った夏の始まり', '2018', '5:31'],
            ['ドライブモード', 'aiko', '湿った夏の始まり', '2018', '3:37'],
            ['うん。', 'aiko', '湿った夏の始まり', '2018', '5:48'],
            ['キラキラ', 'aikoの詩。', '2019', '5:08', 'aiko'],
            ['恋のスーパーボール', 'aiko', 'aikoの詩。', '2019', '4:31'],
            ['磁石', 'aiko', 'どうしたって伝えられないから', '2021', '4:24'],
            ['食べた愛', 'aiko', '食べた愛/あたしたち', '2021', '5:17'],
            ['列車', 'aiko', '食べた愛/あたしたち', '2021', '4:18'],
            ['花の塔', 'さユり', '花の塔', '2022', '4:35'],
            ['夏恋のライフ', 'aiko', '夏恋のライフ', '2022', '5:03'],
            ['あかときリロード', 'aiko', 'あかときリロード', '2023', '4:04'],
            ['荒れた唇は恋を失くす', 'aiko', '今の二人をお互いが見てる', '2023', '4:07'],
            ['ワンツースリー', 'aiko', '今の二人をお互いが見てる', '2023', '4:47'],
        ]
        songInfos += songInfos

        self.m_model = QStandardItemModel()

        strheader = [self.tr('Title'), self.tr('Artist'), self.tr('Album'),
                     self.tr('Year'), self.tr('Duration')]

        self.m_model.setHorizontalHeaderLabels(strheader)
        self.ui.tableview.setModel(self.m_model)

        # self._headView = self.ui.tableview.horizontalHeader()
        # self._headButton = DropDownPushButton(strheader[0], self._headView)
        # self._headView.setIndexWidget(self.m_model.index(0, 0), self._headButton)
        # self._headButton.resize(90, 23)
        # self._headView.sectionResized.connect(self.onModelIndexResize)

        self.ui.tableview.horizontalHeader().setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableview.horizontalHeader().customContextMenuRequested.connect(self.right_menu)

        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.m_model.setItem(i, j, QStandardItem(songInfo[j]))

        self.ui.m_pSearchLineEdit.setPlaceholderText("搜索")

        self.ui.TreeWidget.setHeaderHidden(True)
        self.ui.TreeWidget.expandAll()

        self.ui.m_pSearchLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.pt_up.clicked.connect(self.pt_up_clicked)
        self.ui.pt_down.clicked.connect(self.pt_down_clicked)
        self.ui.pt_ok.clicked.connect(self.pt_ok_clicked)
        self.ui.pt_close.clicked.connect(self.pt_close_clicked)
        self.ui.TreeWidget.itemChanged.connect(self.tree_item_change)
        # self.ui.TreeWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

    def onModelIndexResize(self, logicalIndex, oldSize, newSize):
        # // 只对表头第一个单元格的控件进行改变，所以判断一下下标
        if logicalIndex == 0:
            #// 控件的大小可由自己设计
            self._headButton.resize(newSize, 23)

    @pyqtSlot(str)
    def on_text_changed(self, text):
        # print(text)
        self.checked_data.clear()
        self.filter(text)

    def filter(self, text):
        top_count = self.ui.TreeWidget.topLevelItemCount()
        self.filter_flag = 1

        for row in range(0, top_count):
            item = self.ui.TreeWidget.topLevelItem(row)  # 循环获取根节点
            if item is not None:
                item_text = item.text(0)  # 根节点文字信息（默认一列）
                if text in item_text or item_text == "全选":
                    print("show:{t}".format(t=item_text))
                    item.setHidden(False)
                    item.setCheckState(0, Qt.CheckState.Checked)
                    # self.ui.treeview.setRowHidden(row, False)
                else:
                    Index = self.ui.TreeWidget.indexFromItem(item, 0)
                    item.setHidden(True)
                    item.setCheckState(0, Qt.CheckState.Unchecked)
                    # print("hide:{t},Index{ind}".format(t=item_text, ind=Index))
        pass
        self.filter_flag = 0

    def init_tree(self):
        item = QTreeWidgetItem([self.tr("全选")])
        item.setCheckState(0, Qt.CheckState.Checked)
        self.ui.TreeWidget.addTopLevelItem(item)
        for str1 in self.Edit_content:
            section = QTreeWidgetItem([self.tr(str1)])
            section.setCheckState(0, Qt.CheckState.Checked)
            self.ui.TreeWidget.addTopLevelItem(section)

        self.Edit_content.clear()

    def remove_tree(self):
        top_count = self.ui.TreeWidget.topLevelItemCount()

        for row in range(0, top_count):
            self.ui.TreeWidget.takeTopLevelItem(0)  # 循环获取根节点

    def get_row_data(self):
        for i in range(0, self.rowC):
            text = self.m_model.item(i, self.index).text()
            if text not in self.Edit_content:
                self.Edit_content.append(text)

    def right_menu(self, pos):
        self.index = self.ui.tableview.columnAt(pos.x())
        self.rowC = self.m_model.rowCount()
        self.get_row_data()
        self.remove_tree()
        self.init_tree()
        self.ui.frame.move(pos)
        self.ui.frame.show()

    def select_all_visiable(self):
        top_count = self.ui.TreeWidget.topLevelItemCount()

        for row in range(0, top_count):
            item = self.ui.TreeWidget.topLevelItem(row)  # 循环获取根节点
            if item is not None:
                hidden_state = item.isHidden()
                check_state = item.checkState(0)
                if not hidden_state and check_state == Qt.CheckState.Unchecked:
                    item.setCheckState(0, Qt.CheckState.Checked)
                    print(item.text(0), hidden_state, check_state)

    def tree_item_change(self, item, colum):
        if item is not None:
            item_text = item.text(colum)
            hidden_state = item.isHidden()
            check_state = item.checkState(0)
            self.cnt = self.cnt + 1
            print("cnt:{cnt}:item:{i},hide:{flag},check:{check}".format(cnt=self.cnt, i=item_text, flag=hidden_state,
                                                                        check=check_state))
            if not hidden_state and self.filter_flag == 0:
                if item_text == "全选":
                    if check_state == Qt.CheckState.Checked:
                        self.select_all_visiable()
                else:
                    item = self.ui.TreeWidget.topLevelItem(0)
                    item.setCheckState(0, Qt.CheckState.Unchecked)
                    pass

    def treeItemChanged(self):
        pass

    def pt_up_clicked(self):
        pass

    def pt_down_clicked(self):
        pass

    def get_check_data(self):
        top_count = self.ui.TreeWidget.topLevelItemCount()
        for row in range(0, top_count):
            item = self.ui.TreeWidget.topLevelItem(row)  # 循环获取根节点
            if item is not None:
                item_text = item.text(0)
                hidden_state = item.isHidden()
                check_state = item.checkState(0)
                if not hidden_state and check_state == Qt.CheckState.Checked:
                    self.checked_data.append(item_text)

    def hide_table_rows(self):
        for i in range(0, self.rowC):
            text = self.m_model.item(i, self.index).text()
            if text not in self.checked_data:
                self.ui.tableview.setRowHidden(i, True)
            else:
                self.ui.tableview.setRowHidden(i, False)
        pass

    def pt_ok_clicked(self):
        self.ui.frame.hide()
        self.get_check_data()
        self.hide_table_rows()
        self.ui.m_pSearchLineEdit.clear()
        pass

    def pt_close_clicked(self):
        self.ui.m_pSearchLineEdit.clear()
        self.ui.frame.hide()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = Mymainwindow()
    myDlg.show()
    sys.exit(myapp.exec())
