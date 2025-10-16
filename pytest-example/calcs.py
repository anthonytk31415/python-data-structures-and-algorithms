from abc import ABC, abstractmethod

# implement an abstract class example
# use this for OOP
class Metric(ABC): 
    
    @abstractmethod
    def addition(self, a, b) -> int:
        pass

class Euclidean(Metric): 
    
    # should we do an abstractmethod here? 
    def addition(self, a, b): 
        return a + b
    



