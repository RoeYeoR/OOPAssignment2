from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


"""
This class represents Factory design pattern which 
hides the implementations of each type of post who extends from Post class.
"""


class PostFactory():

    def create_post(self,user, post_type, *args):
        if post_type == "Text":
            return TextPost(user,*args)
        elif post_type == "Image":
            return ImagePost(user,*args)
        elif post_type == "Sale":
            return SalePost(user,*args)
        else:
            raise ValueError("Invalid post type")
