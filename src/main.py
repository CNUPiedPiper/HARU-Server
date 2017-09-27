#-*- coding: utf-8 -*- 
from os import listdir
from os.path import abspath, dirname
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import functions
import types
from builder import modelbuilder
from sentence2vec import sentence2vec
import configparser
from flask import Flask, request
import json

app = Flask('Main')

# Wait rest api from HARU Interface
@app.route('/request',  methods=['POST'])
def answer_request():
    if request.method == 'POST':
        order = request.form[u'sentence']
        print("[HARU]Sentence : " + order)

        text, ans_num = Main.main_flow(Main(), order)

        data = {
            "function_number" : ans_num,
            "answer" : text
        }
        print data
        return json.dumps(data)

# Haru Server main class.
class Main:
    
    # Module for classifying user's order sentence.
    class Classifier:
        def __init__(self):
            self.s2v = sentence2vec.Sentence2Vec()
            self.model_set = []
            
            # Read neural network model from file.
            file_list = listdir( ''.join([dirname(abspath(__file__)), '/model']) )
            file_list.sort()
            for f in file_list:
                self.model_set.append(modelbuilder.ModelBuilder(f))

        def classify(self, input_sentence):
            # Convert input_sentence to vector using sentecne2vec.
            result = self.s2v.sentence2vec(input_sentence)
            words_vec = result[0]
            words_raw = result[1]

            input_vector = np.array(words_vec)
            
            result = np.array([])
            model_number = 1
            
            # Put pre-processed vector to neural network model.
            for model in self.model_set:
                status_1 = np.zeros([100])
                status_2 = np.zeros([100])
                for i in xrange(input_vector.shape[0]):
                    prop, status_1, status_2 = model.run(input_vector[i, :], status_1, status_2)
                result = np.append(result, prop)
                print(''.join(['[HARU] Model', str(model_number), ' :: ', str(result[model_number-1])]))
                model_number = model_number + 1

            max_index = np.argmax(result)
            
            # No answer in model
            if result[max_index] < 0.5:
                return 0, words_raw
            # Return argmax index
            else:
                return max_index + 1, words_raw

    def __init__(self):
        self.classifier = self.Classifier()
        self.response = [functions.__dict__.get(func) for func in dir(functions)
                           if isinstance(functions.__dict__.get(func), types.FunctionType)]

        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        naver_id = self.config.get('NAVER', 'id')
        naver_secret = self.config.get('NAVER', 'secret')


    def main_flow(self, order):
        print('[HARU] In Main flow..')

        sentence = order
        
        # sentence = u'오늘 날씨가 어때'
        # sentence = u'내일 천안 날씨가 어때'
        # sentence = u'오늘 이슈는 뭐야'
        # sentence = u'지금 몇시야'
        # sentence = u'이 노래가 뭐지'
        # sentence = u'네이버가 뭐야'
        # sentence = u'윤동주가 누구야'
        # sentence = u'런던 검색해줘'
        # sentence = u'가시두더지를 찾아줘'
        # sentence = u'딱풀이 뭐야'
        # sentence = u'오늘이 무슨 요일이야'
        
        # Get classified number from user's order sentence.
        response_number, words = self.classifier.classify(sentence)
        print('[HARU] Getting the result text from API')
        
        # Run app function
        # Send anwer_text to interface
        answer_text = self.response[response_number](words)
        print answer_text
        return answer_text, response_number
    
    
    def run(self):
        # Wait request from interface.
        app.run(host='0.0.0.0')

        # self.main_flow(None)
        # import time
        # time.sleep(3)
        

if __name__ == "__main__":
    print('[HARU] Starting the HARU Server')
    Main().run()
