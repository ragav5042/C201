from tkinter import *
window=Tk()

window.title('Simple Intrest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculatedsi():
    principal= float(principal_entry.get())
    rate= float(rate_entry.get())
    time= float(time_entry.get())
    i=(principal*rate*time)/100
    intrest=round(i,2)
    name=username.get()
    result_label.destroy()

    outputmsg= Label(result_frame,text=name+", Your Intrest "+str(intrest), bg = "lightcyan", font=("Calibri", 12), width=42)    
    outputmsg.place(x=20,y=40)
    outputmsg.pack()
    

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principal_label=Label(window, text="Enter principal amont ", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principal_label.place(x=20, y=140)

principal_entry=Entry(window, text="", bd=2, width=10)
principal_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter rate of interest ", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=10)
rate_entry.place(x=150, y=187)    

time_label=Label(window, text="Enter time period ", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=220)

time_entry=Entry(window, text="", bd=2, width=10 )
time_entry.place(x=150, y=225)  

calculateBtn = Button(window, text="Submit" ,fg="black" , bg="cyan" , bd=4,command=calculatedsi)
calculateBtn.place(x=20,y=250)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()