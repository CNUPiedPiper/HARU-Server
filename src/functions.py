#-*- coding: utf-8 -*-
from apibucket import weather, issue, geoip, wiki, date
from apibucket.music_recognizer import music_recog
from sentence2vec import word2vec
import datetime
import configparser
import re

config = configparser.RawConfigParser()
config.read('config.ini')

def function0(words):
    return u'적절한 응답을 찾을 수 없습니다'

def function1(words):
    #nouns = [re.findall(r"[가-힣\w]+", word)[0] for word in words if re.findall(r"[가-힣\w]+", word)[1] == u'Noun']
    #print (unicode(words))
    w_key = config.get('WEATHER', 'key')
    m_key = config.get('MISE', 'key')
    geo = geoip.Geoip().get_geo()
    w2v = word2vec.Word2Vec()
    day = 0
    #day = [1 for noun in words if w2v.model.wv.similarity(unicode(noun), u'내일/Noun') >= 0.9]
    for word in words:
        if w2v.model.wv.similarity(unicode(word),u'내일/Noun') >= 0.9 : 
            day = 1
    #print (w2v.model.wv.similarity(u'오늘/Noun', u'내일/Noun'))
    return weather.get_weather(w_key, geo[1], geo[2], m_key, geo[0], day)

def function2(words):
    return u"좋은 아침 입니다. " + issue.get_issue()

def function3(words):
    now = datetime.datetime.now()
    return u'지금은 {h}시 {m}분 입니다.'.format(h=now.hour, m=now.minute)

def function4(words):
	host = config.get('MUSIC_RECOGNIZER', 'host')
	key = config.get('MUSIC_RECOGNIZER', 'key')
	secret = config.get('MUSIC_RECOGNIZER', 'secret')
	return music_recog.get_music_title(host, key, secret)

def function5(words):
    title = [re.findall(r"[가-힣\w]+", word)[0] for word in words if re.findall(r"[가-힣\w]+", word)[1] == u'Noun'][0]
    return wiki.get_wiki(title)

def function6(words):
    return date.get_date()
