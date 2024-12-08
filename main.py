import customtkinter as ctk # importando a biblioteca customtkinter

class main (ctk.CTk) :
  def __init__(self) :
    super().__init__()

    self.geometry ("400x400") # definindo as dimensões da janela
    self.title ("window")     # titulo da janela

    # criando um label
    self.lbl = ctk.CTkLabel (
        master="self",
        text="hello, world"
    )
    
    self.lbl.pack(padx=0,pady=20)

app = main()
app.mainloop()
