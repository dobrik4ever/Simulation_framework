from . import *

class BaseExperiment:

    def __init__(self, **cores) -> None:
        '''Should use the Core instance to conduct experiments'''
        for key, value in cores.items():
            setattr(self, key, value)
    
    def run(self):
        '''This method will run the experiment, using the Core attributes as the processed data'''
        
    def plot(self):
        '''This method is called, when you need to visualize the results of your experiment'''

    def __setattr__(self, name: str, value):
        if 'core' in name.lower() and type(value) != Core:
            raise ValueError('The input value must be Core')   
        super().__setattr__(name, value)

# ===== Example ===== #

# if __name__ == '__main__':
#     exp = BaseExperiment(core1 = Core(), core2 = Core())
#     exp.run()
#     exp.plot()