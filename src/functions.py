#-*- coding: utf-8 -*-
from apibucket import weather, issue, geoip, wiki
from apibucket.music_recognizer import music_recog
import datetime
import configparser
import re

config = configparser.RawConfigParser()
config.read('config.ini')

def function0(words):
    return u'적절한 응답을 찾을 수 없습니다'

def function1(words):
    # nouns = [word[:-5] for word in words if re.findall(r"\w+", word)[0] == u'Noun']
    # print (nouns)
    w_key = config.get('WEATHER', 'key')
    m_key = config.get('MISE', 'key')
    geo = geoip.Geoip().get_geo()
    return weather.get_weather(w_key, geo[1], geo[2], m_key, geo[0], 0)

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
    title = [word[:-5] for word in words if re.findall(r"\w+", word)[0] == u'Noun'][0]
    return wiki.get_wiki(title)
