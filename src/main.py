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
from flask import Flask

app = Flask('Main')

@app.route('/order/<order>/')
def answer_request(order):
    print(order)
    return Main.main_flow(Main(), order)

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
            input_vector = np.array(self.s2v.sentence2vec(input_sentence))
            
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
                return 0
            # Return argmax index
            else:
                return max_index + 1

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
        
        #sentence = u'오늘 날씨는 어때'
        #sentence = u'오늘 이슈는 뭐야'
        #sentence = u'지금 몇시야'
        #sentence = u'이 노래가 뭐지'
        
        # Get classified number from user's order sentence.
        response_number = self.classifier.classify(sentence)
        print('[HARU] Getting the result text from API')
        
        # Run app function
        #anwer_text interface로 보냄
        answer_text = self.response[response_number](None)
        print(answer_text)
        
        # Call run funciton again.
        #self.run()
        return answer_text
    
    
    def run(self):
        # Wait request from interface.
        app.run(host='0.0.0.0')
        

if __name__ == "__main__":
    print('[HARU] Starting the HARU Server')
    Main().run()
