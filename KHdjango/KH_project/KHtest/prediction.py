import numpy as np
from keras.models import load_model
import csv
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
import numpy as np

from .models import Data

class Predict():

	def do_prediction():
		keras.backend.clear_session()
		model = load_model('/Users/winnergogo/Desktop/DB/KHdjango/KH_project/KHtest/my_model.h5')

		r = Data.objects.raw('SELECT * FROM data ORDER BY id DESC LIMIT 1')
		for i in r:

			user_text = [i.age, i.marital, i.education, i.balance, i.housing , i.loan , i.duration]

			if i.marital == 'married':
				maritalv = 0
			elif i.marital == 'single':
				maritalv = 1
			elif i.marital == 'divorced':
				maritalv = 2
			else:
				maritalv = 3

			if i.education == 'MS':
				educationv = 0
			elif i.education == 'PhD':
				educationv = 1
			elif i.education == 'BS':
				educationv = 2
			else:
				educationv =3

			if i.housing == 'no':
				housingv = 0
			elif i.housing == 'yes':
				housingv = 1
			else:
				housingv = 2

			if i.loan == 'no':
				loanv = 0
			elif i.loan == 'yes':
				loanv = 1
			else:
				loanv = 2
			
			test = [[i.age, maritalv, educationv, i.balance, housingv, loanv, i.duration]]
		test = np.array(test)

		predicted = model.predict(test)
		if predicted > 0.5:
			result = 'yes'
			probility = predicted[0][0]*100
			word = '恭喜！😀恭喜！😀'
			return result , probility, word, user_text, 

		else:
			result = 'no'
			probility = predicted[0][0]*100
			word = '抱歉！😰抱歉！😰'
			return result , probility, word, user_text, 


