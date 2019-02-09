import tkinter
import random


class minhaApp_tk(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid() #lbl
        self.lblC = tkinter.Label(self, text="Inteiro")
        self.lblC.grid(column=0, row=0)

        self.lblSep = tkinter.Label(self, text="<-->")
        self.lblSep.grid(column=1, row=0)

        self.lblF = tkinter.Label(self, text="Binario")
        self.lblF.grid(column=2, row=0)

        #segunda parte
        self.lblA = tkinter.Label(self, text="Inteiro")
        self.lblA.grid(column=0, row=4)

        self.lblSep = tkinter.Label(self, text="<-->")
        self.lblSep.grid(column=1, row=4)

        self.lblB = tkinter.Label(self, text="Octal")
        self.lblB.grid(column=2, row=4)

        #terceira parte
        self.lblZ = tkinter.Label(self, text="Inteiro")
        self.lblZ.grid(column=0, row=7)

        self.lblSep = tkinter.Label(self, text="<-->")
        self.lblSep.grid(column=1, row=7)

        self.lblX = tkinter.Label(self, text="Hexadecimal")
        self.lblX.grid(column=2, row=7)


        #entry
        self.entryC = tkinter.Entry(self)
        self.entryC.grid(column=0, row=1,
                         sticky='EW')

        self.entryF = tkinter.Entry(self)
        self.entryF.grid(column=2, row=1,
                         sticky='EW')
        #segunda parte
        self.entryA = tkinter.Entry(self)
        self.entryA.grid(column=0, row=5,
                         sticky='EW')

        self.entryB = tkinter.Entry(self)
        self.entryB.grid(column=2, row=5,
                         sticky='EW')

        #terceira parte
        self.entryZ = tkinter.Entry(self)
        self.entryZ.grid(column=0, row=8,
                         sticky='EW')

        self.entryX = tkinter.Entry(self)
        self.entryX.grid(column=2, row=8,
                         sticky='EW')

        #botao
        self.btnCalculaF = tkinter.Button(self, text=u" Inteiro -> Binario",
                                          command=self.OnButtonCalculaFClick)
        self.btnCalculaF.grid(column=0, row=3)


        self.btnCalculaC = tkinter.Button(self, text=u" Binario -> Inteiro",
                                          command=self.OnButtonCalculaCClick)
        self.btnCalculaC.grid(column=2, row=3)

        #SEGUNDA PARTE
        self.btnCalculaF1 = tkinter.Button(self, text=u" Inteiro -> Octal",
                                          command=self.OnButtonCalculaFC1lick)
        self.btnCalculaF1.grid(column=0, row=6)

        self.btnCalculaC1 = tkinter.Button(self, text=u" Octal -> Inteiro",
                                          command=self.OnButtonCalculaCC1lick)
        self.btnCalculaC1.grid(column=2, row=6)

        #terceira parte
        self.btnCalculaF2 = tkinter.Button(self, text=u" Inteiro -> Hexadecimal",
                                           command=self.OnButtonCalculaFC2lick)
        self.btnCalculaF2.grid(column=0, row=9)

        self.btnCalculaC2 = tkinter.Button(self, text=u" Hexadecimal -> Inteiro",
                                           command=self.OnButtonCalculaCC2lick)
        self.btnCalculaC2.grid(column=2, row=9)

        #entrada
    def OnButtonCalculaFClick(self):
        inteiro = int(self.entryC.get())
        binario = bin(inteiro)[2:]
        self.entryF.delete(0, tkinter.END)
        self.entryF.insert(0, str(binario))

    def OnButtonCalculaCClick(self):
        binario = (self.entryF.get())
        inteiro = int(binario, 2)
        self.entryC.delete(0, tkinter.END)
        self.entryC.insert(0, str(inteiro))

        #segunda parte
    def OnButtonCalculaFC1lick(self):
        inteiro = int(self.entryA.get())
        octal = oct(inteiro)[2:]
        self.entryB.delete(0, tkinter.END)
        self.entryB.insert(0, str(octal))

    def OnButtonCalculaCC1lick(self):
        octal = (self.entryB.get())
        inteiro = int(octal, 8)
        self.entryA.delete(0, tkinter.END)
        self.entryA.insert(0, str(inteiro))

        #terceira parte
    def OnButtonCalculaFC2lick(self):
        inteiro = int(self.entryZ.get())
        hexadecimal = hex(inteiro)[2:]
        self.entryX.delete(0, tkinter.END)
        self.entryX.insert(0, str(hexadecimal))

    def OnButtonCalculaCC2lick(self):
        hexadecimal = (self.entryX.get())
        inteiro = int(hexadecimal, 16)
        self.entryZ.delete(0, tkinter.END)
        self.entryZ.insert(0, str(inteiro))



if __name__ == "__main__":
    app = minhaApp_tk(None)
    app.title('Calculadora conversão positiva')
    app.mainloop()
