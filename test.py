# -*- coding: utf-8 -*-

import error_correction_polbot
import argparse

parser = argparse.ArgumentParser(description='mj')

parser.add_argument('--word', required = True, help = '단어 입력')

args = parser.parse_args()

print(error_correction_polbot.correction(arg.word))
