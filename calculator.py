from tkinter import *



root=Tk()

root.title("CALCULATOR")

displaytext=StringVar()
displaytext.set(0)


def buttonClicked(a):
    b=displaytext.get()
    c=str(b)+str(a)
    d=int(c)
    displaytext.set(d)

def operatorClicked(a):
    k=displaytext.get()
    global firstValue
    firstValue=float(k)
    displaytext.set(0)
    global operator
    operator=a
    
def equalClicked():
    m=displaytext.get()
    secondValue=float(m)
    
    if operator==1:
        
        result=firstValue+secondValue
        displaytext.set(result)
    elif operator==2:
        result=firstValue-secondValue
        displaytext.set(result)
    elif operator==3:
        result=firstValue*secondValue
        displaytext.set(result)
    elif operator==4:
        result=firstValue/secondValue
        displaytext.set(result)
    elif operator==5:
        displaytext.set(0)
    elif operator==6:
        
        displaytext.set()
    
 
        
        
    
Entry(root,bg="lightgray").grid(column=6,row=1,columnspan=3,rowspan=1,sticky=N+W+E+S)

display=Label(root,textvariable=displaytext,fg="gray")
display.grid(column=6,row=1,columnspan=3,rowspan=2,sticky=N+E)

buttonEqu=Button(root,text="=",command=equalClicked)
buttonEqu.grid(row=3,column=7,columnspan=2,sticky=N+S+W+E)


buttonPlus=Button(root,text="+",command=lambda:operatorClicked(1))
buttonPlus.grid(row=1,column=4,rowspan=2,sticky=N+S+W+E)

buttonbackspace=Button(root,text="<=",command=lambda:operatorClicked(6))
buttonbackspace.grid(row=2,column=8,sticky=N+S+W+E)



buttonMinus=Button(root,text="-",command=lambda:operatorClicked(2))
buttonMinus.grid(row=1,column=5,sticky=N+S+W+E)

buttonMul=Button(root,text="*",command=lambda:operatorClicked(3))
buttonMul.grid(row=2,column=5,sticky=N+S+W+E)

buttonDivide=Button(root,text="/",command=lambda:operatorClicked(4))
buttonDivide.grid(row=2,column=6,sticky=N+S+W+E)

buttonPlus=Button(root,text="CLEAR",command=lambda:operatorClicked(5))
buttonPlus.grid(row=2,column=7,rowspan=1,sticky=N+S+W+E)


buttondot=Button(root,activebackground= "gray",height=2,width=2,text=".",command =lambda:buttonClicked("."))
buttondot.grid(row=3,column=6,sticky=W+N+E+S)

button0=Button(root,activebackground= "gray",height=2,width=2,text="0",command =lambda:buttonClicked(0))
button0.grid(row=3,column=4,columnspan=2,sticky=W+N+E+S)

button1=Button(root,activebackground= "gray",height=2,width=2,text="1",command =lambda:buttonClicked(1))
button1.grid(row=1,column=1)

button2=Button(root,height=2,width=2,text="2",command=lambda:buttonClicked(2))
button2.grid(row=1,column=2)

button3=Button(root,activebackground= "gray",text="3",height=2,width=2,command=lambda:buttonClicked(3))
button3.grid(row=1,column=3)

button4=Button(root,height=2,width=2,text="4",command=lambda:buttonClicked(4))
button4.grid(row=2,column=1)

button5=Button(root,activebackground= "gray",height=2,width=2,text="5",command=lambda:buttonClicked(5))
button5.grid(row=2,column=2)

button6=Button(root,height=2,width=2,text="6",command=lambda:buttonClicked(6))
button6.grid(row=2,column=3)

button7=Button(root,activebackground= "gray",height=2,width=2,text="7",command=lambda:buttonClicked(7))
button7.grid(row=3,column=1)

button8=Button(root,height=2,width=2,text="8",command=lambda:buttonClicked(8))
button8.grid(row=3,column=2)

button8=Button(root,activebackground= "gray",height=2,width=2,text="9",command=lambda:buttonClicked(9))
button8.grid(row=3,column=3)


root.mainloop()
