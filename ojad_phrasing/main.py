#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import argparse
import requests
import cssselect
from lxml import html

parser = argparse.ArgumentParser(description='ojad-phrasing')
parser.add_argument(
    '-estimation',
    type=str,
    required=False,
    dest='estimation',
    default='crf',
    choices=('crf', 'bunsetsu'),
    help='アクセント句境界推定 crf - 機械学習による句境界推定, bunsetsu - 文節境界を利用')
parser.add_argument('text', nargs=argparse.REMAINDER)

def analyze(estimation, text):
    payload = {
        '_method': 'POST',
        'data[Phrasing][text]':             text,
        'data[Phrasing][curve]':            'advanced',
        'data[Phrasing][accent]':           'advanced',
        'data[Phrasing][accent_mark]':      'all',
        'data[Phrasing][estimation]':       estimation,
        'data[Phrasing][analyze]':          'true',
        'data[Phrasing][phrase_component]': 'invisible',
        'data[Phrasing][param]':            'invisible',
        'data[Phrasing][subscript]':        'visible',
        'data[Phrasing][jeita]':            'invisible',
    }
    resp = requests.post('http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index', data=payload)

    doc = html.fromstring(resp.text)
    phrasing_rows = doc.cssselect('#phrasing_main > .phrasing_row_wrapper')
    for phrasing_row in phrasing_rows:
        phrasing_text_spans = phrasing_row.cssselect('.phrasing_phrase_wrapper > .phrasing_text > span')
        if len(phrasing_text_spans) == 0:
            continue
        pitch = ''
        text = ''
        for span in phrasing_text_spans:
            char = span.cssselect('.char')
            if len(char) == 0 or char[0].text is None:
                continue
            text += char[0].text

            if 'accent_plain' in span.classes:
                pitch += '\033[0;31mー\033[0m'
            elif 'accent_top' in span.classes:
                pitch += '\033[0;31m─┐\033[0m'
            else:
                pitch += '　'
        print pitch
        print text.encode('utf-8')

        phrasing_subscript = phrasing_row.cssselect('.phrasing_phrase_wrapper > .phrasing_subscript')[0]
        phrasing_subscript_spans = phrasing_subscript.cssselect('span')
        text = ''
        for span in phrasing_subscript_spans:
            if span.text:
                text += span.text
        print text.encode('utf-8')

def main():
    args = parser.parse_args()

    if len(args.text) > 0:
        analyze(args.estimation, '\n'.join(args.text))
    else:
        analyze(args.estimation, '\n'.join(sys.stdin.readlines()))

if __name__ == "__main__":
    main()
