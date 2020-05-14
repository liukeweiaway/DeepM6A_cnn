#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2020/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------


def choiceThreshold(species, tissues, threshold):
    threshold = str(threshold)
    M_threshold = 0.5
    if species == 'Human':
        if tissues == 'brain':
            if threshold == 'low':  # low
                M_threshold = 0.7848
            elif threshold == 'normal':  # normal
                M_threshold = 0.8185
            elif threshold == 'high':  # high
                M_threshold = 0.7848
        elif tissues == 'liver':
            if threshold == 'low':
                M_threshold = 0.8477
            elif threshold == 'normal':
                M_threshold = 0.8950
            elif threshold == 'high':
                M_threshold = 0.8477
        elif tissues == 'kidney':
            if threshold == 'low':
                M_threshold = 0.8005
            elif threshold == 'normal':
                M_threshold = 0.8485
            elif threshold == 'high':
                M_threshold = 0.9250

    elif species == 'Mouse':
        if tissues == 'brain':
            if threshold == 'low':
                M_threshold = 0.8372
            elif threshold == 'normal':
                M_threshold = 0.8703
            elif threshold == 'high':
                M_threshold = 0.9304
        elif tissues == 'liver':
            if threshold == 'low':
                M_threshold = 0.7946
            elif threshold == 'normal':
                M_threshold = 0.8252
            elif threshold == 'high':
                M_threshold = 0.8924
        elif tissues == 'kidney':
            if threshold == 'low':
                M_threshold = 0.7499
            elif threshold == 'normal':
                M_threshold = 0.8055
            elif threshold == 'high':
                M_threshold = 0.8886
        elif tissues == 'heart':
            if threshold == 'low':
                M_threshold = 0.7794
            elif threshold == 'normal':
                M_threshold = 0.8075
            elif threshold == 'high':
                M_threshold = 0.8716
        elif tissues == 'testis':
            if threshold == 'low':
                M_threshold = 0.8356
            elif threshold == 'normal':
                M_threshold = 0.8708
            elif threshold == 'high':
                M_threshold = 0.9236

    elif species == 'Rat':
        if tissues == 'brain':
            if threshold == 'low':
                M_threshold = 0.7787
            elif threshold == 'normal':
                M_threshold = 0.8189
            elif threshold == 'high':
                M_threshold = 0.8886
        elif tissues == 'liver':
            if threshold == 'low':
                M_threshold = 0.7999
            elif threshold == 'normal':
                M_threshold = 0.8383
            elif threshold == 'high':
                M_threshold = 0.9174
        elif tissues == 'kidney':
            if threshold == 'low':
                M_threshold = 0.7832
            elif threshold == 'normal':
                M_threshold = 0.8510
            elif threshold == 'high':
                M_threshold = 0.9199

    return M_threshold
