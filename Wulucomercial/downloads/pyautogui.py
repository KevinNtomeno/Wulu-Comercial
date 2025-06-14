from pyautogui import *
from time import sleep
press('winleft')
sleep(0.5)
write('Text Editor', 0.1)

try:
    local = locateOnScreen('/home/kv/Documentos/Vs Code Pasta/python/Projectos Pessoais/PyAutoGui/editor.png')
    leftClick(local)
    sleep(2)
    press('f11')
    sleep(1)
    write(""" import sqlite3 as sq
from tkinter import *
from PIL import *
import ttkbootstrap as tb
import pymsgbox as box
def cadrastar():
    nome2 = str(nome.get()).upper().lstrip().rstrip()
    idade2 = int(idade.get())
    classe2 = int(classe.get())
    lb2.config(text='''CADRASTO CONCLUIDO
            
            ''', fg='green')
    conn = sq.connect('Virtual Db.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sacrinor (
nome TEXT NOT NULL,
idade INT,
classe INT)''')
    cursor.execute('INSERT INTO sacrinor VALUES (?, ?, ?)', (nome2, idade2, classe2))
    conn.commit()
    cursor.fetchall()
    box.alert('CADRASTO FEITO COM SUCESSO!')
    nome.delete(0, END)
    idade.delete(0, END)
    classe.delete(0, END)
    def deitar():
        nome.delete(0, END)
        idade.delete(0, END)
        classe.delete(0, END)
        nome.after(5000, deitar)
        idade.after(5000, deitar)
        classe.after(5000, deitar)

def deletar():
    nome2 = str(nome.get()).upper().lstrip().rstrip()
    conn = sq.connect('Virtual Db.db')
    cursor = conn.cursor()
    cursor.execute(f'''DELETE FROM sacrinor WHERE nome = '{nome2}' ''')
    conn.commit()
    cursor.fetchall()
    lb3['text'] = 'ALUNO REMOVIDO COM SUCESSO!'

def achar():
    nome2 = str(nome.get()).upper().lstrip().rstrip()
    conn = sq.connect('Virtual Db.db')
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM sacrinor WHERE nome = '{nome2}' ''')
    conn.commit()
    kv  = cursor.fetchall()
    lb3['text'] = kv

    

def lista():

    listas = Tk()
    listas.title('LISTAS')
    listas.geometry('300x300')
    lb4 = Label(listas, text='listas aqui', font=('arial', 12))
    lb4.pack()
    lb5 = Button(listas, text='SAIR', activebackground='red', command=listas.destroy)
    lb5.pack()
    conn = sq.connect('Virtual Db.db')
    cursor = conn.cursor()
    cursor.fetchall()
    se = cursor.execute('SELECT * FROM sacrinor')
    for se1 in se:
        lb4['text'] = f'{se1}'
        print('''NOME -- IDADE -- CLASSE''')
        print(se1)





janela = tb.Window(themename='superhero')
janela.geometry('700x600')
janela.title('CADRASTO NTOMENO')
lb1 = Label(janela, text='CADRASTO', font=('Arial', 20, 'bold'))
lb1.grid(row=0, column=1, pady=10)
lb2 = Label(janela, text='''Insira os dados do Aluno
            
            ''')
lb2.grid(row=1, column=1)

nome = tb.Entry(janela, font=('arial', 30), bootstyle='danger')
nome.grid(row=2, column=1, padx=30)
nome1 = Label(janela, text='Nome: ', font=('arial', 14))
nome1.grid(row=2, column=0, padx=30)

idade = tb.Entry(janela, font=('arial', 30), bootstyle='danger')
idade.grid(row=3, column=1, padx=30)

idade1 = Label(janela, text='Idade: ', font=('arial', 14))
idade1.grid(row=3, column=0, pady=30)

classe = tb.Entry(janela, font=('arial', 30), bootstyle='danger')
classe.grid(row=4, column=1, padx=30)

classe1 = Label(janela, text='Classe: ', font=('arial', 14))
classe1.grid(row=4, column=0, pady=30)

bt_cadrastar = tb.Button(janela, text='CADRASTAR', width=10, bootstyle='success outline', command=cadrastar)
bt_cadrastar.grid(row=5, column=1, pady=30)


bt_deletar = tb.Button(janela, text='REMOVER', width=10, command=deletar, bootstyle='danger outline')
bt_deletar.place(x=170, y=370)

bt_achar = tb.Button(janela, text='LOCALIZAR', width=10, bootstyle='info outline', command=achar)
bt_achar.place(x=480, y=370)

lb3 = Label(janela, text='DADOS ', font=('arial', 16))
lb3.grid(row=6, column=1, pady=20)
#lb3.place(x=250, y=500)
bt_lista = Button(janela, text='LISTA', activebackground='yellow', relief='groove', font=('arial', 18), command=lista)
bt_lista.grid(row=7, column=1)

sair = Button(janela, text='SAIR', activebackground='red', command=janela.quit)
sair.place(x=50, y=50)




janela.mainloop()""", 0.3)
except:
    print('Not found')
