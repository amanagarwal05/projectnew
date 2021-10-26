import numpy as np
import pandas as pd
from sklearn import *
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('netanomset.csv')
df["misc_fact1"] = df["misc_fact1"].map({'InCompatiable':1,'Compatiable':0})
df["misc_fact2"] = df["misc_fact2"].map({'UnAuthorizedAccess':1,'AuthorizedAccess':0})
df["misc_fact3"] = df["misc_fact3"].map({'OverSubscription':1,'ReasonableSubscription':0})
df["misc_fact4"] = df["misc_fact4"].map({'PoorDesign':1,'GoodDesign':0})
df["misc_fact5"] = df["misc_fact5"].map({'ProneToHackers':1,'NotProneToHackers':0})
df["sw_fact1"] = df["sw_fact1"].map({'OwnProtocol':1,'CommonProtocol':0})
df["sw_fact2"] = df["sw_fact2"].map({'IneffectiveProtocol':1,'EffectiveProtocol':0})
df["sw_fact3"] = df["sw_fact3"].map({'UnDefinedFileLimits':1,'DefinedFileLimits':0})
df["sw_fact4"] = df["sw_fact4"].map({'ImProperFirewalls':1,'ProperFirewalls':0})
df["hw_fact1"] = df["hw_fact1"].map({'HardwareIncompatiability':1,'Hardwarecompatiability':0})
df["hw_fact2"] = df["hw_fact2"].map({'OutdatedRouter':1,'GoodRouter':0})
df["hw_fact3"] = df["hw_fact3"].map({'ManyDevices':1,'ReasonableDevices':0})
df["Sum_Desc"] = df["Sum_Desc"].map({'NoAnomaly':1,'AnomLikely':2,'AnomMostLikely':3})
data = df[["misc_fact1","misc_fact2","misc_fact3","misc_fact4","misc_fact5","sw_fact1","sw_fact2","sw_fact3","sw_fact4","hw_fact1","hw_fact2","hw_fact3","Sum_Desc"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = AdaBoostClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
#print ("The accuracy of Adaboost Classifier on testing data is: " + str(accuracy))
#testSet = [[1,0,0,0,1,0,0,0,0,0,1,0]]
#test = pd.DataFrame(testSet)
#predictions_new = classifier.predict(test)
def print_predict(y):
    predictions_new = classifier.predict(y)




#print('Adaboost Prediction on the first test set is:',predictions)
#testSet = [[1,0,1,0,1,1,0,0,1,0,1,0]]
#test = pd.DataFrame(testSet)
#predictions = classifier.predict(test)
#print('Adaboost Prediction on the second test set is:',predictions)
#testSet = [[1,1,1,0,1,1,0,1,1,1,1,0]]
#test = pd.DataFrame(testSet)
#predictions = classifier.predict(test)
#print('Adaboost Prediction on the third test set is:',predictions)
