from tkinter import *
import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
global a
global b
global c
c=0
a=""
b=""
def first(): 
    print("Clicked")
def disp():
    df=pd.read_csv('minorproject5.csv')
    x=df.loc[:,'Aggregate rating':'Votes']
    y=df.loc[:,'Rating text']
    knn=KNeighborsClassifier()
    knn.fit(x,y)
    x_test=[[0,0],[10,9000]]
    prediction=knn.predict(x_test)
    #print('Accuracy of test sets :{:.2f}'.format(knn.score(x_test,prediction)))
    #print(prediction)
    h=str("%.2f" % knn.score(x,y))
    st1.set(h)
    st2.set(str(knn.score(x_test,prediction)))
    #print('Accuracy of train sets :{:.2f}'.format(knn.score(x,y)))
def show_label_info():
    df=pd.read_csv('minorproject5.csv')
    #print(df.head())
    x=df.loc[:,'Aggregate rating':'Votes']
    y=df.loc[:,'Rating text']
    knn=KNeighborsClassifier()
    knn.fit(x,y)
    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
    x_test=[[3,305],[4.8,333]]
    prediction=knn.predict(x_test)
    d=str(prediction)
    st.set(d)
    n=int(e1.get())
    x=df.iloc[:,[0,1]].values
    lb1.insert(END, 'Total data items :  %d' %len(x))
    lb1.insert(END, "Restaurant ID's having price range {}=".format(n))
    #print("Restaurant ID's having price range {}=".format(n))
    for i in range(len(x)):
        if x[i][1]==n:
            lb1.insert(END, x[i][0])
    #print(df.groupby('Price range').size())
    n = int(e2.get())
    rat = float(e3.get())
    x = df.iloc[:, [0, 1, 2]].values
    lb2.insert(END, 'Total data items :  %d' %len(x))
    lb2.insert(END, "Restaurant ID's having price range {} and rating above {} =".format(n, rat))
    #print('Total data items', len(x))
    #print("Restaurant ID's having price range {} and rating above {} =".format(n, rat))
    no = 0
    for i in range(len(x)):
        if x[i][1] == n and x[i][2] >= rat:
            lb2.insert(END, x[i][0])
            no += 1
    lb2.insert(END, "Total number of items having the given requirements are : %d" %no)       
    #print("Total number of items having the given requirements are", no)
root=Tk()
root.title('Asach')
root.geometry('550x650')
root.config(background='cornflowerblue')
root.resizable(width=False, height=False)
sc1=Scrollbar(root) 
sc2=Scrollbar(root)
label0=Label(root, text='First Stage  :', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
label1=Label(root, text=' Enter price range to\nsee all restaurants\n under that pricing  : ', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
label2=Label(root, text='Second Stage: ', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
label3=Label(root, text='Enter price range  :', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
label4=Label(root, text=' Enter Rating          : ', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
label_predic=Label(root, text='When [3,305],[4.8,333]\nis given see, the O/P   :', font=("Impact Bold",15), fg="gray23", bg="cornflowerblue")
label5=Label(root, text='Data Details  : ', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
lb1=Listbox(root, yscrollcommand=sc1.set, height=8, width=30, bg="gray93")
label6=Label(root, text='After computing: ', font=("Impact Bold",17), fg="gray23", bg="cornflowerblue")
lb2=Listbox(root, yscrollcommand=sc2.set, height=8, width=30, bg="gray93")
sc1.grid(row=2, sticky=E)
sc2.grid(row=9, sticky=E)
label0.grid(row=0, column=1)
label1.grid(row=1)
label2.grid(row=3, column=1)
label3.grid(row=4)
label4.grid(row=5)
label_predic.grid(row=6)
label5.grid(row=6, column=1)
label6.grid(row=8, column=1)
e1=Entry(root)
e1.focus()
e2=Entry(root)
e3=Entry(root)
st=StringVar()
e4=Entry(root, textvariable=st)
st1=StringVar()
e5=Entry(root, textvariable=st1)
st2=StringVar()
e6=Entry(root, textvariable=st2)
e1.grid(row=1,column=1)
e2.grid(row=4,column=1)
e3.grid(row=5,column=1)
e4.grid(row=6, column=1)
e5.grid(row=11, column=1)
e6.grid(row=12, column=1)
lb1.grid(row=2, column=1)
lb2.grid(row=9, column=1)
sc1.config(command=lb1.yview)
sc2.config(command=lb2.yview)
e1.config(highlightbackground="cornflowerblue")
e2.config(highlightbackground="cornflowerblue")
e3.config(highlightbackground="cornflowerblue")
e4.config(highlightbackground="cornflowerblue")
e5.config(highlightbackground="cornflowerblue")
e6.config(highlightbackground="cornflowerblue")
Button(root, text='Show Details', command= show_label_info, highlightbackground="cornflowerblue").grid(row=13,column=0, sticky=S, pady=4)
Button(root, text='Accuracy', command=disp, highlightbackground="cornflowerblue").grid(row=13,column=1, sticky=S, pady=4)
Button(root,text='Exit', command=exit, highlightbackground="cornflowerblue").grid(row=13, column=2, sticky=S, pady=4)
root.mainloop
