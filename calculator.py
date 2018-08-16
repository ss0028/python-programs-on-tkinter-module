#Calculator program
#created by Shikha Singh
from tkinter import *
import tkinter.messagebox
calc=Tk()
calc.title("Calculator")
calc.resizable(width=False,height=False)

#def msg():
#    tkinter.messagebox.showinfo('using calculator:',"this is a simple calculator.Just press the desired buttons to perform the required actions!!!")


n=0.0
op=''
def click(num):
    global n
    if(num!='AC'):
        val=inp.get()+num
        inp.delete(0,"end")
        inp.insert(0,val)
    else:
        inp.delete(0,"end")
        n=0.0
def operator(x):
    global n
    global op
    try:
        if x!='=':
            n=float(inp.get())
            inp.delete(0,"end")

        if x=='+':
            op='+'
        elif x=='-':
            op='-'
        elif x=='*':
            op='*'
        elif x=='/':
            op='/'
        elif x=='=':
            if op=='+':
                ans=n + float(inp.get())
            elif op=='-':
                ans=n - float(inp.get())
            elif op=='*':
                ans=n * float(inp.get())
            elif op=='/':
                ans=n / float(inp.get())
            inp.delete(0,"end")
            if(op!=''):
                inp.insert(0,str(ans))
    except ValueError:
        display="error"
        inp.insert(0,display)
        inp.delete(0,"end")

inp=Entry(calc,width="20",font="aerial")
inp.grid(row=0,column=0,columnspan=4)

btn7=Button(calc,text="7",height="2",width="5",command=lambda:click("7")).grid(row="2",column="0")
btn8=Button(calc,text="8",height="2",width="5",command=lambda:click("8")).grid(row="2",column="1")
bt9=Button(calc,text="9",height="2",width="5",command=lambda:click("9")).grid(row="2",column="2")
btnDiv=Button(calc,text="/",height="2",width="5",command=lambda:operator("/")).grid(row="2",column="3")

btn4=Button(calc,text="4",height="2",width="5",command=lambda:click("4")).grid(row="3",column="0")
btn5=Button(calc,text="5",height="2",width="5",command=lambda:click("5")).grid(row="3",column="1")
btn6=Button(calc,text="6",height="2",width="5",command=lambda:click("6")).grid(row="3",column="2")
btnMultiply=Button(calc,text="*",height="2",width="5",command=lambda:operator("*")).grid(row="3",column="3")

btn1=Button(calc,text="1",height="2",width="5",command=lambda:click("1")).grid(row="4",column="0")
btn2=Button(calc,text="2",height="2",width="5",command=lambda:click("2")).grid(row="4",column="1")
btn3=Button(calc,text="3",height="2",width="5",command=lambda:click("3")).grid(row="4",column="2")
btnSubtract=Button(calc,text="-",height="2",width="5",command=lambda:operator("-")).grid(row="4",column="3")

btnClear=Button(calc,text="AC",height="2",width="5",command=lambda:click("AC")).grid(row="5",column="0")
btn0=Button(calc,text="0",height="2",width="5",command=lambda:click("0")).grid(row="5",column="1")
btnEqual=Button(calc,text="=",height="2",width="5",command=lambda:operator("=")).grid(row="5",column="2")
btnAdd=Button(calc,text="+",height="2",width="5",command=lambda:operator("+")).grid(row="5",column="3")

calc.mainloop()
