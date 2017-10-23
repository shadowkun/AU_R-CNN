import os
from collections import OrderedDict

import cv2
from bidict import bidict

ROOT_PATH = "/home/machen/dataset/"
# ROOT_PATH = "D:/work/face_expr/data/"

DATA_PATH = {
    "ck+": ROOT_PATH + "/CK+",
    "fer2013": ROOT_PATH+"/fer2013",
    "CASME2": ROOT_PATH + "/CASME2",
    "mnist": ROOT_PATH + "/mnist",
    "BP4D": ROOT_PATH + "/BP4D/",
    "DISFA": ROOT_PATH + "/DISFA/",
    "BP4D_DISFA": ROOT_PATH + "/BP4D_DISFA/"
}
TRAINING_PATH = {
    "BP4D": ROOT_PATH + "/BP4D/BP4D-training/",
    "DISFA": ROOT_PATH + "DISFA/",
}

CROP_DATA_PATH = {
    "BP4D": ROOT_PATH + "/BP4D/BP4D_crop/",
    "DISFA": ROOT_PATH + "/DISFA/DISFA_crop/"
}
AU_REGION_MASK_PATH = {
    "BP4D": ROOT_PATH + "/BP4D/BP4D_AUmask/",
    "DISFA": ROOT_PATH + "/DISFA/DISFA_AUmask/",
}
ENHANCE_BALANCE_PATH = {
    "BP4D": ROOT_PATH + "/BP4D/BP4D_enhance_balance/"
}


'''
READER_CREATER's key must equally match DATA_PATH's key
'''
READER_CREATER = {
    "ck+": "CKPlusDataReader",
    "fer2013" : "Fer2013DataReader",
    "CASME2" : "CASME2DataReader",
    "BP4D" : "BP4DDataReader",
}
READ_COLOR_TYPE = {
    "CASME2" : cv2.IMREAD_COLOR,
    "BP4D" : cv2.IMREAD_COLOR,
}
AU_LABEL_BP4D = {
    0: 0,
    1: 1,
    9: "unlabeled",
}
AU_INTENSITY_BP4D = { i:i for i in range(0, 9)}
AU_INTENSITY_BP4D.update({9: "unlabeled"})

EMOTION_LABEL_CK = {
    0: "neutral",
    1: "anger",
    2: "contempt",
    3: "disgust",
    4: "fear",
    5: "happiness",
    6: "sadness",
    7: "surprise",
}

EMOTION_LABEL_CASME2 = {
    "happiness": 0,
    "disgust": 1,
    "repression": 2,
    "surprise": 3,
    "fear": 4,
    "sadness": 5,
    "others": 6
}
KMEANS_CLUSTER_NUM = 3

NUM_CLASSES = {
    "CASME2": 7,
    "mnist": 10,
}

IMG_SIZE = (512, 512)  # not same with VGG, FC layer single train, before fix
CHANNEL = 3
MEAN_VALUE = 128
TRN_TEST_FOLD = 5

CV_PRETRAIN_MODEL = ROOT_PATH + "/cv_train_model"
DLIB_LANDMARK_PRETRAIN = CV_PRETRAIN_MODEL + os.sep + "shape_predictor_68_face_landmarks.dat"

PY_CAFFE_PATH = "/home2/mac/caffe_orig/python"
CAFFE_PATH = "/home2/mac/caffe_mac/build/tools/caffe"


FLOW_PYRAMID_LEVEL = 4

DEBUG = True

BACKEND = "lmdb"
BACKEND_DIR = "CAFFE_IN"

PRETRAIN_WEIGHTS = {"keras_vgg16": "D:/work/face_expr/data/keras_pretrain/vgg16_weights.h5",
                    "fcn8s": "/home/machen/dataset/chainer_model/fcn8s.npz"}

# some cases AU with other region needs to be incorporate with it
# only shows AU couple tuple, #TODO may cause bug, especially AU couple change
BOX_SHIFT  = {
    ('6',):((-10,10), (-10,10), (-10,10), (-10,10)),
    ('16', '20', '25', '26', '27'):((-10,10), (-10,10), (-10,10), (-10,10)),
    ('10', '11', '12', '13', '14', '15'):((-10,10), (-10,10), (-10,10), (-10,10)),
    ('18', '22', '23', '24', '28'):((-10,10), (-10,10), (-10,10), (-10,10)),
    ('17',): ((-10,10), (-10,10), (-10,10), (-10,10)),
    ('51', '52', '53', '54', '55', '56', '57', '58'): ((-10,10), (-10,10), (-10,10), (-10,10)),
    ('9',): ((-10,10), (-10,10), (-10,10), (-10,10)),
    ('41', '42', '43', '44', '45', '46', '61', '62', '63', '64'):((-10,10), (-10,10), (-10,10), (-10,10)),
    ('4',):((-10,10), (-10,10),(-1,1), (-1,1)),
    ('1', '2', '5', '7'):((-10,10), (-10,10), (-1,1), (-1,1)),
}

LABEL_INCORPORATE = {
    ("4",) :[("1","2","5","7"),],
    ("6",):[("9", ),],
    ('10', '11', '12', '13', '14', '15'): [('18', '22', '23', '24', '28'),('16', '20', '25', '26', '27')],
    ('16', '20', '25', '26', '27'): [('10', '11', '12', '13', '14', '15'),],
}
# 时刻搞清楚到底AU号和label之间的对应关系
AU_ROI = OrderedDict({"1":[1, 2, 8, 9, 5, 6, 12, 13, 40, 41, 42, 43],  # 修改，增加眼睛部分，与5和7一致
                      "2":[1, 2, 8, 9, 5, 6, 12, 13, 40, 41, 42, 43],  # 修改与1一样
                      "4":[1, 2, 3, 4, 8, 9, 5, 6, 12, 13, 40, 41],  # 增加3和4：皱眉头的眉头部分
                      "5":[1, 2, 8, 9, 5, 6, 12, 13, 40, 41, 42, 43], # 整个不对，改掉，应该是眼睛和眉毛部分
                      "6":[42,43,16,17,18,19],# 修改，增加眼睛和颧骨部分，颧骨外侧删掉
                      "7":[1, 2, 8, 9, 5, 6, 12, 13, 40, 41, 42, 43], # 修改
                      "9":[10,11,17,18,22,23],
                      "10":[21,22,23,24,25,26,27,28,37], # 删除21和24
                      "11":[21,22,23,24,25,26,27,28,37], # 修改为10一样
                      "12":[21,22,23,24,25,26,27,28,37], # 重定义
                      "13":[21,22,23,24,25,26,27,28,37], # 修改为与12 一致
                      "14":[21,22,23,24,25,26,27,28,37], # 修改为与12 一致
                      "15":[21,22,23,24,25,26,27,28,37], # 修改为与12一致
                      "16":[25,26,27,28,29,30,31,32,33,34,35,36,37], # 删掉22和23
                      "17":[29,30,31,32,33,34,35,36],
                      "18":[26,27,37,29,30,31,32],  # 只有嘴巴区域，删掉22和23，与AU22保持一致
                      "20":[25,26,27,28,29,30,31,32,33,34,35,36,37],
                      "22":[26,27,37,29,30,31,32],  # 本来22,23,24,25,28是 [26,27,37,29,30,31,32] 需要加入下巴区域吗？
                      "23":[26,27,37,29,30,31,32],
                      "24":[26,27,37,29,30,31,32],
                      "25":[25,26,27,28,29,30,31,32,33,34,35,36,37],
                      "26":[25,26,27,28,29,30,31,32,33,34,35,36,37], # 修改为27号合并，与AU25的区别是带下巴
                      "27":[25,26,27,28,29,30,31,32,33,34,35,36,37],
                      "28":[26,27,37,29,30,31,32],
                      "41":[8,9,12,13,40,41,42,43],  #上睑下垂，增加眼睛部分
                      "42":[8,9,12,13,40,41,42,43], # 修改
                      "43":[8,9,12,13,40,41,42,43],# 修改
                      "44":[8,9,12,13,40,41,42,43],# 修改
                      "45":[8,9,12,13,40,41,42,43],# 修改
                      "46":[8,9,12,13,40,41, 42,43],# 修改
                      "51":[i for i in range(1,42)],  #turn around whole head ， 两种页面定义不同 奇怪
                      "52":[i for i in range(1,42)],  #turn around whole head
                      "53":[i for i in range(1,42)],  #turn around whole head
                      "54":[i for i in range(1,42)],  #turn around whole head
                      "55":[i for i in range(1,42)],  #turn around whole head
                      "56":[i for i in range(1,42)],  #turn around whole head
                      "57":[i for i in range(1,42)],  #head forward
                      "58":[i for i in range(1,42)],  #head back
                      "61":[8,9,12,13,40,41,42,43],
                      "62":[8,9,12,13,40,41,42,43],
                      "63":[8,9,12,13,40,41,42,43],
                      "64":[8,9,12,13,40,41,42,43], })

BP4D_use_AU = ["1", "2", "4", "5", "6", "7", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "20", "22", "23", "24", "27", "28"]
DISFA_use_AU = ["1", "2", "4", "5", "6", "9", "12", "15", "17", "20", "25", "26"]

paper_use_BP4D = ["1", "2", "4", "6", "7", "10", "12", "14", "15", "17", "23", "24"]
paper_use_DISFA = ["1", "2", "4", "6", "9", "12", "25", "26"]

BOX_NUM = {"BP4D":9, "DISFA":8}
# AU_SQUEEZE all 0 means is actually background
AU_SQUEEZE = bidict({idx : str(AU) for idx, AU in enumerate(sorted(map(int, list(AU_ROI.keys()))))}) # inside train or test, always use key

#key is ROI number
ROI_LANDMARK = OrderedDict({"1": ["17u","19u","19","17"], #eye brow
                "2": ["19u","21u","21","19"],
                "3": ["21u", "27uu","27","21"],
                "4": ["27uu","22u","27","22"],
                "5": ["22u","24u","24","22"],
                "6": ["24u","26u","26","24"],
                #eye and temple
                "7": ["1", "17", "36"],
                "8": ["17","19","37","36"],
                "9": ["19","38","39","21"],
                "10":["21","27","28","39"],
                "11":["22","27","28", "42"],
                "12":["22","42","43","24"],
                "13":["24","44","45","26"],
                "14":["26","16","15","45"],
                #middle
                "15":["2","41~2","3~29","3"],
                "16":["41","2~41","3~29","39"],
                "17":["39","3~29","29","28"],
                "18":["28","29","13~29","42"],
                "19":["42","46","14~46","13~29"],
                "20":["14~46","14","13","13~29"],
                #middle down
                "21":["3","3~29","4~33","4"],
                "22":["4~33","3~29","29","33"],
                "23":["33","29","13~29","12~33"],
                "24":["13~29","13","12","12~33"],
                #mouse
                "25":["4","4~33","5~59","5"],
                "26":["5~59","4~33","33","59"],
                "27":["33","55","11~55","12~33"],
                "28":["11~55","12~33","12","11"],
                #below mouse
                "29":["59","58","6~58","5~59"],
                "30":["6~58","58","57","8~57"],
                "31":["57","8~57","10~56","56"],
                "32":["56","10~56","11~55","55"],
                #chin
                "33":["5","5~59","6~58","6"],
                "34":["6","6~58","8~57","8"],
                "35":["8~57","10~56","10","8"],
                "36":["10~56","10","11","11~55"],
                #miss part mouse
                "37":["33","55","56","57","58","59"],
                "38":["1","2","36","37"],
                "39":["14","15","44","45"],
                "40":["19","37","38"],
                "41":["24","43","44"],
                "42": ["36","37", "38", "39", "40", "41"], # left eye
                "43": ["42","43","44","45","46","47"]
                })

AU_RELATION_JPML = {
    "positive" : [(1,2), (6,7), (6,10),(7,10), (6,12), (7,12), (10,12), (17,24)],
    "negative" : [(1,6), (1,7), (2,6), (2,7), (10,17), (10,23), (10,24), (12,15), (12,17), (12,23), (12,24), (15,23),
                  (15,24), (23,24)]
}

# calculated from graphic_lasso_cv to get percscion matrix, number inside is true AU
AU_RELATION_BP4D = [(5, 9), (10, 11), (5, 6), (1, 15), (11, 23), (4, 12), (1, 6), (6, 17), (1, 11), (16, 24), (16, 17), (12, 20), (1, 14), (12, 24), (12, 17), (7, 28), (12, 28), (1, 24), (4, 28), (6, 16), (1, 23), (4, 5), (4, 14), (5, 24), (4, 16), (16, 23), (10, 24), (5, 15), (1, 9), (10, 28), (4, 11), (2, 17), (2, 7), (5, 10), (20, 24), (4, 15), (5, 7), (2, 11), (2, 15), (15, 16), (2, 4), (9, 12)]
AU_RELATION_BP4D = set(AU_RELATION_BP4D)

AU_RELATION_DISFA = [(12, 15), (2, 6), (12, 26), (12, 20), (2, 9), (5, 6), (12, 26),(2, 25), (5, 12), (5, 25), (4, 12), (1, 6), (2, 12), (17, 25), (6, 26), (9, 12)]
AU_RELATION_DISFA = set(AU_RELATION_DISFA)

GRAPH_CONFIG = {"has_attrib_value": False}

OPEN_CRF_CONFIG = {"max_bp_iter":10, "penalty_sigma_square":0.0001, "max_iter":30, "eps":1e-3, "use_pure_python":False}