from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
This class displays post of type image
'''

class ImagePost(Post):
    
    def __init__(self,user,image_path):
        super(ImagePost,self).__init__(user)
        print(f"{user.name} posted a picture")
        print()

        self._image_path=image_path
    def like(self, user_did_like):
        return super()._like(user_did_like)
    def comment(self,user_commented,text):
        return super()._comment(user_commented,text)
    def display(self):
        img = mpimg.imread(self._image_path)  # Load the image
        plt.imshow(img)  # Display the image
        plt.axis('off')  # Hide axis
        plt.show()  # Show the plot return super().comment(user_commented,text)
        print("Shows picture")
    def __str__(self):
        return f"{self._user.name} posted a picture\n"




