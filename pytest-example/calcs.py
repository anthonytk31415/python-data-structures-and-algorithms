from abc import ABC, abstractmethod


class Metric(ABC): 
    
    @abstractmethod
    def addition(self, a, b) -> int:
        pass

class Euclidean(Metric): 
    
    def addition(self, a, b): 
        return a + b
    
