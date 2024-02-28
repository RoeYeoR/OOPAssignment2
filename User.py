from PostFactory import PostFactory
from observer import *


'''

This class handles the actions and features of user of the SocialNetwork.

'''



class User(Sender,Reciever):

    def __init__ (self,name,password):
        Sender.__init__(self)
        Reciever.__init__(self)

        self._name=name
        self._password=password
        self._following=[]
        self._followers=[]
        self._posts=[]
        self._online=True



    def follow(self,user_to_follow):
        if(self._online):

            for user in self._following:
                if(user.name ==user_to_follow.name):
                    print("You already following this user")
                    return
            self._following.append(user_to_follow)
            user_to_follow.subscribe(self)
            user_to_follow.followers.append(self)
            print(f"{self.name} started following {user_to_follow.name}")

    def unfollow(self,user_to_unfollow):
        if(self._online):

            if user_to_unfollow in self._following:
                self._following.remove(user_to_unfollow)
                user_to_unfollow.unsubscribe(self)
                user_to_unfollow.followers.remove(self)
                print(f"{self.name} unfollowed {user_to_unfollow.name}")


            else:   
                print("You already unfollowing this user")
                
    def publish_post(self,post_type,*args):
        if(self._online):

            post_factory = PostFactory()
            post=post_factory.create_post(self,post_type,*args)
            self._posts.append(post)
            self.notify(f"{self.name} has a new post")

            return post
    def __str__(self):
        return (f"User name: {self.name}, Number of posts: {len(self._posts)}, Number of followers: {len(self._followers)}")
    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.notifications:
            print(notification)
    @property
    def name(self):
        return self._name
    @property
    def posts(self):
        return self._posts
    @property
    def following(self):
        return self._following
    @property
    def followers(self):
        return self._followers
    @property
    def password(self):
            return self._password
    @property
    def online(self):
            return self._online
    @property
    def notifications(self):
            return self._notifications