from tkinter import *
root=Tk()
nameg=""
emailg=""
ageg=""
phoneg=""
genderg=""                   
font_size=20
font=("arial",font_size,"bold")
def func():
    global nameg,emailg,ageg,phoneg,genderg
    nameg=namee.get()
    emailg=emaile.get()
    ageg=agee.get()
    phoneg=phonee.get()
    genderg=genvar.get()
    on_click()
def on_click():
    parent=Toplevel()
    namep=Label(parent,text="Name: "+nameg)
    namep.grid(row=1,column=0,padx=10,pady=10)
    emailp=Label(parent,text="Email ID: "+ageg)
    emailp.grid(row=2,column=0,padx=10,pady=10)
    agep=Label(parent,text="Age: "+ageg)
    agep.grid(row=3,column=0,padx=10,pady=10)
    phonep=Label(parent,text="Phone: "+phoneg)
    phonep.grid(row=4,column=0,padx=10,pady=10)
    genderp=Label(parent,text="Gender: "+genderg)
    genderp.grid(row=5,column=0,padx=10,pady=10)    
for i in range(20):
    root.grid_rowconfigure(i,weight=1)
for j in range(20):
    root.grid_columnconfigure(j,weight=1)
login=Label(root,text="LOGIN PAGE",font=font)
login.grid(row=1,column=10)
f=Frame(root,width=100,highlightbackground="black", highlightthickness=3)
f.grid(row=2,column=10,padx=10,pady=20,ipadx=10,ipady=30)
name=Label(f,text="Name")
name.grid(row=6,column=7,padx=20,pady=20)
namee=Entry(f,width=30)
namee.grid(row=6,column=10,padx=20,pady=20)
email=Label(f,text="Email ID")
email.grid(row=7,column=7,padx=20,pady=20)
emaile=Entry(f,width=30)
emaile.grid(row=7,column=10,padx=20,pady=20)
age=Label(f,text="Age")
age.grid(row=8,column=7,padx=20,pady=20)
agee=Entry(f,width=30)
agee.grid(row=8,column=10,padx=20,pady=20)
phone=Label(f,text="Phone No.")
phone.grid(row=9,column=7,padx=20,pady=20)
phonee=Entry(f,width=30)
phonee.grid(row=9,column=10,padx=20,pady=20)
gender=Label(f,text="Gender")
gender.grid(row=10,column=7,pady=20)
genvar=StringVar()
genderf=Radiobutton(f,text="Male",variable=genvar,value="Male")
genderf.grid(row=10,column=9)
genderm=Radiobutton(f,text="Female",variable=genvar,value="Female")
genderm.grid(row=10,column=10)
save=Button(f,text="click to save",width=15,command=func)
save.place(x=130,y=330)
root.mainloop()

