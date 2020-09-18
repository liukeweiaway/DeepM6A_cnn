#!/usr/bin/env python
# -*- coding:utf-8-*-
# auther:Kewei Liu time:2019/8/26 20:11  QQ:422209303  e-mail:Liukeweiaway@hotmail.com
# --------------------------------------------------------------------------
import pandas as pd
import re
from joblib import load
from featureEtraction import iMRMFeatureEtraction
import numpy as np
import tensorflow as tf
from mainf import Threshold
# ------------------------------------ HG --------------------------------------------


def Deep_M6A(sequence, species, tissues, threshold):
    modelPath = 'model/' + species + '/' + tissues
    network = tf.keras.models.load_model(modelPath)
    M_threshold = Threshold.choiceThreshold(species, tissues, threshold)
    # -------------------------------------------------------------
    line = sequence
    line = line.upper()  # bug
    if re.search(r'[^AUCG]', line.strip()):
        nota = "Please input the RNA sequence 'AUCG'."
        return nota
    length = len(line.strip())
    if length < 41:
        nota = "Please input the RNA sequence at least 41 bases! "
        return nota
    hg_n_base_41_M6A = 19
    hg_n_base_list_M6A_proba = []
    hg_M6A_list_num = []
    for base in line.strip()[20:-20]:
        hg_n_base_41_M6A += 1
        file_inter_M6A = open('inter_use/hg_inter_use_M6A.txt', 'w')
        if base == 'A':
            new_line = line.strip()[hg_n_base_41_M6A - 20:hg_n_base_41_M6A + 21]
            print(*iMRMFeatureEtraction.onehot(new_line, 41), file=file_inter_M6A)
            file_inter_M6A.close()
            pddtest = pd.read_csv("inter_use/hg_inter_use_M6A.txt", sep=' ', header=None)
            X_test = pddtest.values[:, :]
            X_test = X_test.astype(np.float32).reshape(-1, 4, 41, 1, order='F')

            # prediction = network.predict_classes(X_test).astype('int')
            prePro = network.predict(X_test)
            if prePro[0][1] > M_threshold:
                hg_n_base_list_M6A_proba.append(prePro[0][1])
                hg_M6A_list_num.append(hg_n_base_41_M6A + 1)
        if len(hg_M6A_list_num) > 0:
            hg_M6A_list_num.reverse()
            hg_n_base_list_M6A_proba.reverse()
            n = 0
            for i in [i - 1 for i in hg_M6A_list_num]:
                line = list(line)
                line[i] = '<font color=#00FF00>A</font>(' + str(hg_n_base_list_M6A_proba[n]) + ')'
                n += 1
        line = str(line).replace(',', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace(' ', '')
        line = line.replace('\'', '')
        line = line.replace('\\r', '')
        line_pro = line.replace('fontcolor', 'font color')
        line = line_pro
        pro_list = re.findall('\(.*?\)', line_pro)
        for i in pro_list:
            line = line.replace(i, '')
        return line, line_pro, hg_M6A_list_num


