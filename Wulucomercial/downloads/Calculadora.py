#CALCULADORA SUPER MAX
from tkinter import *





janela =Tk()
janela.title('Calculadora')



def botao(clicado):
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(atual) + str(clicado))

def deitar():
    entrada.delete(0, END)

def deitar1():
    entrada.delete(0, 1)


def somar():
    atual = entrada.get()
    global numeros
    global operacao
    operacao = 'soma'
    numeros = int(atual)
    entrada.delete(0, END)

def subtrair():
    atual = entrada.get()
    global numeros
    global operacao
    numeros = int(atual)
    operacao = 'sub'
    entrada.delete(0, END)

def div():
    atual = entrada.get()
    global numeros
    global operacao
    operacao = 'div'
    numeros= int(atual)
    entrada.delete(0, END)

def mult():
    atual =  entrada.get()
    global numeros
    global operacao
    operacao = 'mult'
    numeros = int(atual)
    entrada.get()

def igual():
    atual = entrada.get()
    entrada.delete(0, END)

    if operacao == 'soma':
        entrada.insert(0, numeros + int(atual))
    elif operacao == 'sub':
        entrada.insert(0, numeros - int(atual))
    elif operacao == 'div':
        entrada.insert(0, numeros / float(atual))
    else:
        entrada.insert(0, numeros * int(atual))

entrada = Entry(janela, justify='right', background='#fff',font=('arial', 18))
entrada.grid(row=0, column=0)
b1 = Button(janela, text='1', width=2, font=('arial', 18), command=lambda:botao(1))
b1.grid(row=0, column=1)
b2 = Button(janela, text='2', width=2, font=('arial', 18), command=lambda:botao(2))
b2.grid(row=0, column=2)
b3 = Button(janela, text='3', width=2, font=('arial', 18), command=lambda:botao(3))
b3.grid(row=0, column=3)
b4 = Button(janela, text='4', width=2, font=('arial', 18), command=lambda:botao(4))
b4.grid(row=1, column=1)
b5 = Button(janela, text='5', width=2, font=('arial', 18), command=lambda:botao(5))
b5.grid(row=1, column=2)
b6 = Button(janela, text='6', width=2, font=('arial', 18), command=lambda:botao(6))
b6.grid(row=1, column=3)
b7 = Button(janela, text='7', width=2, font=('arial', 18), command=lambda:botao(7))
b7.grid(row=2, column=1)
b8 = Button(janela, text='8', width=2, font=('arial', 18), command=lambda:botao(8))
b8.grid(row=2, column=2)
b9 = Button(janela, text='9', width=2, font=('arial', 18), command=lambda:botao(9))
b9.grid(row=2, column=3)
b0 = Button(janela, text='0', width=5, font=('arial', 18), command=lambda:botao(0))
b0.grid(row=2, column=4)
eliminar = Button(janela, text='C', width=5, font=('arial', 18, 'bold'), background='red', activebackground='red', command=deitar)
eliminar.grid(row=4, column=5)
eliminar1 = Button(janela, text='B', width=5, font=('arial', 18, 'bold'), background='yellow', activebackground='yellow', command=deitar1)
eliminar1.grid(row=4, column=4)
igual = Button(janela, text='=', width=5, font=('arial', 20), background='green', activebackground='green', command= igual)
igual.grid(row=2, column=5)
mais = Button(janela, text='+', width=5, font=('arial', 20), command=somar)
mais.grid(row=0,column=4)
menos = Button(janela, text='-', width=5, font=('arial', 20), command=subtrair)
menos.grid(row=0,column=5)
div = Button(janela, text='/', width=5, font=('arial', 20), command=div)
div.grid(row=1,column=4)
mult = Button(janela, text='*', width=5, font=('arial', 20), command=mult)
mult.grid(row=1,column=5)
lb1 = Label(janela, text='HISTORICO')
lb1.grid(row=3, column=0)

janela.mainloop()