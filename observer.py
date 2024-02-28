from abc import ABC,abstractmethod

"""
This class represents Observer design pattern where we have sender(to notify about some action)
and receiver (to get the updated notifications)
"""


class Sender(ABC):
    
    def __init__(self):
        self._subscribers =[]

    def subscribe(self,subscriber):
        self._subscribers.append(subscriber)    
    
    def unsubscribe(self,subscriber):
        self._subscribers.remove(subscriber)
    
    def notify(self,message):
        for subscriber in self._subscribers:
                subscriber.update(message)
class Reciever(ABC):

    def __init__(self):
        self._notifications=[]
    
    def update(self,message):
        self._notifications.append(message)
