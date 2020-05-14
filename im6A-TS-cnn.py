#!/usr/bin/env python
# -*- coding:utf-8-*-
# author: Liukewei time:2020/1/21 QQ:422209303 e-mail:Liukeweiaway@hotmail.com
# ----------------------------------------------------------------------------
import argparse
from mainf import preproces
import warnings
from mainf.formatCheck import formatCheck
warnings.filterwarnings("ignore")


def parse_args():
    """
    :return:进行参数的解析
    """
    description = "We propose a new model called im6A-TS-cnn, which can identify m6A sites in brain, liver, kidney, heart and testis from human, mouse and rat by using the algorithm of convolutional neural network. Thank you very much for submitting the error message to Liukeweiaway@hotmail.com.  Example: python im6A-TS-cnn.py -i sequence.txt -o ccc.html -s Human -t tissues -ts low"
    parser = argparse.ArgumentParser(description=description)
    help = "The correct path of address"
    parser.add_argument('--addresses', help=help)
    parser.add_argument('-i', '--inputFile', help='-i input.txt (The input file is a complete Fasta format sequence.)')
    parser.add_argument('-o', '--outputFile', help='-o output.html (Results are saved under results folder.)')
    parser.add_argument('-s', '--species', help='-s Human/Mouse/Rat (Choose one from three species to use.)')
    parser.add_argument('-t', '--tissues', help='-t Human(brain/liver/kidney) Mouse(brain/liver/kidney/heart/testis) Rat(brain/liver/kidney) (We can choose testis you want.)')
    parser.add_argument('-ts', '--threshold', help='-th low/normal/high (We offer 3 options based on the difference in specificity, which are low, normal and high.)')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    formatCheck = formatCheck(args.inputFile, args.outputFile, args.species, args.tissues, args.threshold)
    print(formatCheck)
    preproces.preprocesser(args.inputFile, args.outputFile, args.species, args.tissues, args.threshold)
    # previous_deal(args.inputFile, args.outputFile, args.featureList)  # feature extraction
