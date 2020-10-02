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
    
    def __create(self):
        kategorier = ['Ettor', 'Tvåor',
                    'Treor', 'Fyror',
                    'Femmor', 'Sexor',
                    'Summa', 'Bonus',
                    'Par', 'Två par',
                    'Triss', 'Fyrtal',
                    'Liten stege',
                    'Stor stege',
                    'Kåk', 'Chans',
                    'Yatzy', 'Summa']
        spelare = ['Namn', 'Obama', 'Greta']
        self.cells = {}
        for idx,i in enumerate(kategorier):
            for jdx, j in enumerate(spelare):
                e = tk.Label(self, bg = '#3E4149', anchor = 'w', justify = 'left')
                if idx == 0 & jdx < len(spelare):
                    e['text'] = j
                    e.grid(row=0,column=jdx)
                elif jdx == 0:
                    e['text'] = i
                    e.grid(row=idx, column=0)
                else:
                    e['text'] = ''
                    e.grid(row=idx, column=jdx)
                self.cells[(idx,jdx)] = e
        
if __name__ == '__main__':
    # initierar tkinter till en root variabel
    root = tk.Tk()
    # lägger till den till en subklass
    app = App(root)
    # startar igång appen med metoden mainloop()
    app.mainloop()