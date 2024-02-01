from tkinter import *
from tkinter import ttk
#from logic import genetic_algorithm

class DataObject:
    def __init__(self, eta, tolerancy, epoch ):
        self.eta = eta
        self.tolerancy = tolerancy
        self.epoch = epoch

root = Tk()
root.title("How to train your perceptron")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
for i in range(4):
    root.rowconfigure(i, weight=1)
    for j in range(3):
        mainframe.columnconfigure(j, weight=1) 


def save_data():
    eta_value = eta.get()
    tolerancy_value = tolerancy.get()
    epoch_value = epoch.get()
    data = DataObject(eta_value, tolerancy_value, epoch_value)
    #genetic_algorithm(data)        

eta = StringVar()
ttk.Label(mainframe, text="Tasa de aprendizaje:").grid(column=1, row=1, sticky=W)
eta.set("0.00000001")
ttk.Entry(mainframe, textvariable=eta).grid(column=2, row=1, sticky=W)


tolerancy = StringVar()
ttk.Label(mainframe, text="Tolerancia:").grid(column=1, row=2, sticky=W)
ttk.Entry(mainframe, textvariable=tolerancy).grid(column=2, row=2, sticky=W)


epoch = StringVar()
ttk.Label(mainframe, text="Número de épocas:").grid(column=1, row=3, sticky=W)
ttk.Entry(mainframe, textvariable=epoch).grid(column=2, row=3, sticky=W)


ttk.Button(mainframe, text="Entrenar", command=save_data).grid(column=3, row=4, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=15, pady=5)

root.update()

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()