# property decorator : It is used to "access ,modify"the private data members
class pwskills:
    def __init__(self,c_price,c_name):
        self.__c_price = c_price #private attribute
        self.c_name = c_name

    @property # decorator to access the private attribute
    def c_price_access(self):
        return self.__c_price

    @c_price_access.setter #decorator to set the value of private attribute
    def c_price_set(self,c_price):
        if c_price <=3434:
            pass
        else:
            self.__c_price = c_price

    @c_price_access.deleter # decorator to delete the attribute
    def delete_c_price(self):
        del self.__c_price

pw = pwskills(3423,"data science master")
print(pw.c_price_access)
print(pw.c_price_set)


