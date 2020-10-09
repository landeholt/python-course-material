import tkinter as tk

class Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg = "#FFFFFF")
        self.FONTSTYLE = ("Arial", 16)

class AllGroups(Page):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.name = "AllGroups"

        label = tk.Label(self, text= "Not great, not terrible")
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        buttonE = tk.Button(self, text="visa grupp E", fg = "#000000", highlightbackground= "#303030", command = lambda : controller.goTo('GruppE'))
        buttonJ = tk.Button(self, text="visa grupp J", fg = "#000000", highlightbackground = "#303030", command = lambda : controller.goTo('GruppJ'))

        buttonE.grid(row = 1, column = 1, padx = 10, pady = 10)
        buttonJ.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
class GruppE(Page):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.name = "GruppE"

        names = ['Max Aronsson',
        'Annie Dang',
        'Filip Engdahl'
        'Theodor Eriksson',
        'Nils Grenmark',
        'Nora Gullberg',
        'Theodor Hagström',
        'Philip Hörnfeldt',
        'Joel Lindgren',
        'Oliver Midbrink',
        'Isak Nordgren',
        'Erik Råberg',
        'Simon Sandberg',
        'Hampus Svensson',
        'Marcus Wahlman',
        'Melker Widlund']

        for idx, n in enumerate(names):
            label = tk.Label(self, text = n)
            label.grid(row = idx)
        
        button = tk.Button(self, text="Gå tillbaka", fg = "#000000", highlightbackground = "#303030", command = lambda : controller.goTo('AllGroups'))
        button.grid(row = idx+1)

class GruppJ(Page):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.name = "GruppJ"

        names = ['John hann inte såhär långt']

        for idx, n in enumerate(names):
            label = tk.Label(self, text = n)
            label.grid(row = idx)
        
        button = tk.Button(self, text="Gå tillbaka", fg = "#000000", highlightbackground = "#303030", command = lambda : controller.goTo('AllGroups'))
        button.grid(row = idx+1)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        # Skapa en huvudcontainer som ska hålla alla andra framesen
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 

        self.frames = {}

        for F in [AllGroups, GruppE, GruppJ]:
            frame = F(container, self)

            self.frames[frame.name] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.goTo("AllGroups")

    def goTo(self, frame):
        self.frames[frame].tkraise()

if __name__ == '__main__':
    # lägger till den till en subklass
    app = App()
    # startar igång appen med metoden mainloop()
    app.mainloop()