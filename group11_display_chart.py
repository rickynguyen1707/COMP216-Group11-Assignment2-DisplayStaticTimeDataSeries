import random
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tkk

class DataGenerator(tkk.Tk):
    def __init__(self, num_vals=10, range_start=0, range_end=1):
        super().__init__()
        self.num_vals = num_vals
        self.range_start = range_start
        self.range_end = range_end
        self.historical_data = self.data_in_range()
        self.initUI()

    def __gen_points(self):
        def growth(series):
            m = (random.random() - 0.5) * 2
            return series * m

        def oscillation(i):
            delta = random.random() - 0.5
            coeff = random.randint(1,10)
            return i + (coeff * delta)

        series = growth(np.array(range(self.num_vals)))
        series = np.array([oscillation(i) for i in series])
        # scale it down to the mean of 0.5 and std of 1:
        return ((series - series.mean()) / (series.max() - series.min())) + 0.5

    def data_in_range(self):
        return (self.range_end - self.range_start) * self.__gen_points() + self.range_start

    def plot(self, points):
        plt.plot(points, color='g')
        plt.xlabel("Days driven")
        plt.ylabel("Gasoline (Liters)")
        plt.title("Fuel Indicator")
        plt.show()

    def initUI(self):
        #Window properties
        self.geometry("600x500")
        self.title("Historical Data")
        self["bg"]="white"
        #Grid
        self.columnconfigure(0,weight=3)
        self.columnconfigure(1,weight=3)
        self.columnconfigure(2,weight=3)
        self.columnconfigure(3,weight=3)
        #Variables
        self.Data_range=tkk.IntVar()
        #Canvas
        self.my_canvas=tkk.Canvas(width=400,height=300,bg="white")
        self.my_canvas.grid(column=1,row=3,pady=75)
        #Commands
        def Go():
            self.my_canvas.delete()
            self.data_range_label.destroy()
            self.data_range_label=tkk.Label(self,text=f"Data range: {self.Data_range.get()}-{self.Data_range.get()+5}",font=("Ariel",15),width=30,bg="white")
            self.data_range_label.grid(column=0,row=1)
            DrawRects(self.Data_range.get())
        def DrawRects(data_range):
            data_range=self.Data_range.get()#no use right now
            x_coord=0
            old_x_coord=0
            old_y2=0
            rect_thickness=40
            rect_spacing=5
            line_spacing=8#Don't ask why
            self.my_canvas=tkk.Canvas(width=400,height=300,bg="white")
            self.my_canvas.grid(column=1,row=3,pady=75)
            index = self.Data_range.get()
            height = 300
            range = self.historical_data[index:index + 5]
            #rescale the range to fit within the box nicely
            range = range * (0.8 * height) / max(range)
            for x, y in enumerate(range):
                x1=x_coord
                x2=x_coord+rect_thickness
                y1=height
                y2=y1-y
                self.my_canvas.create_rectangle(x1,y1,x2,y2,fill="lightgreen")
                if(x!=0):
                    self.my_canvas.create_line(old_x_coord+line_spacing,old_y2,x2-((rect_spacing+rect_thickness)/2),y2,fill="red",width=2)
                x_coord+=rect_thickness+rect_spacing
                old_x_coord=x_coord-rect_thickness+rect_spacing
                old_y2=y2
        #Labels
        self.data_range_entrylabel=tkk.Label(self,text="Data range",font=("Ariel",15),width=15,bg="white")
        self.data_range_label=tkk.Label(self,text=f"Data range: {self.Data_range.get()}-{self.Data_range.get()+5}",font=("Ariel",15),width=30,bg="white")
        self.data_range_entrylabel.grid(column=0,row=0,padx=25)
        self.data_range_label.grid(column=0,row=1)
        #Entry
        self.data_range_entry=tkk.Entry(self,textvariable=self.Data_range)
        self.data_range_entry.grid(column=1,row=0,padx=50)
        #Button
        self.data_range_button=tkk.Button(self,text="Go",width=20,command=Go)#No you dont put () after the Go method
        self.data_range_button.grid(column=2,row=0)

if __name__ == "__main__":
    valuesList = []
    gen = DataGenerator(20, 0, 100)
    gen.mainloop()
    valuesList = gen.data_in_range()
    #print(valuesList)  
