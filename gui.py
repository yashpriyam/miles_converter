from tkinter import *  #import * = import all from tkinter

window=Tk()     #it creates a window// 'Tk' is correct not 'tk'
def km_to_miles():
       #e1_value is an object, .get is a function to get the string entrered in entry widget
    miles=float(e1_value.get())*1.6
    t1.delete("1.0", END)
    t1.insert(END,miles)   #to put the value entered in text widget at the end of it.what'er you enter in entry widget you get that in text

b1=Button(window,text="convert",command=km_to_miles)   #defining a variable, button creates a button in windows with name 'execute' written on it and we can pass 'text' in it
                                                        #command function helps you execute any function through your button
b1.grid(row=0,column=0)       #b1.pack() places the button in the window or can use b1.grid(row=0,column=0)#much better method

e1_value=StringVar()    #StringVar is a fuction to denote e1_value is a string variable
e1=Entry(window,textvariable=e1_value)    #creates entry bar in your window where you can type in any data (text),textvariable ensures it is a text
e1.grid(row=1,column=1)     #rows=(),column=() decide place of the button in the window
e1=Label(window,text="kms")
e1.grid(row=1,column=0)

t1=Text(window,height=1,width=20)  #height=(),width=() decides size of the widget in your window
t1.grid(row=1,column=3)
e2=Label(window,text="miles")
e2.grid(row=0,column=3)

window.mainloop()   #all the program written between these window commands is shown in the window
