from tkinter import *
from tkinter import messagebox
import math as m

screen = Tk()
screen.title('AP')
screen.geometry('432x445')
screen.maxsize(width='432',height='445')
screen.minsize(width='432',height='445')
screen.configure(bg='blue')
screen.iconbitmap('Calculator.ico')

def click(number):
    global operator
    operator += str(number)
    txt.set(operator)

def fsqrt():
    try:
        global operator
        result = m.sqrt(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Please input value before performing sqrt operation on it',parent=screen)

def fln():
    try:
        global operator
        result = m.log(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Please input the value before performing ln on it',parent=screen)

def ffact():
    try:
        global operator
        result = m.factorial(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Please input the value before performing factorial operation',parent=screen)

def flog():
    try:
        global operator
        result = m.log10(eval(operator))
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','Please input the value before performing log operation',parent=screen)

def clear():
    global operator
    operator = ''
    txt.set(operator)

def equal():
    try:
        global operator
        result = eval(operator)
        operator = str(result)
        txt.set(operator)
    except:
        messagebox.showinfo('Notification','PLease input some values',parent=screen)

def on_enter7(a):
    btn7.configure(bg='orange')
def on_leave7(a):
    btn7.configure(bg='pink')

def on_enter8(a):
    btn8.configure(bg='orange')
def on_leave8(a):
    btn8.configure(bg='pink')

def on_enter9(a):
    btn9.configure(bg='orange')
def on_leave9(a):
    btn9.configure(bg='pink')

def on_enteradd(a):
    btnadd.configure(bg='orange')
def on_leaveadd(a):
    btnadd.configure(bg='pink')

def on_enter4(a):
    btn4.configure(bg='orange')
def on_leave4(a):
    btn4.configure(bg='pink')

def on_enter5(a):
    btn5.configure(bg='orange')
def on_leave5(a):
    btn5.configure(bg='pink')

def on_enter6(a):
    btn6.configure(bg='orange')
def on_leave6(a):
    btn6.configure(bg='pink')

def on_entersbt(a):
    btnsbt.configure(bg='orange')
def on_leavesbt(a):
    btnsbt.configure(bg='pink')

def on_enter1(a):
    btn1.configure(bg='orange')
def on_leave1(a):
    btn1.configure(bg='pink')

def on_enter2(a):
    btn2.configure(bg='orange')
def on_leave2(a):
    btn2.configure(bg='pink')

def on_enter3(a):
    btn3.configure(bg='orange')
def on_leave3(a):
    btn3.configure(bg='pink')

def on_entermlt(a):
    btnmlt.configure(bg='orange')
def on_leavemlt(a):
    btnmlt.configure(bg='pink')

def on_enter0(a):
    btn0.configure(bg='orange')
def on_leave0(a):
    btn0.configure(bg='pink')

def on_enterclear(a):
    btnclear.configure(bg='orange')
def on_leaveclear(a):
    btnclear.configure(bg='pink')

def on_enterequal(a):
    btnequal.configure(bg='orange')
def on_leaveequal(a):
    btnequal.configure(bg='pink')

def on_enterdiv(a):
    btndiv.configure(bg='orange')
def on_leavediv(a):
    btndiv.configure(bg='pink')

def on_enterdec(a):
    btndec.configure(bg='orange')
def on_leavedec(a):
    btndec.configure(bg='pink')

def on_enterrbc(a):
    btnrbc.configure(bg='orange')
def on_leaverbc(a):
    btnrbc.configure(bg='pink')

def on_enterlbc(a):
    btnlbc.configure(bg='orange')
def on_leavelbc(a):
    btnlbc.configure(bg='pink')

def on_entersqrt(a):
    btnsqrt.configure(bg='orange')
def on_leavesqrt(a):
    btnsqrt.configure(bg='pink')

def on_enterlog(a):
    btnlog.configure(bg='orange')
def on_leavelog(a):
    btnlog.configure(bg='pink')


txt = StringVar()
operator = ''

entry1 = Entry(screen,bg='light blue',font=('arial',20,'italic bold'),bd=20,justify='right',textvariable=txt)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,bg='pink',text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(7),activebackground='light yellow',activeforeground='purple')
btn7.grid(row=1,column=0)

btn8 = Button(screen,bg='pink',text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(8),activebackground='light yellow',activeforeground='purple')
btn8.grid(row=1,column=1)

btn9 = Button(screen,bg='pink',text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(9),activebackground='light yellow',activeforeground='purple')
btn9.grid(row=1,column=2)

btnadd = Button(screen,bg='pink',text='+',font=('arial',20,'italic bold'),bd=8,padx=14,pady=12,command=lambda:click('+'),activebackground='light yellow',activeforeground='purple')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,bg='pink',text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(4),activebackground='light yellow',activeforeground='purple')
btn4.grid(row=2,column=0)

btn5 = Button(screen,bg='pink',text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(5),activebackground='light yellow',activeforeground='purple')
btn5.grid(row=2,column=1)

btn6 = Button(screen,bg='pink',text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(6),activebackground='light yellow',activeforeground='purple')
btn6.grid(row=2,column=2)

btnsbt = Button(screen,bg='pink',text='-',font=('arial',20,'italic bold'),bd=8,padx=17,pady=12,command=lambda:click('-'),activebackground='light yellow',activeforeground='purple')
btnsbt.grid(row=2,column=3)

btn1 = Button(screen,bg='pink',text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(1),activebackground='light yellow',activeforeground='purple')
btn1.grid(row=3,column=0)

btn2 = Button(screen,bg='pink',text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(2),activebackground='light yellow',activeforeground='purple')
btn2.grid(row=3,column=1)

btn3 = Button(screen,bg='pink',text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(3),activebackground='light yellow',activeforeground='purple')
btn3.grid(row=3,column=2)

btnmlt= Button(screen,bg='pink',text='*',font=('arial',20,'italic bold'),bd=8,padx=17,pady=12,command=lambda:click('*'),activebackground='light yellow',activeforeground='purple')
btnmlt.grid(row=3,column=3)

btn0 = Button(screen,bg='pink',text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=12,command=lambda:click(0),activebackground='light yellow',activeforeground='purple')
btn0.grid(row=4,column=0)

btnrbc = Button(screen,bg='pink',text='!',font=('arial',20,'italic bold'),bd=8,padx=18,pady=12,command=lambda:ffact(),activebackground='light yellow',activeforeground='purple')
btnrbc.grid(row=4,column=1)

btnlbc = Button(screen,bg='pink',text='log',font=('arial',20,'italic bold'),bd=8,padx=5,pady=12,command=lambda:flog(),activebackground='light yellow',activeforeground='purple')
btnlbc.grid(row=4,column=2)

btndiv = Button(screen,bg='pink',text='/',font=('arial',20,'italic bold'),bd=8,padx=18,pady=12,command=lambda:click('/'),activebackground='light yellow',activeforeground='purple')
btndiv.grid(row=4,column=3)

btndec = Button(screen,bg='pink',text='.',font=('arial',20,'italic bold'),bd=8,padx=23,pady=12,command=lambda:click('.'),activebackground='light yellow',activeforeground='purple')
btndec.grid(row=4,column=4)

btnclear = Button(screen,bg='pink',text='c',font=('arial',20,'italic bold'),bd=8,padx=19,pady=11,command=lambda:clear(),activebackground='light yellow',activeforeground='purple')
btnclear.grid(row=0,column=4)

btnequal = Button(screen,bg='pink',text='=',font=('arial',20,'italic bold'),bd=8,padx=19,pady=12,command=lambda:equal(),activebackground='light yellow',activeforeground='purple')
btnequal.grid(row=1,column=4)

btnsqrt = Button(screen,bg='pink',text='sqrt',font=('arial',20,'italic bold'),bd=8,padx=2,pady=12,command=lambda:fsqrt(),activebackground='light yellow',activeforeground='purple')
btnsqrt.grid(row=2,column=4)

btnlog = Button(screen,bg='pink',text='ln',font=('arial',20,'italic bold'),bd=8,padx=15,pady=12,command=lambda:fln(),activebackground='light yellow',activeforeground='purple')
btnlog.grid(row=3,column=4)


###########################Binding cursor and buttons

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsbt.bind('<Enter>',on_entersbt)
btnsbt.bind('<Leave>',on_leavesbt)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmlt.bind('<Enter>',on_entermlt)
btnmlt.bind('<Leave>',on_leavemlt)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btndec.bind('<Enter>',on_enterdec)
btndec.bind('<Leave>',on_leavedec)

btnrbc.bind('<Enter>',on_enterrbc)
btnrbc.bind('<Leave>',on_leaverbc)

btnlbc.bind('<Enter>',on_enterlbc)
btnlbc.bind('<Leave>',on_leavelbc)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)



screen.mainloop()