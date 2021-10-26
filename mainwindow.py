from tkinter import *
from tkinter import messagebox
import os
from prediction import get_values
from bagging_prediction import display_prediction

"""""
def get_prediction(values):
    os.system("prediction.py")
    get_values(values)
"""


main_window=Tk()
main_window.title("NETWORK DETAILS")
main_window.resizable(True,True)

# HARDWARE FEATURES

# string variables_hardware
netId_txt_var=StringVar()
Hcom_txt_var=StringVar()
router_txt_var=StringVar()
devices_txt_var=StringVar()


# Hardware GUI
network_id_label=Label(main_window,text="Network ID").pack()
network_id=Entry(main_window,textvariable=netId_txt_var)
network_id.pack()
compatible_label=Label(main_window,text="non compatible hardware?").pack()
hard_compatibility=Entry(main_window,textvariable=Hcom_txt_var)
hard_compatibility.pack()
router_label=Label(main_window,text="Outdated router?").pack()
router_value=Entry(main_window,textvariable=router_txt_var)
router_value.pack()
devices_label=Label(main_window,text="Too many devices connected to a single router").pack()
devices_value=Entry(main_window,textvariable=devices_txt_var)
devices_value.pack()



#print(hard_comp)

# MISCELANOUS FACTORS

# string variables_miscelanous
trans_txt_var=StringVar()
auth_txt_var=StringVar()
sub_txt_var=StringVar()
design_txt_var=StringVar()
hack_txt_var=StringVar()

# Miscelanous GUI
trans_label=Label(main_window,text="Incompatibility between transmission hardware and software?").pack()
transmission_value=Entry(main_window,textvariable=trans_txt_var)
transmission_value.pack()
auth_label=Label(main_window,text="Unauthorized users/devices can access the network?").pack()
auth_value=Entry(main_window,textvariable=auth_txt_var)
auth_value.pack()
sub_label=Label(main_window,text="Oversubscription of network?").pack()
sub_value=Entry(main_window,textvariable=sub_txt_var)
sub_value.pack()
design_label=Label(main_window,text="poor network design?").pack()
design_value=Entry(main_window,textvariable=design_txt_var)
design_value.pack()
hack_label=Label(main_window,text="network prone to hackers?").pack()
hack_value=Entry(main_window,textvariable=hack_txt_var)
hack_value.pack()



# SOFTWARE FACTORS

# string variables_software
protocol_txt_var=StringVar()
comm_prot_txt_var=StringVar()
filesize_txt_var=StringVar()
firewalls_txt_var=StringVar()

 # software GUI
protocol_label=Label(main_window,text="Unauthorized users/devices can access the network").pack()
protocol_value=Entry(main_window,textvariable=protocol_txt_var)
protocol_value.pack()
comm_prot_label=Label(main_window,text="Unauthorized users/devices can access the network").pack()
comm_prot_value=Entry(main_window,textvariable=comm_prot_txt_var)
comm_prot_value.pack()
filesize_label=Label(main_window,text="Unauthorized users/devices can access the network").pack()
filesize_value=Entry(main_window,textvariable=filesize_txt_var)
filesize_value.pack()
firewalls_label=Label(main_window,text="Unauthorized users/devices can access the network").pack()
firewalls_value=Entry(main_window,textvariable=firewalls_txt_var)
firewalls_value.pack()

def store_values():
    netId = int(netId_txt_var.get())
    hard_comp = int(Hcom_txt_var.get())
    router =int( router_txt_var.get())
    devices=int(devices_txt_var.get() )

    transmission=int(trans_txt_var.get())
    authorization=int(auth_txt_var.get())
    oversubscription=int(sub_txt_var.get())
    net_design=int(design_txt_var.get())
    hack_prone=int(hack_txt_var.get())

    protocol=int(protocol_txt_var.get())
    comm_protocol=int(comm_prot_txt_var.get())
    filesize_trans=int(filesize_txt_var.get())
    firewalls=int(firewalls_txt_var.get())

    return [transmission,authorization,oversubscription,net_design,hack_prone,protocol,comm_protocol,filesize_trans,firewalls,hard_comp,router,devices]

    #print(type(hard_comp))
    get_prediction(transmission,authorization,oversubscription,net_design,hack_prone,protocol,comm_protocol,filesize_trans,firewalls,hard_comp,router,devices)


def adaboost_classifier():
    values=store_values()
    get_values(values)



def bagging_classifier():
    values=store_values()
    display_prediction(values)
    


#Button(main_window,text="Get prediction",bg="orange",fg="white",width=20).pack()
Button(main_window,text="Get Adaboost prediction",bg="orange",fg="white",width=20,command=adaboost_classifier).pack()
Button(main_window,text="Get Bagging prediction",bg="orange",fg="white",width=20,command=bagging_classifier).pack()
main_window.mainloop()
