#this are special methods which are prefix and suffix with "__" like "__add__" .
#you don't need to call this methods they called implicitly
class Auther:
    def __init__(self,name,book_name,pages):
        self.name =name
        self.book = book_name
        self.page = pages
    def __str__(self):#it is a dunder method which will return the string value of the constuctor only using the object name
        return f"{self.book} is written by {self.name}"
    def __len__(self):# return the pages of book
        return self.page
    def __call__(self, *args, **kwargs):
        print("Hi")
    def __del__(self):
        print("Auther object is being deleted")
d= Auther("Mohit","Java",234)
print(d)
print(len(d))
d()
del d