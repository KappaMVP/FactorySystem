# pyqt5
from warnings import simplefilter
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from numpy.core.numeric import identity

# qt_ui
from model1_new_0517 import Ui_MainWindow
from databaseview import Ui_Form
from logingui import Ui_Dialog
import datetime

# module
import pymysql
import cv2
import numpy as numpy
import sys
import dlib
import os
import shutil
import time
import numpy as np
import pandas as pd
import skimage.io as io
import csv

# darkflow
import tensorflow as tf
config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(allow_growth=True))
sess = tf.compat.v1.Session(config=config)
from darkflow.net.build import TFNet

# Qrcode
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image, ImageDraw, ImageFont
import imutils

#pyqt feat matplotlib
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# mail
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName, FileType, Disposition)
predictor = dlib.shape_predictor(
    'data/data_dlib/shape_predictor_68_face_landmarks.dat')

detector = dlib.get_frontal_face_detector()
# Dlib Resnet 人脸识别模型，提取 128D 的特征矢量 / Use Dlib resnet50 model to get 128D face descriptor
face_reco_model = dlib.face_recognition_model_v1(
    "data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")
path_images_from_camera = "data/data_faces_from_camera/"

now1 = 0

# 載入模組3-安全帽
options3 = {'model': 'cfg/yolov2-helmet.cfg', 'load': 'bin/yolov2-helmet_final.weights',
            'labels': 'helmet-labels.txt', 'threshold': 0.65, "gpu": 0.8}
tfnet3 = TFNet(options3)

# 載入模組2-口罩
options2 = {'model': 'cfg/yolov2-mask.cfg', 'load': 'bin/yolov2-mask_final.weights',
            'labels': 'mask-labels.txt', 'threshold': 0.65, "gpu": 0.8}
tfnet2 = TFNet(options2)
# 載入模組1
options1 = {'model': 'cfg/yolo.cfg',
            'load': 'bin/yolov2.weights', 'threshold': 0.6, "gpu": 0.8}
tfnet1 = TFNet(options1)



# 框框的顏色
colors = [tuple(255 * numpy.random.rand(3)) for i in range(5)]
strat = True

# han
detector = dlib.get_frontal_face_detector()

# sqlname
namess = ""
connect = pymysql.connect(host='localhost', port=3306,
                          user="root", password="", db="factorysystem")
catch_conn = []
catch_conn.append(connect)

class MainWindow(QtWidgets.QMainWindow):

    # 讀取QRcode資料
    def scan_qrcode(qrcode):
        data = pyzbar.decode(qrcode)
        if data:
            return data

    def __init__(self):
        # setup
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('factory.png'))
        self.pic = QPixmap("ab.png")
        self.pic_2 = QPixmap("abc.jpg")
        self.ui.label_3.setStyleSheet("color:white")
        # ui_title_name
        self.setWindowTitle('FactorySystem')
        self.ui.submit_btn.clicked.connect(self.member_add)
        self.get_face_database_flag=True
        # Button
        self.qrcode_flag = False
        self.ui.io_delete_btn.clicked.connect(self.io_Delete)
        self.ui.score_delete_btn.clicked.connect(self.score_Delete)
        self.ui.close_btn.clicked.connect(self.closeallview)
        self.ui.gen_features_btn.clicked.connect(self.getFeatures)
        self.unknow_flag=False
        # palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QColor(48, 53, 58))
        self.setPalette(palette)

        # Datetime
        self.showtime()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000)

        # camera
        # self.timer2 = QTimer()
        # self.timer2.timeout.connect(self.viewCam)
        # self.controlTimer()

        # dataview
        self.ui.score_table.doubleClicked.connect(self.score_databaseview)
        self.ui.io_table.doubleClicked.connect(self.io_databaseview)

        self.path_photos_from_camera = "data/data_faces_from_camera/"
        self.current_face_dir = ""
        self.font = cv2.FONT_ITALIC

        self.first_unknow = False
        self.existing_faces_cnt = 0
        self.ss_cnt = 0
        self.current_frame_faces_cnt = 0
        self.save_flag = 1
        self.press_n_flag = 0
        self.frame_time = 0
        self.frame_start_time = 0
        self.fps = 0
        self.namess = ""
        self.preKey = ""
        self.closeCam = True
        self.height1 = 0
        self.width1 = 0
        self.hh = 0
        self.ww = 0
        self.num = 0
        self.img_blank_new = []
        self.img_rd_new = []
        self.chineseName = []
        self.dd = []
        self.ct2 = 0
        # self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.tableWidget.clicked.connect(self.taxx)

        # self.clickBtn
        # test
        self.ui.tabWidget.currentChanged['int'].connect(
            self.on_clickbar1)
        self.buttoncheck = QtWidgets.QPushButton('check')
        self.known = []
        self.sqlNameList = []
        self.sqlNameList_dic = {}
        self.sqlUpdate()
        self.feature_known_list = []
        # 存储录入人脸名字 / Save the name of faces in the database
        self.name_known_list = []
        self.current_frame_feature_list = []
        self.current_frame_face_cnt = 0
        self.current_frame_name_position_list = []
        self.current_frame_name_list = []
        self.CsvNameList = []
        self.lossScore = {'nohelmet': 10, 'nomask': 5}
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.viewCam1)
        self.controlTimer()
    
    def return_128d_features(self, path_img):
        img_rd = io.imread(path_img)
        faces = detector(img_rd, 1)

        if len(faces) != 0:
            shape = predictor(img_rd, faces[0])
            face_descriptor = face_reco_model.compute_face_descriptor(
                img_rd, shape)
        else:
            face_descriptor = 0

        return face_descriptor

    def return_features_mean_personX(self, path_faces_personX):
        features_list_personX = []
        photos_list = os.listdir(path_faces_personX)
        if photos_list:
            for i in range(len(photos_list)):

                features_128d = self.return_128d_features(
                    path_faces_personX + "/" + photos_list[i])
                if features_128d == 0:
                    i += 1
                else:
                    features_list_personX.append(features_128d)

        if features_list_personX:
            features_mean_personX = np.array(
                features_list_personX).mean(axis=0)
        else:
            features_mean_personX = np.zeros(128, dtype=int, order='C')
        return features_mean_personX

    def getFeatures(self):
        person_list = os.listdir("data/data_faces_from_camera/")
        person_cnt = len(person_list)

        with open("data/features_all.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for person in range(person_cnt):
                tempa=path_images_from_camera +person_list[person] + str(person + 1)
                features_mean_personX = self.return_features_mean_personX(
                    path_images_from_camera + person_list[person])
                features_mean_personX_list = features_mean_personX.tolist()
                features_mean_personX_list.insert(0, person_list[person])
                writer.writerow(features_mean_personX_list)
            label = QtWidgets.QLabel("已完成特徵提取")
            label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
            self.ui.face_reg_layout.addWidget(label)
            self.sqlUpdate()

    # 寄發扣分通知信
    def sendMail(self, id, picName, loss):
        message = Mail(
            from_email='factorysystem.nkust@gmail.com',
            to_emails=str(self.sqlNameList_dic[id][2]),
            subject='扣分通知信件',
            html_content='員工編號：'+id+'<br>'+'員工姓名：'+str(self.sqlNameList_dic[id][1])+'<br>' +
            '扣分項目：'+loss+'<br>'+'扣除分數：' +
            str(self.lossScore[loss])+'<br>'+'目前總分：' +
            str(self.sqlNameList_dic[id][3])+'<br>'
        )
        # 圖片附件
        with open(picName, 'rb') as f:
            data = f.read()
            f.close()
        encoded_file = base64.b64encode(data).decode()

        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName('當日扣分照片.jpg')
        )
        message.attachment = attachedFile
        # 串接api
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)
        except Exception as e:
            print(e)

    # Tabbar
    def on_clickbar1(self, index):
        if index == 0:
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.viewCam1)
            self.controlTimer()
        elif index == 1:
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.viewCam2)
            self.controlTimer()
        elif index == 2:
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.viewCam4)
            self.controlTimer()
        elif index == 3:
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.viewCam3)
            self.controlTimer()
        elif index == 4:
            cur = catch_conn[0].cursor()
            # 讀取進出紀錄表
            sql = "SELECT * FROM safeidentify"
            cur.execute(sql)
            data = cur.fetchall()
            x = 0
            for i in data:
                row_num = self.ui.score_table.rowCount()
                while(len(data) != row_num):
                    row_num+=1
                    self.ui.score_table.setRowCount(row_num)
                y = 0
                for j in i:
                    item = QtWidgets.QTableWidgetItem(str(data[x][y]))
                    item.setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.score_table.setItem(x, y, item)
                    y += 1
                x += 1
        elif index == 5:
            cur = catch_conn[0].cursor()
            # 讀取進出紀錄表
            sql = "SELECT * FROM face"
            cur.execute(sql)
            data = cur.fetchall()
            x = 0
            for i in data:
                row_num = self.ui.io_table.rowCount()
                while(len(data) != row_num):
                    row_num+=1
                    self.ui.io_table.setRowCount(row_num)
                y = 0
                for j in i:
                    item = QtWidgets.QTableWidgetItem(str(data[x][y]))
                    item.setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.io_table.setItem(x, y, item)
                    y += 1
                x += 1

    def update_fps(self):
        now = time.time()
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

    def get_face_database(self):
        if os.path.exists("data/features_all.csv"):
            self.name_known_list = []
            self.feature_known_list = []
            path_features_known_csv = "data/features_all.csv"
            csv_rd = pd.read_csv(path_features_known_csv, header=None)
            for i in range(csv_rd.shape[0]):
                features_someone_arr = []
                for j in range(1, 129):
                    if csv_rd.iloc[i][j] == '':
                        features_someone_arr.append('0')
                    else:
                        features_someone_arr.append(csv_rd.iloc[i][j])
                self.feature_known_list.append(features_someone_arr)
                if (type(csv_rd.iloc[i][0])==numpy.float64):
                    tempb=int(csv_rd.iloc[i][0])
                    self.name_known_list.append(str(tempb))
                else:
                    self.name_known_list.append(str(csv_rd.iloc[i][0]))

            return 1
        else:
            if (self.get_face_database_flag):
                label = QtWidgets.QLabel("請提取特徵")
                label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
                self.ui.face_layout.insertWidget(0,label)

            self.get_face_database_flag=False
            return 0
  
    # Rec

    #sqlNameList_dic:"C107156110":["C107156110","陳傳翰",email,score]
    def sqlUpdate(self):
        sql = 'select * from member'
        cursor_data = connect.cursor()
        cursor_data.execute(sql)
        self.sqlNameList = cursor_data.fetchall()
        for i in self.sqlNameList:
            tempList = i[0:5:1]
            tempList = tempList+(0, 0,False,False)
            tempList = list(tempList)
            self.sqlNameList_dic.setdefault(i[0], tempList)

    @ staticmethod
    def return_euclidean_distance(feature_1, feature_2):
        feature_1 = np.array(feature_1)
        feature_2 = np.array(feature_2)
        dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
        return dist

    def draw_note_Rec(self, img_rd):
        cv2.putText(img_rd, "Face Recognizer", (20, 40),
                    self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "FPS:   " + str(self.fps.__round__(2)),
                    (20, 100), self.font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Faces: " + str(self.current_frame_face_cnt),
                    (20, 140), self.font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Q: Quit", (20, 450), self.font,
                    0.8, (255, 255, 255), 1, cv2.LINE_AA)

    def draw_note(self, img_rd):
        cv2.putText(img_rd, "Face Register", (20, 40), self.font,
                    1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "FPS:   " + str(self.fps.__round__(2)), (20, 100), self.font, 0.8, (0, 255, 0), 1,
                    cv2.LINE_AA)
        cv2.putText(img_rd, "Faces: " + str(self.current_frame_faces_cnt),
                    (20, 140), self.font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "N:Create new folder", (20, 350),
                    self.font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "S:Save face", (20, 400),
                    self.font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Q:Quit", (20, 450), self.font,
                    0.8, (255, 255, 255), 1, cv2.LINE_AA)

    def draw_name(self, img_rd):
        font = ImageFont.truetype("simsun.ttc", 30)
        img = Image.fromarray(cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        for i in range(len(self.chineseName)):
            draw.text(
                xy=self.current_frame_name_position_list[i], text=self.chineseName[i], font=font)
            img_with_name = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        return img_with_name

    def show_chinese_name(self):
        if self.current_frame_face_cnt >= 1:
            # ["C107156110","C107156120"]
            for i in self.current_frame_name_list:

                if (i != 'unknown'):
                    try:
                        self.chineseName.append(self.sqlNameList_dic[i][1])
                    except Exception as e:
                        print("沒有這個人在資料庫")
                    
                elif(i == 'unknown'):
                    self.chineseName.append("unknown")

    def keyPressEvent(self, event):
        self.preKey = event.text()
        if self.save_flag:
            if event.text() == 's':
                if self.press_n_flag:
                    self.ss_cnt += 1
                    for ii in range(int(self.height1*2)):
                        for jj in range(int(self.width1*2)):
                            self.img_blank_new[ii][jj] = self.img_rd_new[self.dd.top(
                            )-self.hh + ii][self.dd.left()-self.ww + jj]
                    cv2.imwrite(self.current_face_dir + "/img_face_" + str(self.ss_cnt) + ".jpg", self.img_blank_new)
                    tempstr="儲存到："+ str(self.current_face_dir) +"/" + self.namess+"_" + str(self.ss_cnt) + ".jpg"                   
                    label = QtWidgets.QLabel(tempstr)
                    label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
                    self.ui.face_reg_layout.addWidget(label)

                else:
                    label = QtWidgets.QLabel("請先建立人臉資料夾後再按'S'")
                    label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
                    self.ui.face_reg_layout.addWidget(label)

        if event.text() == "q":
            self.closeCam = False

        if event.text() == "r":
            self.closeCam = True
            self.controlTimer()

    # 人臉註冊
    def viewCam1(self):
        ret, img_rd = self.cap.read()
        self.img_rd_new = img_rd.copy()
        faces = detector(img_rd, 0)
        if len(faces) != 0:
            for k, d in enumerate(faces):
                self.dd = d
                self.height1 = (d.bottom() - d.top())
                self.width1 = (d.right() - d.left())
                self.hh = int(self.height1/2)
                self.ww = int(self.width1/2)
                if (d.right()+self.ww) > 948 or (d.bottom()+self.hh > 711) or (d.left()-self.ww < 0) or (d.top()-self.hh < 0):
                    cv2.putText(img_rd, "OUT OF RANGE", (20, 300),
                                self.font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    color_rectangle = (0, 0, 255)
                    self.save_flag = 0
                else:
                    color_rectangle = (255, 255, 255)
                    self.save_flag = 1

                cv2.rectangle(img_rd,
                                tuple(
                                    [d.left() - self.ww, d.top() - self.hh]),
                                tuple([d.right() + self.ww,
                                        d.bottom() + self.hh]),
                                color_rectangle, 2)

                img_blank = np.zeros(
                    (int(self.height1*2), int(self.width1*2), 3), np.uint8)
                self.img_blank_new = img_blank.copy()

        img_rd = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
        height, width, channel = img_rd.shape
        step = channel * width
        self.draw_note(img_rd)
        self.current_frame_faces_cnt = len(faces)
        qImg = QImage(img_rd.data, width, height,
                        step, QImage.Format_RGB888)
        self.ui.face_reg_scr.setPixmap(QPixmap.fromImage(qImg))
        self.update_fps()

    # 臉部辨識
    def viewCam2(self):
        ret, img_rd = self.cap.read()
        if self.get_face_database():
            text = ""
            img_rd_qr = imutils.resize(img_rd)
            barcodes = pyzbar.decode(
                img_rd_qr,  symbols=[ZBarSymbol.QRCODE])
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img_rd_qr, (x, y), (x + w, y + h),
                                (0, 0, 255), 2)

                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                text = barcodeData
                cv2.putText(img_rd, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            faces = detector(img_rd, 0)
            self.draw_note_Rec(img_rd)
            self.current_frame_feature_list = []
            self.current_frame_face_cnt = 0
            self.current_frame_name_position_list = []
            self.current_frame_name_list = []
            if len(faces) != 0:
                for i in range(len(faces)):
                    shape = predictor(img_rd, faces[i])
                    self.current_frame_feature_list.append(
                        face_reco_model.compute_face_descriptor(img_rd, shape))
                for k in range(len(faces)):
                    self.current_frame_name_list.append("unknown")
                    self.current_frame_name_position_list.append(tuple(
                        [faces[k].left(), int(faces[k].bottom() + (faces[k].bottom() - faces[k].top()) / 4)]))
                    current_frame_e_distance_list = []
                    for i in range(len(self.feature_known_list)):
                        if str(self.feature_known_list[i][0]) != '0.0':
                            e_distance_tmp = self.return_euclidean_distance(self.current_frame_feature_list[k],
                                                                            self.feature_known_list[i])
                            # print(e_distance_tmp)
                            current_frame_e_distance_list.append(
                                e_distance_tmp)
                        else:
                            current_frame_e_distance_list.append(
                                999999999)
                    similar_person_num = current_frame_e_distance_list.index(
                        min(current_frame_e_distance_list))
                    # print("   >>> Minimum e distance with ", self.name_known_list[self.similar_person_num], ": ", min(
                    #     current_frame_e_distance_list))

                    if min(current_frame_e_distance_list) < 0.4:
                        self.current_frame_name_list[k] = self.name_known_list[similar_person_num]

                    for kk, d in enumerate(faces):
                        cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]),
                                        (0, 255, 255), 2)

                self.current_frame_face_cnt = len(faces)

                self.chineseName = []
                self.show_chinese_name()

                img_with_name = self.draw_name(img_rd)
                img_rd = img_with_name

        if (len(text) > 0):
            self.qrcode_flag = True
            for i in self.current_frame_name_list:
                if i == text:
                    self.unknow_flag = False
                if i == 'unknown':
                    self.unknow_flag = True
        
        ct = 0
        if len(self.current_frame_name_list) ==1:
            for ii in self.current_frame_name_list:
                for jj in self.known:
                    if (ii != jj):
                        ct += 1
                if (ct == len(self.known) and ii != 'unknown'):
                    if self.qrcode_flag:
                        self.qrcode_flag=False
                        self.num =self.num+ 1
                        self.ui.lcdNumber.display(self.num)
                        timesql = (datetime.datetime.now()).strftime(
                            "%Y-%m-%d %H:%M:%S")
                        try:
                            catch_conn[0].cursor().execute(
                                "INSERT INTO `face` (`EmpID`, `EmpName`,`identity`,`EnterTime`) VALUES ('"+text+"','"+self.sqlNameList_dic[text][1]+"','"+self.sqlNameList_dic[text][4]+"','"+timesql+"')")
                        except:
                            pass
                        catch_conn[0].commit()
                        self.known.append(ii)
                        widget = QtWidgets.QWidget()
                        widget.setFixedSize(230, 100)
                        widget.setStyleSheet("background-color: #91A0AA")
                        layout = QtWidgets.QGridLayout()
                        label1 = QtWidgets.QLabel("人臉辨識")
                        label1.setStyleSheet(
                            "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
                        layout.addWidget(label1, 0, 0)
                        label2 = QtWidgets.QLabel(self.sqlNameList_dic[ii][0])
                        label2.setStyleSheet(
                            "color: #000000; background-color: #768895;padding-left: 5; font-size:14px; font-weight:bold; font-family: 微軟正黑體;")
                        layout.addWidget(label2, 0, 1)
                        tempdate = (datetime.datetime.now()).strftime(
                            "%Y-%m-%d")
                        temptime = (datetime.datetime.now()).strftime(
                            "%H:%M:%S")
                        label3 = QtWidgets.QLabel(tempdate+"\n"+temptime)
                        label3.setStyleSheet(
                            "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
                        layout.addWidget(label3, 1, 0)
                        label4 = QtWidgets.QLabel(self.sqlNameList_dic[ii][1])
                        label4.setStyleSheet(
                            "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
                        layout.addWidget(label4, 1, 1)
                        widget.setLayout(layout)
                        self.ui.face_layout.insertWidget(0,widget)
                elif(self.qrcode_flag==True and self.unknow_flag == True and self.first_unknow == False):
                    self.first_unknow =True
                    widget = QtWidgets.QWidget()
                    widget.setFixedSize(230, 100)
                    widget.setStyleSheet("background-color: #91A0AA")
                    layout = QtWidgets.QGridLayout()
                    label1 = QtWidgets.QLabel("進廠辨識")
                    label1.setStyleSheet(
                        "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
                    layout.addWidget(label1, 0, 0)
                    label2 = QtWidgets.QLabel("未知")
                    label2.setStyleSheet(
                        "color: #000000; background-color: #768895;padding-left: 5; font-size:14px; font-weight:bold; font-family: 微軟正黑體;")
                    layout.addWidget(label2, 0, 1)
                    tempdate = (datetime.datetime.now()).strftime(
                        "%Y-%m-%d")
                    temptime = (datetime.datetime.now()).strftime(
                        "%H:%M:%S")
                    label3 = QtWidgets.QLabel(tempdate+"\n"+temptime)
                    label3.setStyleSheet(
                        "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
                    layout.addWidget(label3, 1, 0)
                    label4 = QtWidgets.QLabel("未知的人")
                    label4.setStyleSheet(
                        "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
                    layout.addWidget(label4, 1, 1)
                    widget.setLayout(layout)
                    self.ui.face_layout.insertWidget(0,widget)


        img_rd = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
        height, width, channel = img_rd.shape
        step = channel * width
        self.draw_note_Rec(img_rd)
        try:
            self.current_frame_faces_cnt = len(faces)
        except:
            pass
        qImg = QImage(img_rd.data, width, height,
                        step, QImage.Format_RGB888)
        self.ui.face_scr.setPixmap(QPixmap.fromImage(qImg))
        self.update_fps()

    # 出口辨識
    def viewCam4(self):
        ret, img_rd = self.cap.read()
        if self.get_face_database():
            text = ""
            img_rd_qr = imutils.resize(img_rd)
            barcodes = pyzbar.decode(
                img_rd_qr,  symbols=[ZBarSymbol.QRCODE])
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img_rd_qr, (x, y), (x + w, y + h),
                                (0, 0, 255), 2)

                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                text = barcodeData
                cv2.putText(img_rd, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            faces = detector(img_rd, 0)
            self.draw_note_Rec(img_rd)
            self.current_frame_feature_list = []
            self.current_frame_face_cnt = 0
            self.current_frame_name_position_list = []
            self.current_frame_name_list = []
            if len(faces) != 0:
                for i in range(len(faces)):
                    shape = predictor(img_rd, faces[i])
                    self.current_frame_feature_list.append(
                        face_reco_model.compute_face_descriptor(img_rd, shape))
                for k in range(len(faces)):
                    self.current_frame_name_list.append("unknown")
                    self.current_frame_name_position_list.append(tuple(
                        [faces[k].left(), int(faces[k].bottom() + (faces[k].bottom() - faces[k].top()) / 4)]))
                    current_frame_e_distance_list = []
                    for i in range(len(self.feature_known_list)):
                        if str(self.feature_known_list[i][0]) != '0.0':
                            e_distance_tmp = self.return_euclidean_distance(self.current_frame_feature_list[k],
                                                                            self.feature_known_list[i])
                            # print(e_distance_tmp)
                            current_frame_e_distance_list.append(
                                e_distance_tmp)
                        else:
                            current_frame_e_distance_list.append(
                                999999999)
                    similar_person_num = current_frame_e_distance_list.index(
                        min(current_frame_e_distance_list))
                    # print("   >>> Minimum e distance with ", self.name_known_list[self.similar_person_num], ": ", min(
                    #     current_frame_e_distance_list))

                    if min(current_frame_e_distance_list) < 0.4:
                        self.current_frame_name_list[k] = self.name_known_list[similar_person_num]

                    for kk, d in enumerate(faces):
                        cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]),
                                        (0, 255, 255), 2)

                self.current_frame_face_cnt = len(faces)

                self.chineseName = []
                self.show_chinese_name()

                img_with_name = self.draw_name(img_rd)
                img_rd = img_with_name
        self.qrcode_flag = False
        if (len(text) > 0):
            self.qrcode_flag = True
            for i in self.current_frame_name_list:
                if i == text:
                    self.unknow_flag = False
                if i == 'unknown':
                    self.unknow_flag = True

                    
        if len(self.current_frame_name_list) ==1:
            for ii in self.current_frame_name_list:
                if self.qrcode_flag:
                    if ii in self.known:
                        self.known.remove(ii)
                        if ii != 'unknown':
                            self.qrcode_flag=False
                            self.num =self.num- 1
                            self.ui.lcdNumber.display(self.num)
                            timesql = (datetime.datetime.now()).strftime(
                                "%Y-%m-%d %H:%M:%S")
                            entertime = (datetime.datetime.now()).strftime(
                                "%Y-%m-%d")
                            try:
                                catch_conn[0].cursor().execute(
                                    "UPDATE `face` SET `OuterTime`='"+timesql+"'WHERE `EmpID` = '"+text+"' AND `EnterTime` LIKE '"+entertime+"%'")
                            except:
                                pass
                            catch_conn[0].commit()
                            widget = QtWidgets.QWidget()
                            widget.setFixedSize(230, 100)
                            widget.setStyleSheet("background-color: #91A0AA")
                            layout = QtWidgets.QGridLayout()
                            label1 = QtWidgets.QLabel("離廠辨識")
                            label1.setStyleSheet(
                                "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
                            layout.addWidget(label1, 0, 0)
                            label2 = QtWidgets.QLabel(self.sqlNameList_dic[ii][0])
                            label2.setStyleSheet(
                                "color: #000000; background-color: #768895;padding-left: 5; font-size:14px; font-weight:bold; font-family: 微軟正黑體;")
                            layout.addWidget(label2, 0, 1)
                            tempdate = (datetime.datetime.now()).strftime(
                                "%Y-%m-%d")
                            temptime = (datetime.datetime.now()).strftime(
                                "%H:%M:%S")
                            label3 = QtWidgets.QLabel(tempdate+"\n"+temptime)
                            label3.setStyleSheet(
                                "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
                            layout.addWidget(label3, 1, 0)
                            label4 = QtWidgets.QLabel(self.sqlNameList_dic[ii][1])
                            label4.setStyleSheet(
                                "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
                            layout.addWidget(label4, 1, 1)
                            widget.setLayout(layout)
                            self.ui.face2_layout.insertWidget(0,widget)

        img_rd = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
        height, width, channel = img_rd.shape
        step = channel * width
        self.draw_note_Rec(img_rd)
        try:
            self.current_frame_faces_cnt = len(faces)
        except:
            pass
        qImg = QImage(img_rd.data, width, height,
                        step, QImage.Format_RGB888)
        self.ui.face2_scr.setPixmap(QPixmap.fromImage(qImg))
        self.update_fps()

    # 安全辨識
    def viewCam3(self):        
        global now1
        # read image in BGR format
        ret, frame = self.cap.read()
        ret2, frame2 = self.cap.read()
        # convert image to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 辨識並將結果存入results1
        results1 = tfnet1.return_predict(frame)
        for color, result1 in zip(colors, results1):
            # 抓取圖片座標集label
            tl = (result1['topleft']['x'], result1['topleft']['y'])
            br = (result1['bottomright']['x'], result1['bottomright']['y'])
            label = result1['label']
            # 判斷是否為人體
            if label == 'person':
                if tl[1]-30 <= 0:
                    cap2 = frame[1:br[1]-1, tl[0]+1:br[0]-1]
                else:
                    cap2 = frame[tl[1]-30:br[1]-1, tl[0]+1:br[0]-1]

                # 在畫面上畫框框
                frame = cv2.rectangle(frame, tl, br, color, 3)
                # 在框框上加label
                frame = cv2.putText(
                    frame, label, tl, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                # 擷取偵測到人體的部分

                data = None
                try:
                    data = MainWindow.scan_qrcode(cap2)
                except Exception as e:
                    pass
                if data:
                    label2ID = data[0].data.decode('utf-8')
                    (x, y, w, h) = data[0].rect
                    frame = cv2.rectangle(
                        frame, (x+tl[0], y+tl[1]), (x + w+tl[0], y + h+tl[1]), color, 3)
                    frame = cv2.putText(
                        frame, label2ID,  (x+tl[0], y+tl[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 0), 2)
                # 將擷取出來的部分作第二層判斷
                results2 = tfnet2.return_predict(cap2)

                for result2 in (results2):
                    tl3 = (result2['topleft']['x']+tl[0],
                            result2['topleft']['y']+tl[1])
                    br3 = (result2['bottomright']['x']+tl[0],
                            result2['bottomright']['y']+tl[1])
                    label3 = result2['label']
                    if data:
                        if label3 == 'nomask':
                            if data:
                                self.sqlNameList_dic[label2ID][5] += 1
                    # 在畫面上畫框框
                    frame = cv2.rectangle(frame, tl3, br3, color, 3)
                    # 在框框上加label
                    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
                    frame = cv2.putText(
                        frame, label3, tl3, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 0), 2)

                results3 = tfnet3.return_predict(cap2)
                for result3 in (results3):
                    tl3 = (result3['topleft']['x']+tl[0],
                            result3['topleft']['y']+tl[1])
                    br3 = (result3['bottomright']['x']+tl[0],
                            result3['bottomright']['y']+tl[1])
                    label3 = result3['label']
                    if data:
                        if label3 == 'nohelmet':
                            if data:
                                self.sqlNameList_dic[label2ID][6] += 1
                    # 在畫面上畫框框
                    frame = cv2.rectangle(frame, tl3, br3, color, 3)
                    # 在框框上加label
                    #cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
                    frame = cv2.putText(
                        frame, label3, tl3, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 0), 2)
                if (now1+5) >= 60:
                    now1 -= 60
                ttime = int(time.localtime().tm_sec) - now1
                if ttime < 0:
                    ttime = ttime*-1
                if ttime > 2:
                    for i in self.sqlNameList_dic:
                        if int(time.localtime().tm_hour) <= 12:
                            timer = time.strftime(
                                "%Y%m%d1", time.localtime())
                        else:
                            timer = time.strftime(
                                "%Y%m%d2", time.localtime())
                        
                        if self.sqlNameList_dic[i][5] > 10:
                            pname = './Loss/'+i+"_"+timer+'nomask.jpg'
                            picname = i+"_"+timer+'nomask.jpg'
                            cv2.imwrite(pname, frame2)
                            tempdate = (datetime.datetime.now()).strftime("%Y-%m-%d")
                            temptime = (datetime.datetime.now()).strftime("%H:%M:%S")
                            if data:
                                nowScore = self.sqlNameList_dic[label2ID][3]
                                if self.sqlNameList_dic[label2ID][7]==False:
                                    nowScore = nowScore - self.lossScore['nomask']
                                    self.sqlNameList_dic[label2ID][3] = nowScore
                                    self.sendMail(label2ID, pname, "nomask")
                                    self.sqlNameList_dic[label2ID][7]=True
                                    timesql = (datetime.datetime.now()).strftime(
                                        "%Y-%m-%d %H:%M:%S")
                                    widget = QtWidgets.QWidget()
                                    widget.setFixedSize(230, 100)
                                    widget.setStyleSheet("background-color: #91A0AA")
                                    layout = QtWidgets.QGridLayout()
                                    label1 = QtWidgets.QLabel("未戴口罩")
                                    label1.setStyleSheet(
                                        "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label1, 0, 0)
                                    label2 = QtWidgets.QLabel(label2ID)
                                    label2.setStyleSheet(
                                        "color: #000000; background-color: #768895;padding-left: 5; font-size:14px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label2, 0, 1)
                                    label3 = QtWidgets.QLabel(tempdate+"\n"+temptime)
                                    label3.setStyleSheet(
                                        "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label3, 1, 0)
                                    label4 = QtWidgets.QLabel(str(self.sqlNameList_dic[label2ID][1]))
                                    label4.setStyleSheet(
                                        "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label4, 1, 1)
                                    widget.setLayout(layout)
                                    self.ui.factory_layout.insertWidget(0,widget)
                                    self.sqlNameList_dic[i][5] = 0
                                timesql = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
                                catch_conn[0].cursor().execute("INSERT INTO `safeidentify` (`EmpID`, `EmpName`,`ImgID`,`LoseTime`,`LoseName`,`LoseScore`,`TotalScore`) VALUES ('"+str(label2ID)+"','"+self.sqlNameList_dic[label2ID][1]+"','"+picname+"','"+timesql+"','"+"nomask"+"','"+str(self.lossScore['nomask'])+"','"+str(nowScore)+"')")                                
                                catch_conn[0].commit()
                                catch_conn[0].cursor().execute("UPDATE `member` SET `score`='"+str(nowScore)+"'WHERE `member`.`id` = '"+str(label2ID)+"'")                                
                                catch_conn[0].commit()
                                

                        if self.sqlNameList_dic[i][6] > 10:
                            pname = './Loss/'+i+"_"+timer+'nohelmet.jpg'
                            picname = i+"_"+timer+'nohelmet.jpg'
                            cv2.imwrite(pname, frame2)
                            tempdate = (datetime.datetime.now()).strftime("%Y-%m-%d")
                            temptime = (datetime.datetime.now()).strftime("%H:%M:%S")
                            timesql = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
                            if data:
                                nowScore = self.sqlNameList_dic[label2ID][3]
                                if data and self.sqlNameList_dic[label2ID][8]==False:
                                    self.sqlNameList_dic[label2ID][8]=True
                                    nowScore = nowScore-self.lossScore['nohelmet']
                                    self.sqlNameList_dic[label2ID][3] = nowScore
                                    self.sendMail(label2ID, pname, "nohelmet")
                                    # catch_conn[0].cursor().execute(
                                    #     "INSERT INTO `safeidentify` (`EmpID`, `EmpName`,`ImgID`,`LoseTime`,`LoseName`,`LoseScore`,`TotalScore`) VALUES ('"+label2+"','"+self.sqlNameList_dic[label2][0]+"','"+picname+"','"+timesql+"','"+'"nohelmet"'+"','"+str(self.lossScore['nohelmet'])+"','"+str(nowScore)+"')")
                                    # catch_conn[0].commit()
                                    widget = QtWidgets.QWidget()
                                    widget.setFixedSize(230, 100)
                                    widget.setStyleSheet("background-color: #91A0AA")
                                    layout = QtWidgets.QGridLayout()
                                    label1 = QtWidgets.QLabel("未戴安全帽")
                                    label1.setStyleSheet(
                                        "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label1, 0, 0)
                                    label2 = QtWidgets.QLabel(label2ID)
                                    label2.setStyleSheet(
                                        "color: #000000; background-color: #768895;padding-left: 5; font-size:14px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label2, 0, 1)
                                    label3 = QtWidgets.QLabel(tempdate+"\n"+temptime)
                                    label3.setStyleSheet(
                                        "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label3, 1, 0)
                                    label4 = QtWidgets.QLabel(self.sqlNameList_dic[label2ID][1])
                                    label4.setStyleSheet(
                                        "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
                                    layout.addWidget(label4, 1, 1)
                                    widget.setLayout(layout)
                                    self.ui.factory_layout.insertWidget(0,widget)
                                    self.sqlNameList_dic[i][6] = 0
                                catch_conn[0].cursor().execute("INSERT INTO `safeidentify` (`EmpID`, `EmpName`,`ImgID`,`LoseTime`,`LoseName`,`LoseScore`,`TotalScore`) VALUES ('"+str(label2ID)+"','"+self.sqlNameList_dic[label2ID][1]+"','"+picname+"','"+timesql+"','"+"nohelmet"+"','"+str(self.lossScore['nohelmet'])+"','"+str(nowScore)+"')")                                
                                catch_conn[0].commit()
                                catch_conn[0].cursor().execute("UPDATE `member` SET `score`='"+str(nowScore)+"'WHERE `member`.`id` = '"+str(label2ID)+"'")                                
                                catch_conn[0].commit()
                                

                        self.sqlNameList_dic[i][5] = 0
                        self.sqlNameList_dic[i][6] = 0
                    now1 = int(time.localtime().tm_sec)
        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height,
                        step, QImage.Format_RGB888)
        # show image in label_2
        self.ui.factory_scr.setPixmap(QPixmap.fromImage(qImg))
   
    def showtime(self):
        time = QDateTime.currentDateTime()
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.ui.label.setText(timedisplay)
        self.ui.label_3.setText(namess)

    def controlTimer(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.timer2.start(30)

    def changeColor(self):
        if self.ui.pushButton_2.isChecked():
            self.ui.pushButton_2.setStyleSheet("background-color : white")
            self.closeCam = True
            self.controlTimer()
        else:
            self.closeCam = False

    def abc(self):
        self.cap.release()
        self.timer2.stop()
        self.ui.label_2.setPixmap(self.pic)

    # 分數個人資料
    def score_databaseview(self):
        cursor = catch_conn[0].cursor()
        row2 = self.ui.score_table.currentRow()
        id =self.ui.score_table.item(row2, 0).text()
        self.datawindow = QtWidgets.QMainWindow()
        self.datawindow.setWindowIcon(QIcon('factory.png'))
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.datawindow)
        cursor.execute("SELECT * FROM member WHERE id ='"+id+"'")
        data = cursor.fetchall()
        self.ui2.id_label.setText(id)
        self.ui2.name_label.setText(str(data[0][1]))
        self.ui2.score_label.setText(str(data[0][3]))
        self.ui2.identity_label.setText(str(data[0][4]))
        str2= str("./data/data_faces_from_camera/"+str(id)+"/img_face_1.jpg")
        photo=QtGui.QPixmap(str2)
        self.ui2.photo.setPixmap(photo)
        global score,lost
        
        score = int(data[0][3])
        lost = 100-int(data[0][3])
        print(score)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot() 
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.ui2.chart_photo.setLayout(layout)
        self.datawindow.show()
        # 彥丞_個人統計圖
        # self.ui2.chart_photo.setPixmap()
        # 跨啥
        self.ui2.close_btn.clicked.connect(self.datawindow.close)
    
    # 進出個人資料
    def io_databaseview(self):
        cursor = catch_conn[0].cursor()
        row2 = self.ui.io_table.currentRow()
        id =self.ui.io_table.item(row2, 0).text()

        self.datawindow = QtWidgets.QMainWindow()
        self.datawindow.setWindowIcon(QIcon('factory.png'))
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.datawindow)
        cursor.execute("SELECT * FROM member WHERE id ='"+id+"'")
        data = cursor.fetchall()
        self.ui2.id_label.setText(id)
        self.ui2.name_label.setText(str(data[0][1]))
        self.ui2.score_label.setText(str(data[0][3]))
        self.ui2.identity_label.setText(str(data[0][4]))
        str2= str("./data/data_faces_from_camera/"+str(id)+"/img_face_1.jpg")
        photo=QtGui.QPixmap(str2)
        self.ui2.photo.setPixmap(photo)
        global score,lost
        
        score = int(data[0][3])
        lost = 100-int(data[0][3])
        print(score)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot() 
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)
        self.ui2.chart_photo.setLayout(layout)
        self.datawindow.show()
        # 彥丞_個人統計圖
        # self.ui2.chart_photo.setPixmap()
        # 跨啥
        self.ui2.close_btn.clicked.connect(self.datawindow.close)

    # 關閉系統
    def closeallview(self):
        self.cap.release()
        self.timer2.stop()
        self.close()

    # 刪除進出紀錄
    def io_Delete(self):
        cur = catch_conn[0].cursor()
        try:
            row_2 = self.ui.io_table.currentRow()
            del_d = self.ui.io_table.item(row_2, 3).text()
            cur.execute("DELETE FROM face WHERE EnterTime = '"+del_d+"'")
            catch_conn[0].commit()
            self.ui.io_table.removeRow(row_2)
        except:
            pass
    
    # 刪除辨識紀錄
    def score_Delete(self):
        cur = catch_conn[0].cursor()
        try:
            row_2 = self.ui.score_table.currentRow()
            del_d = self.ui.score_table.item(row_2, 3).text()
            cur.execute(
                "DELETE FROM safeidentify WHERE LoseTime = '"+del_d+"'")
            catch_conn[0].commit()
            self.ui.score_table.removeRow(row_2)
        except:
            pass
    
    # 添加人員資料
    def member_add(self):
        while self.press_n_flag == 0:
            db_id = self.ui.id_edit.text()
            db_name = self.ui.name_edit.text()
            db_email = self.ui.email_edit.text()
            db_identity = self.ui.identity_edit.currentText()
            if(db_id == ""):
                QtWidgets.QMessageBox().information(None, "提示", "請輸入員工編號")
            elif(db_name == ""):
                QtWidgets.QMessageBox().information(None, "提示", "請輸入員工姓名")
            elif(db_email == ""):
                QtWidgets.QMessageBox().information(None, "提示", "請輸入電子信箱")
            elif (("@" in db_email) == False):
                QtWidgets.QMessageBox().information(None, "提示", "請輸入正確的電子信箱格式")
            else:
                catch_conn[0].cursor().execute("INSERT INTO `member` (`id`, `name`,`email`,`score`,`identity`) VALUES ('" +str(db_id)+"', '"+str(db_name)+"', '"+str(db_email)+"', '100', '"+str(db_identity)+"')")
                catch_conn[0].commit()
                QtWidgets.QMessageBox().information(None, "提示", "您已經成功登錄此會員資訊！")
            person_list = os.listdir("data/data_faces_from_camera/")

            if db_id in person_list:
                label = QtWidgets.QLabel("錯誤, 重複的登錄者，請重新輸入。")
                label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
                self.ui.face_reg_layout.addWidget(label)
            elif db_id != "":
                self.existing_faces_cnt += 1
                self.current_face_dir = self.path_photos_from_camera + db_id
                os.makedirs(self.current_face_dir)
                label = QtWidgets.QLabel("已登入並新建" + db_id+"的人臉資料夾")
                label.setStyleSheet("font-size:16px; font-family: 微軟正黑體;")
                self.ui.face_reg_layout.addWidget(label)
                self.ss_cnt = 0
                self.press_n_flag = 1

#ScoreChart
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        labe = "score",""
        size = [score,lost]
        self.axes = fig.add_subplot(111)
        self.axes.pie(size, labels = labe, colors =["lightblue","gray"],explode = [0.1,0] )
        self.axes.set_aspect('1')
        self.axes.figure.canvas.draw()
        super(MplCanvas, self).__init__(fig)
class Login_window(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self):
        super(Login_window, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('factory.png'))       
        self.pushButton.setText("登入")
        self.pushButton_2.setText("取消")
        self.btn_login_fuc
        self.pushButton.clicked.connect(self.btn_login_fuc)
        self.pushButton_2.clicked.connect(self.btn_cancel)

    # buttonfunction
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.btn_login_fuc()

    def btn_login_fuc(self):
        global namess
        cursor = connect.cursor()
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = 'select * from login where account="%s" and password="%s"' % (
            account, password)
        cursor.execute(sql)
        a = cursor.fetchone()
        if cursor.rowcount == 0:
            QtWidgets.QMessageBox().warning(None, "警告", "帳密錯誤")
        else:
            namess = a[1]
            print(namess)
            window.show()

            self.close()

    def btn_cancel(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_window()
    login.show()
    window = MainWindow()
    sys.exit(app.exec_())

