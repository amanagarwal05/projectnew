import bagging1
import os
import pandas as pd

def display_prediction(values):
    user_values=pd.DataFrame([values])
    print(user_values)
    y=bagging1.classifier.predict(user_values)
    print(y)