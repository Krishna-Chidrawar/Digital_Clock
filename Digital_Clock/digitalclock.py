from tkinter import *
import time
clk=Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")
clk.configure(bg="#0C1E28")

def clock():
    hr=str(time.strftime("%H"))
    mn=str(time.strftime("%M"))
    sc=str(time.strftime("%S"))
    print(hr,mn,sc)
     

    #condition for am/pm!
    if int(hr)>12 and  int(mn)>0:
        lb_dn.config(text="PM")
    if int(hr)>12:
        hr= str(int(int(hr)-12))
    

    #configurations of the clock!
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)
    lb_hr.after(200,clock)          #to update clock according to current time


#hour window making
lb_hr =Label(clk,text="12",font=("Times 20 bold" ,75,'bold'),bg="#0875B7",fg="white")
lb_hr.place(x=350,y=200,width=150,height=150)
lb_hr_txt=Label(clk,text="Hour",font=("Times 20 bold",20,"bold"),bg="#0875B7",fg="white")
lb_hr_txt.place(x=350,y=360,width=150,height=50)

#minute window making
lb_mn =Label(clk,text="12",font=("Times 20 bold" ,75,'bold'),bg="#008EA4",fg="white")
lb_mn.place(x=520,y=200,width=150,height=150)
lb_mn_txt=Label(clk,text="Minute",font=("Times 20 bold",20,"bold"),bg="#008EA4",fg="white")
lb_mn_txt.place(x=520,y=360,width=150,height=50)

#second window making
lb_sc =Label(clk,text="12",font=("Times 20 bold" ,75,'bold'),bg="#06B4B8",fg="white")
lb_sc.place(x=690,y=200,width=150,height=150)
lb_sc_txt=Label(clk,text="Second",font=("Times 20 bold",20,"bold"),bg="#06B4B8",fg="white")
lb_sc_txt.place(x=690,y=360,width=150,height=50)

#noon window making
lb_dn =Label(clk,text="AM",font=("Times 20 bold" ,70,'bold'),bg="#9F0646",fg="white")
lb_dn.place(x=860,y=200,width=150,height=150)
lb_dn_txt=Label(clk,text="Noon",font=("Times 20 bold",20,"bold"),bg="#9F0646",fg="white")
lb_dn_txt.place(x=860,y=360,width=150,height=50)


clock()   #Final clcock function
clk.mainloop()   # To continue the loop for infinite time!

