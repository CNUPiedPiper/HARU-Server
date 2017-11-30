#-*- coding: utf-8 -*-
from apibucket import weather, issue, geoip, wiki, date, word_play
#from apibucket.music_recognizer import music_recog
from sentence2vec import word2vec
import datetime
import configparser
import re
from geopy.geocoders import Nominatim
import geopy

config = configparser.RawConfigParser()
config.read('config.ini')
geolocator = Nominatim()

def function0(words):
    return u'적절한 응답을 찾을 수 없습니다'

def function1(words):
    sido = [u'서울',u'서울시',u'부산',u'부산시',u'대구',u'대구시',u'인천',u'인천시',u'광주',u'광주시',u'울산',u'울산시',u'세종',u'세종시']
    #nouns = [re.findall(r"[가-힣\w]+", word)[0] for word in words if re.findall(r"[가-힣\w]+", word)[1] == u'Noun']
    #print (unicode(words))
    w_key = config.get('WEATHER', 'key')
    m_key = config.get('MISE', 'key')
    geo = geoip.Geoip().get_geo()
    location = []
    location.append(geo[0])
    location.append(geo[1])
    location.append(geo[2])
    w2v = word2vec.Word2Vec()
    day = 0
    city = u'이곳'

    error = 0

    for word in words:
        if w2v.model.wv.similarity(unicode(word),u'내일/Noun') >= 0.9 : 
            day = 1
        elif w2v.model.wv.similarity(unicode(word),u'지역/Noun') >= 0.1 \
        and w2v.model.wv.similarity(unicode(word),u'날씨/Noun') <= 0.7 \
        and w2v.model.wv.similarity(unicode(word),u'지역/Noun') <= 0.7:
            if word == '시/Noun' :
                continue
            city = unicode(word[:-5])
            try :
                geo_city = geolocator.geocode(city, timeout=10)
            except geopy.exc.GeocoderTimedOut :
                try :
                    geo_city = geolocator.geocode(city, timeout=20)
                except geopy.exc.GeocoderTimedOut :
                    return u"적절한 지역을 찾지 못했습니다. 다시 한번 검색해주세요"
            
            try : 
                location[0] = city[:2]
                sido.index(city)
            except ValueError:
                location[0] = geo_city.address[-8:-6]
            
            location[1] = geo_city.latitude
            location[2] = geo_city.longitude
            print(location[0])

    return weather.get_weather(w_key, location[1], location[2], m_key, city, location[0], day)

def function2(words):
    return u"좋은 아침 입니다. " + issue.get_issue()

def function3(words):
    now = datetime.datetime.now()
    return u'지금은 {h}시 {m}분 입니다.'.format(h=now.hour, m=now.minute)

def function4(words):
    '''
	host = config.get('MUSIC_RECOGNIZER', 'host')
	key = config.get('MUSIC_RECOGNIZER', 'key')
	secret = config.get('MUSIC_RECOGNIZER', 'secret')
	return music_recog.get_music_title(host, key, secret)
    '''
    return u"노래를 들려주세요."

def function5(words):
    title = [re.findall(r"[가-힣\w]+", word)[0] for word in words if re.findall(r"[가-힣\w]+", word)[1] == u'Noun'][0]
    return wiki.get_wiki(title)

def function6(words):
    return date.get_date()

def function7(word):
    return word_play.get_word_play()

def function8(word):
    return u"저는 점점 똑똑해지는, 인공지능 스피커, 하루 입니다."
