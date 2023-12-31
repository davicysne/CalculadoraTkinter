from tkinter import *


def limpar():
    display.delete(0,END)

def inserir(valor):
    display.insert(END, valor)

def calcular():
    text_display = display.get()
    resultado = eval(text_display)
    display.delete(0, END)
    limpar()
    display.insert(0, str(resultado))





window = Tk()
window.title("Calculadora")

display = Entry(window, font = "Arial 20 bold", bg = "#1c3ec7",
                fg = "white", width=19)

display.pack()

panel = Frame(window)

btn_0 = Button(panel, background="orange", bd= 0, text= '0', 
               font= "Arial 16 bold", width=5,height=3, command=lambda: inserir("0"))
btn_1 = Button(panel, background="orange", bd= 0, text= '1', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("1"))
btn_2 = Button(panel, background="orange", bd= 0, text= '2', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("2"))
btn_3 = Button(panel, background="orange", bd= 0, text= '3', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("3"))
btn_4 = Button(panel, background="orange", bd= 0, text= '4', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("4"))
btn_5 = Button(panel, background="orange", bd= 0, text= '5', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("5"))
btn_6 = Button(panel, background="orange", bd= 0, text= '6', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("6"))
btn_7 = Button(panel, background="orange", bd= 0, text= '7', 
               font= "Arial 16 bold", width=5,height=3,command= lambda: inserir("7"))
btn_8 = Button(panel, background="orange", bd= 0, text= '8', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("8"))
btn_9 = Button(panel, background="orange", bd= 0, text= '9', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("9"))

btn_limpar = Button(panel, background="orange", bd= 0, text= 'C', 
               font= "Arial 16 bold", width=5,height=3, command=limpar)

btn_igual = Button(panel, background="orange", bd= 0, text= '=', 
               font= "Arial 16 bold", width=5,height=3,
               command=calcular)

btn_sum = Button(panel, background="orange", bd= 0, text= '+', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("+"))

btn_sub = Button(panel, background="orange", bd= 0, text= '-', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("-"))

btn_mult = Button(panel, background="orange", bd= 0, text= '*', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("*"))

btn_div = Button(panel, background="orange", bd= 0, text= '/', 
               font= "Arial 16 bold", width=5,height=3, command= lambda: inserir("/"))





panel.pack()

btn_7.grid(row=0,column=0)
btn_8.grid(row=0,column=1)
btn_9.grid(row=0,column=2)
btn_mult.grid(row=0,column=3)


btn_4.grid(row=1, column=0)
btn_5.grid(row=1,column=1)
btn_6.grid(row=1,column=2)
btn_sub.grid(row=1,column=3)

btn_1.grid(row=2,column=0)
btn_2.grid(row=2,column=1)
btn_3.grid(row=2,column=2)
btn_sum.grid(row=2,column=3)

btn_div.grid(row=3,column=0)
btn_limpar.grid(row=3,column=1)
btn_0.grid(row=3,column=2)
btn_igual.grid(row=3,column=3)



window.mainloop()



