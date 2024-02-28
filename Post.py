from abc import ABC, abstractmethod

"""
This is an abstract class which defines functions of like and comment
"""


class Post(ABC):
    
    def __init__(self,user):
        self._likes=[]
        self._comments={}
        self._user=user


    def _like(self,user_did_like):
        if(self._user.online):
            for user in self._likes:
                if(user.name ==user_did_like.name):
                    print("This user aleady liked that post")

                    return
            if(self._user.name!=user_did_like.name):
                self._likes.append(user_did_like)
                print(f"notification to {self._user.name}: {user_did_like.name} liked your post")
                self._user.update(f"{user_did_like.name} liked your post")
    def _comment(self,user_commented,text):
        if(self._user.online):

            if user_commented.name not in self._comments:
                    self._comments[user_commented.name] = [text]
                    self._user.update(f"{user_commented.name} commented on your post")
                    print(f"notification to {self._user.name}: {user_commented.name} commented on your post: {text}")

            else:
                    self._comments[user_commented.name].append(text)
                    print(f"notification to {self._user.name}: {user_commented.name} commented on your post: {text}")

                    self._user.update(f"{user_commented.name} commented on your post")


