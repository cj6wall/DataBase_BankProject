import csv
import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

data = pd.read_csv('/Users/winnergogo/Desktop/DB/bank_withname.csv')

train_df = pd.read_csv('/Users/winnergogo/Desktop/DB/bank_withname.csv')  

train_df = train_df.drop(['name'], axis=1)

ages = train_df['age']

train_df['marital'] = train_df['marital'].replace('married',0)
train_df['marital'] = train_df['marital'].replace('single',1)
train_df['marital'] = train_df['marital'].replace('divorced',2)
train_df['marital'] = train_df['marital'].replace('unknown',3)

train_df['education'] = train_df['education'].replace('MS',0)
train_df['education'] = train_df['education'].replace('PhD',1)
train_df['education'] = train_df['education'].replace('BS',2)
train_df['education'] = train_df['education'].replace('unknown',3)

train_df['housing'] = train_df['housing'].replace('no',0)
train_df['housing'] = train_df['housing'].replace('yes',1)
train_df['housing'] = train_df['housing'].replace('unknown',2)

train_df['loan'] = train_df['loan'].replace('no',0)
train_df['loan'] = train_df['loan'].replace('yes',1)
train_df['loan'] = train_df['loan'].replace('unknown',2)


balances = train_df['balance']
durations = train_df['duration']

y_train = train_df['y']
y_train = y_train.replace('no',0)
y_train = y_train.replace('yes',1)

train_df = train_df.drop(['y'], axis=1)

train_df = train_df.values
y_train = y_train.values

model = Sequential()

model.add(Dense(units=16, input_dim=7, 
                activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(units=32, 
                activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(units=256, 
                activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(units=1,
                activation='sigmoid'))
                    
model.summary()

model.compile(loss='binary_crossentropy', 
              optimizer='adam', metrics=['accuracy'])

model.fit(train_df, y_train,batch_size=512, 
         epochs=500,verbose=2,validation_split=0.2)

# model.save('my_model.h5')

# model = load_model('my_model.h5')