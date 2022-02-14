import glob
from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import keras as k
from google.colab import files
uploaded=files.upload()
df=pd.read_csv('kidney_disease.csv')
df.head()
df.shape
columns_2_retain=['sg','al','sc','hemo','pcv','wc','rbc','htn','classification']

#Drop the columns that are not in columns_2_retain
df=df.drop([col for col in df.columns if not col in columns_2_retain], axis=1)

#Drop the rows with Nan or missing values
df=df.dropna(axis=0)
#Transform the non numeric data in the columns
for column in df.columns:
  if df[column].dtype==np.number:
    continue
  else:
    df[column]=LabelEncoder().fit_transform(df[column])
#Print the first five rows new cleaned dataset
df.head()
#Split the  data into independent (X) dataset and independent (y) dataset
X=df.drop(['classification'], axis=1)
y=df['classification']
#Feature scaling
x_scaler=MinMaxScaler()
x_scaler.fit(X)
column_names=X.columns
X[column_names]=x_scaler.transform(X)
#split the data into 4:1
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, shuffle=True)
#Build the model
model=Sequential()
model.add(Dense(256, input_dim=len(X.columns), kernel_initializer=k.initializers.random_normal(seed=13), activation='relu'))
model.add(Dense(1, activation='hard_sigmoid'))
#Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#Train the model
history=model.fit(X_train, y_train,epochs=2000, batch_size=X_train.shape[0])
#Save the model
model.save('ckd.model')
#Visualize the loss and accuracy of the model
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('model accuracy and loss')
plt.ylabel('accuracy and loss')
plt.xlabel('epoch')
print('shape of train data:', X_train.shape)
print('shape of test data:', X_test.shape)
pred=model.predict(X_test)
#Show the actual values
print(y_test)
print(pred)
print('Original {0}:'.format(", ".join(str(x) for x in y_test)))
print('Predict  {0}:'.format(", ".join(str(x) for x in pred)))
