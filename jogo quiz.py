from tkinter import *
janela= Tk()
import tkinter as tk


#Parágrafo 1
lb=Label (janela,text="Seja bem- vindo ao Jogo Quiz!Vamos testar seu conhecimento sobre Ensino Básico!")
lb.place(x=150, y=20)

#Parágrafo 2
lb=Label (janela,text="Vamos começar!")
lb.place(x=300, y=60)

#Definição do botão para Pergunta 1
def button_click1():
    print("bt_click1")
    lb["text"]= "Você Errou!:( \n São 8 planetas. Mercúrio, Vênus, Terra, Marte\nJúpiter, Saturno, Urano e Netuno"

def button_click2():
    print("bt_click2")
    lb["text"]= "Você acertou!Muito bem! :)"

#Pergunta1
lb=Label (janela,text="1-Quantos planetas compõem o sistema solar?",bg="Light blue")
lb.place(x=20, y=100)

#Botão a
bt= Button(janela, width=20, text="A) 9", command= button_click1)
bt.place(x=20, y=130)
lb=Label (janela,text="Essa é muito fácil!",bg="Light blue")
lb.place(x=300, y=145)


#Botão b
bt= Button(janela, width=20, text="B) 10",command= button_click1)
bt.place(x=20, y=160)

#Botão c
bt= Button(janela, width=20, text="C) 8",command= button_click2)
bt.place(x=20, y=190)

#Botão d
bt= Button(janela, width=20, text="D) 7",command= button_click1)
bt.place(x=20, y=220)

  
#Definição do Botão para pergunta 2
def button_click3():
    print("bt_click3")
    lb2["text"]= "Você Errou!:(\n Foi na Bahia, onde fica localizada a praia de Porto Seguro"

def button_click4():
    print("bt_click4")
    lb2["text"]= "Você acertou!Muito bem! :)"

#Pergunta2
lb2=Label (janela,text="2-Em relação ao descobrimento do Brasil,em qual Estado aconteceu o primeiro desembarque de Pedro Álvares Cabral?",bg="Light blue")
lb2.place(x=20, y=250)

#Botão a
bt= Button(janela, width=20, text="A) Rio de Janeiro", command= button_click3)
bt.place(x=20, y=278)
lb2=Label (janela,text="Essa é muito fácil!",bg="Light blue")
lb2.place(x=300, y=300)


#Botão b
bt= Button(janela, width=20, text="B) Minas Gerais",command= button_click3)
bt.place(x=20, y=308)

#Botão c
bt= Button(janela, width=20, text="C) Pernambuco",command= button_click3)
bt.place(x=20, y=338)

#Botão d
bt= Button(janela, width=20, text="D) Bahia",command= button_click4)
bt.place(x=20, y=368)


#Definição do Botão para pergunta 3
def button_click5():
    print("bt_click5")
    lb3["text"]= "Você Errou!:(\n Foi a Lei Áurea, sancionada pela Princesa Isabel\nno dia 13 de Maio de 1888"

def button_click6():
    print("bt_click6")
    lb3["text"]= "Você acertou!Muito bem! :)"

#Pergunta3
lb3=Label (janela,text="3-Qual o nome da lei assinada pela Princesa Isabel responsável por abolir completamente a escravidão no Brasil?",bg="Light blue")
lb3.place(x=20, y=400)

#Botão a
bt= Button(janela, width=20, text="A) Lei Áurea", command= button_click6)
bt.place(x=20, y=428)
lb3=Label (janela,text="Cuidado para não se confundir!",bg="Light blue")
lb3.place(x=300, y=450)


#Botão b
bt= Button(janela, width=20, text="B)Lei do Ventre Livre",command= button_click5)
bt.place(x=20, y=458)

#Botão c
bt= Button(janela, width=20, text="C)Lei dos Sexagenários",command= button_click5)
bt.place(x=20, y=488)

#Botão d
bt= Button(janela, width=20, text="D)Lei da Áurea Livre",command= button_click5)
bt.place(x=20, y=518)


def janela2(): 
      
    
    
    novajanela = Toplevel(janela) 
  
    
    
    novajanela.title("Jogo Quiz") 
    novajanela["bg"]=  "light blue"
    novajanela["background"]= "light blue"
  
    
    novajanela.geometry("800x600+200+200") 

    label=Label (novajanela,text="Vamos para mais perguntas!")
    label.place(x=250, y=20)

    #Pergunta 4
    label=Label (novajanela,text="4-Como se lê a potência 3³?",bg="Light blue")
    label.place(x=20, y=100)

    
    #Definição dos botões pergunta 4
    def button_click7():
        print("bt_click1")
        label["text"]= "Você Errou!:(\n A resposta correta é a B\n3 elevado ao cubo"

    def button_click8():
        print("bt_click2")
        label["text"]= "Você acertou!Muito bem! :)"
            
#Botão a
    btn2= Button(novajanela, width=22, text="A) 3 elevado ao triplo", command= button_click7)
    btn2.place(x=20, y=130)
    label=Label (novajanela,text="Essa é muito fácil!",bg="Light blue")
    label.place(x=300, y=145)


#Botão b
    btn2= Button(novajanela, width=22, text="B) 3 elevado ao cubo",command= button_click8)
    btn2.place(x=20, y=160)

#Botão c
    btn2= Button(novajanela, width=22, text="C) 3x3",command= button_click7)
    btn2.place(x=20, y=190)

#Botão d
    btn2= Button(novajanela, width=22, text="D) 3 elevado ao quadrado",command= button_click7)
    btn2.place(x=20, y=220)


    #Pergunta 5
    label2=Label (novajanela,text="5-Qual a fórmula do Dióxido de Carbono?'",bg="Light blue")
    label2.place(x=20, y=255)

    #Definição dos botões pergunta 5
    def button_click9():
        print("bt_click1")
        label2["text"]= "Você Errou!:(\n A resposta correta é a letra D\n Também conhecido como Gás Carbônico"

    def button_click10():
        print("bt_click2")
        label2["text"]= "Você acertou!Muito bem! :)"


#Botão a
    btn2= Button(novajanela, width=22, text="A) H2O", command= button_click9)
    btn2.place(x=20, y=290)
    label2=Label (novajanela,text="Essa é muito fácil!",bg="Light blue")
    label2.place(x=300, y=320)


#Botão b
    btn2= Button(novajanela, width=22, text="B) Ca",command= button_click9)
    btn2.place(x=20, y=320)

#Botão c
    btn2= Button(novajanela, width=22, text="C) NaCl",command= button_click9)
    btn2.place(x=20, y=350)

#Botão d
    btn2= Button(novajanela, width=22, text="D) CO2",command= button_click10)
    btn2.place(x=20, y=380)


    #Pergunta 6
    label3=Label (novajanela,text="6-Quais são os países do Eixo envolvidos na II Guerra Mundial?",bg="Light blue")
    label3.place(x=20, y=420)

    #Definição dos botões pergunta 6
    def button_click11():
        print("bt_click1")
        label3["text"]= "Você Errou!:(\nResposta correta:C\n Foram responsáveis pelo início do conflito armado."

    def button_click12():
        print("bt_click2")
        label3["text"]= "Você acertou!Muito bem! :)"


#Botão a
    btn2= Button(novajanela, width=32, text="A) Estados Unidos,França e Inglaterra", command= button_click11)
    btn2.place(x=20, y=450)
    label3=Label (novajanela,text="Essa é muito fácil!",bg="Light blue")
    label3.place(x=300, y=470)


#Botão b
    btn2= Button(novajanela, width=32, text="B) Polônia, Tchecoslováquia e Austria",command= button_click11)
    btn2.place(x=20, y=480)

#Botão c
    btn2= Button(novajanela, width=32, text="C) Alemanha, Itália e Japão",command= button_click12)
    btn2.place(x=20, y=510)

#Botão d
    btn2= Button(novajanela, width=32, text="D) Rússia,França e Inglaterra",command= button_click11)
    btn2.place(x=20, y=540)


#Botão próximo janela 2
    btn2=Button(novajanela, text="Próximo>>", command=janela3)
    btn2.pack(pady = 10) 
    btn2.place(x=500, y=550)

#Definição para janela 3

def janela3(): 
      
    
    
    novajanela3 = Toplevel(janela) 
  
    
    
    novajanela3.title("Jogo Quiz") 
    novajanela3["bg"]=  "light blue"
    novajanela3["background"]= "light blue"
  
    
    novajanela3.geometry("800x600+200+200") 

    label=Label (novajanela3,text="Últimas perguntas!")
    label.place(x=300, y=20)


    #Pergunta 7
    label4=Label (novajanela3,text="7-Você não vai sair de casa hoje,___?",bg="Light blue")
    label4.place(x=20, y=80)

    #Definição dos botões pergunta 7
    def button_click13():
        print("bt_click1")
        label4["text"]= "Você Errou!:(\nResposta correta:Letra A\nÉ usado no final das frases interrogativas. "

    def button_click14():
        print("bt_click2")
        label4["text"]= "Você acertou!Muito bem! :)"


#Botão a
    btn2= Button(novajanela3, width=25, text="A) Por quê", command= button_click14)
    btn2.place(x=20, y=110)
    label4=Label (novajanela3,text="Essa é muito fácil!",bg="Light blue")
    label4.place(x=300, y=150)


#Botão b
    btn2= Button(novajanela3, width=25, text="B) Por que",command= button_click13)
    btn2.place(x=20, y=140)

#Botão c
    btn2= Button(novajanela3, width=25, text="C) Porquê",command= button_click13)
    btn2.place(x=20, y=170)

#Botão d
    btn2= Button(novajanela3, width=25, text="D) Porque",command= button_click13)
    btn2.place(x=20, y=200)


    #Pergunta 8

    label5=Label (novajanela3,text="8- Ana guardou 3/10 de seu salário na poupança e com 2/10 do salário ela pagou o aluguel. Assinale a alternativa que \napresenta a fração do que sobrou do salário de Ana",bg="Light blue")
    label5.place(x=20, y=240)

    #Definição dos botões pergunta 8
    def button_click15():
        print("bt_click1")
        label5["text"]= "Você Errou!:( Resposta correta:Letra C"

    def button_click16():
        print("bt_click2")
        label5["text"]= "Você acertou!Muito bem! :)"


#Botão a
    btn2= Button(novajanela3, width=25, text="A) 6/10", command= button_click15)
    btn2.place(x=20, y=290)
    label5=Label (novajanela3,text="Essa é muito fácil!",bg="Light blue")
    label5.place(x=300, y=300)


#Botão b
    btn2= Button(novajanela3, width=25, text="B) 4/10",command= button_click15)
    btn2.place(x=20, y=320)

#Botão c
    btn2= Button(novajanela3, width=25, text="C) 5/10",command= button_click16)
    btn2.place(x=20, y=350)

#Botão d
    btn2= Button(novajanela3, width=25, text="D) 3/10",command= button_click15)
    btn2.place(x=20, y=380)



    #Pergunta 9

    label6=Label (novajanela3,text="9- São objetos rochosos e metálicos que orbitam o Sol mas são pequenos demais para serem considerados planetas:",bg="Light blue")
    label6.place(x=20, y=410)

    #Definição dos botões pergunta 9
    def button_click17():
        print("bt_click1")
        label6["text"]= "Você Errou!:(\nResposta Correta: Asteróides\nSão objetos que orbitam o Sol e que\nnão se transformaram em um disco e não possuíam caldas\n como um cometa ativo"

    def button_click18():
        print("bt_click2")
        label6["text"]= "Você acertou!Muito bem! :)"


#Botão a
    btn2= Button(novajanela3, width=25, text="A) Satélites", command= button_click17)
    btn2.place(x=20, y=440)
    label6=Label (novajanela3,text="Essa é muito fácil!",bg="Light blue")
    label6.place(x=300, y=470)


#Botão b
    btn2= Button(novajanela3, width=25, text="B) Cometas",command= button_click17)
    btn2.place(x=20, y=470)

#Botão c
    btn2= Button(novajanela3, width=25, text="C) Asteróides",command= button_click18)
    btn2.place(x=20, y=500)

#Botão d
    btn2= Button(novajanela3, width=25, text="D) Estrelas",command= button_click17)
    btn2.place(x=20, y=530)






    
#Botão próximo
btn = Button(janela, text ="Próximo>>", command = janela2) 
btn.pack(pady = 10) 
btn.place(x=500, y=550)


#janela principal
janela.title("Jogo Quiz-Teste de conhecimento de Ensino Básico")
janela["bg"]=  "light blue"
janela["background"]= "light blue"
janela.geometry("800x600+200+200")



janela.update()

janela.mainloop()
