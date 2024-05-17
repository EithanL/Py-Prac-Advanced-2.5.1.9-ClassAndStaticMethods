# Scenario
# Create a class representing a luxury watch;
# The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
# the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
# the regular __init__ method should only increase the value of the appropriate class variable;
# The text intended to be engraved should follow some restrictions:

# it should not be longer than 40 characters;
# it should consist of alphanumerical characters, so no space characters are allowed;
# if the text does not comply with restrictions, an exception should be raised;
# before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

# Create a watch with no engraving
# Create a watch with correct text for engraving
# Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
# After each watch is created, call class method to see if the counter variable was increased

##########################################################################################################################################

class luxuryWatch:
    __ctr = 0
    def __init__(self):
        luxuryWatch.__ctr+=1
        self.engrave=""
        
    
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__ctr
    
    @staticmethod
    def verifEngrave(engrave):
        if len(engrave)<=40 and engrave.replace(" ","").isalpha():
            return True
        else:
            raise ValueError
        
    
    @classmethod    
    def engravedWatch(cls,engrave):
        if cls.verifEngrave(engrave):
            insClass = cls()
            insClass.engrave = engrave
        

cl1 = luxuryWatch()
cl2 = luxuryWatch.engravedWatch("For you")
try:
    cl3 = luxuryWatch.engravedWatch("foo@baz.com")
except:
    pass
print(luxuryWatch.get_number_of_watches_created())