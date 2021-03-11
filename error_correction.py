# -*- coding: utf-8 -*-

import difflib
from functools import reduce

ja = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅍㅎ#'
mo = 'ㅏㅐㅑㅐㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ#'
bad = ' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄻㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ#'

BASE = 0xAC00

def segment(ch):

    code = ord(ch) - BASE
    jong = code % 28

    code = code - jong
    jung = int((code / 28) % 21)

    code = int(code / 28)
    cho = int(code / 21)

    if cho < 0 :
        cho = -1
    if jong > 19 :
        jong = -1

    return ja[cho], mo[jung], bad[jong]

def diff(word1, word2):
    L1 = ''.join(reduce(lambda x1, x2 : x1+x2, map(segment, word1)))
    L2 = ''.join(reduce(lambda x1, x2 : x1+x2, map(segment, word2)))
    differ = difflib.SequenceMatcher(None, L1, L2)
    return differ.ratio()

def correction(call):
    #단어 세트 추가 및 변경
    target = ['호랑이', '사자', '가오리', '토끼', '사슴']

    result = 0
    result_word = ''

    for i in range(len(target)):
        current = diff(call, target[i])
        current_word = target[i]
        if current > result:
            result = current
            result_word = current_word

    return result_word

if __name__ == "__main__":
    print(correction(''))
