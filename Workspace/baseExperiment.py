from . import *
import pickle

class BaseExperiment:

    def __init__(self, core) -> None:
        '''Should use the Core instance to conduct experiments'''
        self.core = core
    
    def run(self):
        '''This method will run the experiment'''
        
    def plot(self):
        '''This method is called, when you need to visualize the results of your experiment'''

    @property
    def core(self):
        return self._core
    
    @core.setter
    def core(self, val):
        if type(val) != Core:
            raise ValueError('The input value must be Core')
        self._core = val