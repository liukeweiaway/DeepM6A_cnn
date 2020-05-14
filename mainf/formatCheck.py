#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2020/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
from mainf.preproces import readFile
import re


def formatCheck(inputFile, outputFile, species, tissues, threshold):
    Fasta_name, sequence = readFile(inputFile)
    speciesList = ['Human', 'Mouse', 'Rat']
    tissuesList = ['brain', 'liver', 'kidney', 'heart', 'testis']
    thresholdList = ['low', 'normal', 'high']
    line = sequence.upper()  # bug
    if re.search(r'[^AUCG]', line.strip()):
        note = "Please input the RNA sequence 'AUCG' or 'aucg'."
        return note
    length = len(line.strip())
    if length < 41:
        note = "Please input the RNA sequence at least 41 bases! "
        return note
    if species not in speciesList:
        note = "eror: please input: -s Human/Mouse/Rat"
        return note
    if tissues not in tissuesList:
        note = "eror: please input: -t brain/liver/kidney/heart/testis"
        return note
    if threshold not in thresholdList:
        note = "eror: please input: -t low/normal/high"
        return note
    note = 'checking over'
    return note

