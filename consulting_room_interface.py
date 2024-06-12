import tkinter as tk

janela = tk.Tk()
janela.title("Consultório")
janela.geometry("1000x500")


frame1 = tk.Frame(janela)
frame2 = tk.Frame(janela)

def login():
    frame2.pack_forget()
    frame1.pack()

def login_feito():
    frame1.pack_forget()
    frame2.pack()

cpf_label = tk.Label(frame1, text="Informe seu CPF:")
cpf_label.pack(padx=5)

cpf = tk.Entry(frame1, width=25)
cpf.pack(padx=5, pady=5)

senha_label = tk.Label(frame1, text="Informe sua senha:")
senha_label.pack(padx=5)

senha = tk.Entry(frame1, width=25)
senha.pack(padx=5, pady=5)

btn_login = tk.Button(frame1, text="Login", width=15, command=login_feito)
btn_login.pack()

btn_home = tk.Button(frame2, text="inicial", width=15, command=login)
btn_home.pack()

frame1.pack()

janela.mainloop()