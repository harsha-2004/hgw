from tkinter import*
#from pil import Image
root=Tk()
root.title("MECHANICS")
root.geometry("700x700")

def fbd():
    new_window=Toplevel(root)
    title=Label(new_window,text="FREE BODY DIAGRAM",font="arial 32")
    title.place(x=400,y=50)
    Button(new_window,text="close me",command=lambda: new_window.destroy()).place(x=200,y=200)
    img_1=PhotoImage(name="image_1",file="C:\\Users\\himaj\\OneDrive\\Desktop\\s1\\Screenshot (228).png")
    label=Label(new_window,image=img_1)
    label.pack(padx=200,pady=250,side=RIGHT)
    new_window.mainloop()

def caluculations():
     new_window=Toplevel(root)
     new_window.title("FBD")
     title=Label(new_window,text="CALUCULATION",font="arial 32")
     title.place(x=400,y=50)
def reset():
    lminvalue.set("")
    lmaxvalue.set("")
    lincvalue.set("")
    wminvalue.set("")
    wmaxvalue.set("")
    wincvalue.set("")
    

title=Label(root,text="SIMPLE PENDULUM",font="arial 32")
variable=Label(root,text="variable",font="arial 15")
minimum=Label(root,text="Min",font="arial 15")
maximum=Label(root,text="Max",font="arial 15")
increment=Label(root,text="INCREMENT",font="arial 15")

l=Label(root,text="L",font="arial 15")
w=Label(root,text="w",font="arial 15")

lminvalue=StringVar()
lmaxvalue=StringVar()
lincvalue=StringVar()
wminvalue=StringVar()
wmaxvalue=StringVar()
wincvalue=StringVar()

lminentry=Entry(root,textvariable=lminvalue,font="arial 20",width=8)
lmaxentry=Entry(root,textvariable=lmaxvalue,font="arial 20",width=8)
lincentry=Entry(root,textvariable=lincvalue,font="arial 20",width=8)
wminentry=Entry(root,textvariable=wminvalue,font="arial 20",width=8)
wmaxentry=Entry(root,textvariable=wmaxvalue,font="arial 20",width=8)
wincentry=Entry(root,textvariable=wincvalue,font="arial 20",width=8)


title.place(x=550,y=50)
variable.place(x=265,y=250)
minimum.place(x=650,y=250)
maximum.place(x=950,y=250)
increment.place(x=1150,y=250)
l.place(x=275,y=300)
w.place(x=275,y=400)

lminentry.place(x=605,y=300)
lmaxentry.place(x=910,y=300)
lincentry.place(x=1150,y=300)
wminentry.place(x=605,y=400)
wmaxentry.place(x=910,y=400)
wincentry.place(x=1150,y=400)


Button(text="FBD",font="arial 20",command=fbd).place(x=300,y=500)
Button(text="calulations",font="arial 20",command=caluculations).place(x=500,y=500)
Button(text="Reset",font="arial 20",command=reset).place(x=800,y=500)
Button(text="close me",font="arial 20",command=lambda: root.destroy()).place(x=1100,y=500)

'''file='C:\\Users\\himaj\\OneDrive\\Desktop\\s1\\R.gif'
info = Image.open(file)
frames = info.n_frames
print(frames)
im=[PhotoImage(file=file,format=f'gif -index {i}')for i in range(frames)]
anim = none
count=0
def animation(count):
    global anim
    im2=im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frame:
        count = 0

    anim = root.after(50,lambda :animation(count))
def stop_animation():
    global anim
    root.after_cancel(anim)
    
gif_label=Label(image="")
gif_label.pack(padx=600,pady=50,side=RIGHT)

start=Button(text="start",command=lambda :animation(count))
start.place(x=1250,y=600)
stop=Button(text="stop",command=stop_animation)
stop.place(x=1275,y=600)'''


root.mainloop()
