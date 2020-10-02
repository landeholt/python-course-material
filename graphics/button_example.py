import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        """ superklassen är Frame.
            Den tar emot title, height, width, bg,
            fg, med mera.
        """
        super().__init__(master, height=150, width=150, bg='#3E4149')
        self.master = master
        """ gör att fönsteret inte minimeras till minsta form, 
            prova skillnaden genom att kommentera ut underliggande rad
        """
        self.pack_propagate(False)
        # metoden pack() placerar widgetten på framen.
        self.pack()
        self.__create()
    
    # create skapar upp en label-widget och två knappar.
    def __create(self):
        label = tk.Label(self,text='Hello!', bg = '#3E4149', fg = 'white')
        label.pack(side='top')
        """ Alla knappar har en parameter som heter command.
            När man klickar på knappen, så är det funktionen
            kopplad till command körs. Det knepiga är att
            det behöver göras genom en lambda funktion, annars
            aktiveras den vid körtiden (alltså när programmet startas)
        """
        obamaButton = tk.Button(self, text="I am Obama", highlightbackground='#3E4149', command=lambda:self.__changeText(label,f'Hello Obama!'))
        gretaButton = tk.Button(self, text='I am Greta', highlightbackground='#3E4149', command=lambda:self.__changeText(label,f'Hello Greta!'))
        
        obamaButton.pack(fill='both')
        gretaButton.pack(fill='both')

    def __changeText(self, w, newText):
        w['text'] = newText

if __name__ == '__main__':
    # initierar tkinter till en root variabel
    root = tk.Tk()
    # lägger till den till en subklass
    app = App(root)
    # startar igång appen med metoden mainloop()
    app.mainloop()
    

