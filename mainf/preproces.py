#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2020/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
from mainf import predictType
import re


def cuttingText(seq, num):
    seq_split = []  ## 空列表
    while (seq != ''):
        seq_split.append(seq[0:num])
        seq = seq[num:]
    return seq_split


def readFile(fileName):
    with open(fileName, 'r') as f:
        file_data = f.readlines()
    return file_data[0], file_data[1]


def preprocesser(inputFile, outputFile, species, tissues, threshold):
    Fasta_name, sequence = readFile(inputFile)
    sequence = sequence.upper()
    htmlf = open('im6A-TS-cnn.html', 'r', encoding="utf-8")
    outputFileR = 'results/' + outputFile
    outputFileP = 'results/' + 'Possibility_' + outputFile
    result_real = open(outputFileR, 'w', encoding="utf-8")
    result_poosi = open(outputFileP, 'w', encoding="utf-8")

    hg_line_M6A, hg_line_M6A_pro, hg_M6A_list = predictType.Deep_M6A(sequence, species, tissues, threshold)
    seq_split = cuttingText(sequence, 60)
    M6A_seq_ = ['-'] * len(sequence)
    for i in hg_M6A_list:
        M6A_seq_[i - 1] = 'A'  # <font color=#00FF00>A</font>
    M6A_seq__split = cuttingText(''.join(M6A_seq_), 60)
    for line in htmlf.readlines():
        if '<li>>' not in line:
            result_real.write(line.strip())
            result_real.write('\n')
        elif '<li>>N1 :GUGAUAUAACUCAGUGGCAGA</li>' in line:
            result_real.write(Fasta_name)
            result_real.write('<br>')
            for i in range(len(seq_split)):
                M6A_seq = M6A_seq__split[i].replace('A', '<font color=#00FF00>A</font>')
                result_real.write('&nbsp&nbsp&nbsp&nbsp')
                result_real.write(''.join(seq_split[i]))
                result_real.write('&nbsp&nbsp&nbsp&nbsp')
                if i < len(seq_split) - 1:
                    result_real.write(str((i + 1) * 60))
                result_real.write('<br>')
                result_real.write('m6A:')
                result_real.write(''.join(M6A_seq))
                result_real.write('<br>')
    result_poosi.write('m6A:')
    result_poosi.write('<br>')
    result_poosi.write(hg_line_M6A_pro)
