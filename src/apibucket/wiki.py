#-*- coding: utf-8 -*- 
import wikipedia as wk
import sys

def get_wiki(title):
    wk.set_lang('ko')
    try: 
        summary = wk.summary(title, sentences=2)
    except wk.exceptions.DisambiguationError as ed:
        summary = wk.summary(ed.options[0], sentences=2)
    except wk.exceptions.PageError as ep: 
        return u'해당 정보가 없습니다.'

    paren_size = 0
    text = ""
    for ch in summary:
        if ch == '(':
            paren_size += 1
        elif ch == ')':
            paren_size -= 1
            continue

        if paren_size == 0:
            text += ch
        
    return title + u'에 관한 위키 백과의 검색 결과를 들려드릴게요. ' + text