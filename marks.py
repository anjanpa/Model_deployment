import pandas as pd 
import numpy as np
from joblib import load
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_prediction(rooms):
	
	model=load("model.joblib")

	X_test=np.array(rooms)
	X_test=X_test.reshape((-1,1))


	return model.predict(X_test)
