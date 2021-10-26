import abc1
import os
import pandas as pd
x=5
def get_values(transmission,authorization,oversubscription,net_design,hack_prone,protocol,comm_prot_label,filesize_trans,firewalls,hard_comp,router,devices):
    print("successful")
    print(x)
    user_values=pd.DataFrame([[transmission,authorization,oversubscription,net_design,hack_prone,protocol,comm_prot_label,filesize_trans,firewalls,hard_comp,router,devices]])
    print(user_values)
    y=abc1.classifier.predict(user_values)
    print(y)
