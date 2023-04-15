import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
signs = "_-=$%@#/?.:"

class getPassword:
    def __init__(self, length = 15, element = [lower, upper, digits, signs]):
        self.element = element
        self.length = length
        
    def convertListToStr(self):
        self.convertedStr = ""
        for element in self.element:
            self.convertedStr += element
        return self.convertedStr
            
    def generateRandomPassword(self):
        self.convertListToStr()
        self.password = ''.join(random.choice(self.convertedStr) for _ in range(self.length))
        return self.password
