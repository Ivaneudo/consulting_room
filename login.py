import tkinter as tk
janela =tk.Tk()
janela.title("Login")
janela.geometry("500x500")

user_1 = tk.Label(janela, text="Digite seu tipo de usuário")
user_1.pack()

adm = tk.Radiobutton(janela, text="Administrador") #? Preciso fazer com que isso fique com o valor vazio.
adm.pack()
med = tk.Radiobutton(janela, text="Médico")
med.pack()
sec = tk.Radiobutton(janela, text="Secretario")
sec.pack()
pas = tk.Radiobutton(janela, text="Pasciente")
pas.pack()

email_1 = tk.Label(janela, text="Digite seu e-mail")
email_1.pack()
email =  tk.Entry(janela)
email.pack()







janela.mainloop()