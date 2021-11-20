import random
import matplotlib.pyplot as plt
import numpy as np

class DataGenerator:
    def __init__(self, num_vals=10, range_start=0, range_end=1):
        self.num_vals = num_vals
        self.range_start = range_start
        self.range_end = range_end

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

valuesList = []
gen = DataGenerator(20, 0, 100)
valuesList = gen.data_in_range()
#print(valuesList)
