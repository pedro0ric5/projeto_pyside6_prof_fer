# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPrincVR3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import myrecursos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 667)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.p = QWidget()
        self.p.setObjectName(u"p")
        self.p.setGeometry(QRect(0, 0, 156, 501))
        self.verticalLayout_4 = QVBoxLayout(self.p)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_Home = QPushButton(self.p)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Home)

        self.btn_Cadastrar = QPushButton(self.p)
        self.btn_Cadastrar.setObjectName(u"btn_Cadastrar")
        self.btn_Cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Cadastrar)

        self.btn_Contatos = QPushButton(self.p)
        self.btn_Contatos.setObjectName(u"btn_Contatos")
        self.btn_Contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Contatos)

        self.btn_Sobre = QPushButton(self.p)
        self.btn_Sobre.setObjectName(u"btn_Sobre")
        self.btn_Sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.p, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 156, 501))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.horizontalLayout_2.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_header = QFrame(self.main_container)
        self.frm_header.setObjectName(u"frm_header")
        self.frm_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_Alternar = QPushButton(self.frm_header)
        self.btn_Alternar.setObjectName(u"btn_Alternar")

        self.horizontalLayout_3.addWidget(self.btn_Alternar)

        self.label = QLabel(self.frm_header)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frm_header)

        self.frmMain = QFrame(self.main_container)
        self.frmMain.setObjectName(u"frmMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMain.sizePolicy().hasHeightForWidth())
        self.frmMain.setSizePolicy(sizePolicy)
        self.frmMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frmMain)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.frmMain)
        self.Pages.setObjectName(u"Pages")
        self.pg_Home = QWidget()
        self.pg_Home.setObjectName(u"pg_Home")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_Home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pg_home = QLabel(self.pg_Home)
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.pg_home)

        self.Pages.addWidget(self.pg_Home)
        self.pg_Cadastrar = QWidget()
        self.pg_Cadastrar.setObjectName(u"pg_Cadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.pg_Cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.pg_Cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_9 = QLineEdit(self.frame_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 6, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 3, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 6, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 2)

        self.lineEdit_10 = QLineEdit(self.frame_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 7, 1, 1, 2)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)

        self.pg_cadastrar = QLabel(self.frame_4)
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.pg_cadastrar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.pg_cadastrar, 0, 0, 1, 3)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(100, 16777215))
        self.pushButton_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_4.setAutoRepeatDelay(1100)

        self.verticalLayout_9.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_Cadastrar)
        self.pg_Contatos = QWidget()
        self.pg_Contatos.setObjectName(u"pg_Contatos")
        self.splitter = QSplitter(self.pg_Contatos)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(200, 60, 111, 31))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.splitter.addWidget(self.label_5)
        self.pg_contatos = QLabel(self.splitter)
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.splitter.addWidget(self.pg_contatos)
        self.Pages.addWidget(self.pg_Contatos)
        self.pg_Sobre = QWidget()
        self.pg_Sobre.setObjectName(u"pg_Sobre")
        self.pg_sobre = QLabel(self.pg_Sobre)
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pg_sobre.setGeometry(QRect(20, 90, 431, 311))
        self.pg_sobre.setWordWrap(True)
        self.Pages.addWidget(self.pg_Sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.frmMain)

        self.frm_footer = QFrame(self.main_container)
        self.frm_footer.setObjectName(u"frm_footer")
        self.frm_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frm_footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frm_footer)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Padoka", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_Contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.p), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_Alternar.setText(QCoreApplication.translate("MainWindow", u"Alternar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pg_home.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/MyRecursos/logo_sysdev_240px.png\"/></p></body></html>", None))
        self.pg_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">EMPRESAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/MyRecursos/whatsApp.png\"/></p></body></html>", None))
        self.pg_contatos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>43 96666-6666</p></body></html>", None))
        self.pg_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a name=\"docs-internal-guid-adc67dc7-7fff-d803-fe9a-89a3eacbc3a1\"/><span style=\" font-family:'Century Gothic','sans-serif'; font-size:16pt; color:#ff9900; background-color:transparent;\">E</span><span style=\" font-family:'Century Gothic','sans-serif'; font-size:16pt; color:#ff9900; background-color:transparent;\">ste sistema faz consulta do CNPJ utilizando API da Receita Federal e faz o cadastro em um banco de dados. O objetivo deste sistema \u00e9 ensinar como utilizar Python e o QT para desenvolver aplica\u00e7\u00f5es modernas e funcionais.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Padoka", None))
    # retranslateUi

