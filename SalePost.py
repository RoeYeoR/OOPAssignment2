from Post import Post



'''
This class displays post of type sale
'''



class SalePost(Post):
    def __init__(self,user,post_description,post_price,post_location):
        super(SalePost,self).__init__(user)
        self._avaliable=True
        print(f"{user.name} posted a product for sale:\nFor sale! {post_description}, price: {post_price}, pickup from: {post_location}\n")
        self._post_description=post_description
        self._post_price=post_price
        self._post_location=post_location
        
    def like(self, user_did_like):
        return super()._like(user_did_like)
    def comment(self,user_commented,text):
        return super()._comment(user_commented,text)

    def discount(self,discount_precentage,password):
        if(self._user.password==password):
            self._post_price= self._post_price*(1-(discount_precentage/100))
            print(f"Discount on {self._user.name} product! the new price is: {self._post_price}")
        else:
            print("Password wrong")
    
    def sold(self,password):
        if(self._user.password==password):
            self._avaliable=False
            print(f"{self._user.name}'s product is sold")
        else:
            print("Password wrong")
    def __str__(self):
        if(self._avaliable):
            return (f"{self._user.name} posted a product for sale:\nFor sale! {self._post_description}, price: {self._post_price}, pickup from: {self._post_location}\n")
        else:
            return (f"{self._user.name} posted a product for sale:\nSold! {self._post_description}, price: {self._post_price}, pickup from: {self._post_location}\n")

