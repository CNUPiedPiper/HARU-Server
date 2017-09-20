#-*- coding: utf-8 -*- 
from datetime import datetime

def get_date() : 

    weekname = ['월', '화', '수', '목', '금', '토', '일']

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    weekday = weekname[datetime.now().weekday()]

    return "오늘은 {year}년 {month}월 {day}일 {weekday}요일 입니다.".format(year=year, month=month, day=day, weekday=weekday)
