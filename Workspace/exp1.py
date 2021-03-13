from . import *
from matplotlib import pyplot as plt

class Experiment1(BaseExperiment):
    def __init__(self, core) -> None:
        super().__init__(core)

    def run(self):
        self.result = 10

    def plot(self):
        plt.scatter([1,2],[2,1])

if __name__ == '__main__':
    e = Experiment1(Core())
    e.plot()
    plt.show()