from Post import Post



'''
This class displays post of type text
'''

class TextPost(Post):
    
    def __init__(self,user,post_text):
        
        print(f'{user.name} published a post:\n"{post_text}"')

        print()
        super(TextPost,self).__init__(user)
        self._post_text=post_text  
    def like(self, user_did_like):
        return super()._like(user_did_like)
    def comment(self,user_commented,text):
        return super()._comment(user_commented,text)
    def __str__(self):
        return (f'{self._user.name} published a post:\n"{self._post_text}"\n')
