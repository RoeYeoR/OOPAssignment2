
from User import *

'''
This class manages the validity of users, 
we want to keep only one instance of this so we will 
use the Singleton design pattern for that.
'''


class SocialNetwork(object):
    _instance = None
    _name = None

    # Sigleton pattern
    # here we check if have already created an instance of this SocialNetwork object.
    #if none, create a new instance.
    #otherwise, return the exsiting instance.
    def __new__ (cls,name):
        if(cls._name==None):
            cls._name=name
        cls._users=[]
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls,).__new__(cls)
            print(f'The social network {cls._name} was created!')

        return cls._instance
        


    def sign_up(self,name,passord):

        for user in self._users:
            if(user.name ==name):
                print("user name already sign up")
                return
        if(len(passord)<4|len(passord)>8):
            print("password <4 or >8")
            return
        self._users.append(User(name,passord))
        return self._users[-1]
    def log_in(self,name,passord):

        for user in self._users:
            if(user.name ==name):
                if(user.password ==passord):
                    user._online=True
                    print(f"{user.name} connected")

    def log_out(self,name):

        for user in self._users: 
            if(user.name ==name):
                user._online=False
                print(f"{user.name} disconnected")

    def __str__(self):
        text=f"{self._name} social network:"
        for user in self._users:
            text+=f"\n{user}"
        text+="\n"
        return text




