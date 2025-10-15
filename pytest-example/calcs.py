from abc import ABC, abstractmethod

# implement an abstract class example
class Metric(ABC): 
    
    @abstractmethod
    def addition(self, a, b) -> int:
        pass

class Euclidean(Metric): 
    
    # should we do an abstractmethod here? 
    def addition(self, a, b): 
        return a + b
    



