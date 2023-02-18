
#importa o pacote tkinter responsável pela GUI.
import tkinter as tk

root = tk.Tk()
root.title("Calculator")

#Constroi a tela onde serão inseridos os valores para calculo.
display = tk.Entry(root, font=("Helvetica", 20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

#Defini os botões numericos e de operações que serão exibidos na tela da calculadora
buttons = [
    "7", "8", "9", "+", "C",
    "4", "5", "6", "-", "*",
    "1", "2", "3", "/", "=",
    "0", ".", "(", ")", "%"
]
#Defini as posições de inicio da linha e da coluna
row = 1
col = 0

#Código para construir as colunas e linhas dos botões da calculadora. Defini e variavel x em uma função lambda que recebe o botão digitado
#e passa como parâmetro para a função calc().
for button in buttons:
    tk.Button(root, text=button, width=5, height=2,command=lambda x=button: calc(x)).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

#Função que realiza o calculo solicitado.
def calc(key):
    #If responsável por limpar a tela caso seja selecionado o botão C
    if key == "C":
        display.delete(0, tk.END)
    #Se for selecionado o botão de igual entrar para fazer
    elif key == "=":
        try:
            #Código responsável por realizar o calculo solicitado
            display.insert(tk.END, "=" + str(eval(display.get())))
        except:
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, key)

root.mainloop()
