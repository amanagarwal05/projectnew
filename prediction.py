import abc1
import os
import pandas as pd

def get_values(values):
    user_values=pd.DataFrame([values])
    print(user_values)
    y=abc1.classifier.predict(user_values)
    print(y)
