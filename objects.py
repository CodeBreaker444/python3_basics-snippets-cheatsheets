
#oop allows us to model real world objects......class is appearance and abilities are functions
class Computers:
    __system=""
    __processor=""
    __ram=0
    __storage=0
#constructor
    def __init__(self,system,processor,ram,storage):
        self.__system=system
        self.__processor=processor
        self.__ram=ram
        self.__storage=storage

    def insert_system(self,system):
        self.__system=system
#enscapulation
    def insert_processor(self,processor):
        self.__processor=processor

    def insert_ram(self,ram):
        self.__ram=ram

    def insert_storage(self,storage):
        self.__storage=storage

    def view_system(self):
        return self.__system

    def view_processor(self):
        return self.__processor

    def view_ram(self):
        return str(self.__ram)

    def view_storage(self):
        return str(self.__storage)

    def print(self):
        return "{} is name,{} is processor,{}GB is ram,{}TB is storage".format(self.__system,
                                                                           self.__processor,
                                                                           self.__ram,
                                                                           self.__storage)

codebreaker=Computers('Cracker','Intel i-7700K',16,2.5)
print(codebreaker.print())

class keyboard(Computers):
    __name=""
    def __init__(self,system,processor,ram,storage,name):
        self.__name=name
        super(keyboard,self).__init__(system,processor,ram,storage)

    def insert_name(self,name):
        self.__name=name

    def view_name(self):
        return self.__name

    def print(self):
        return "{} is name,{} is processor,{}GB is ram,{}TB is storage,{} is the Keyboard".format(
                                                                               self.__system,
                                                                               self.__processor,
                                                                               self.__ram,
                                                                               self.__storage,
                                                                               self.__name)

codebreakers=keyboard('Hacker','AMDRyzen7',16,2,'AZIO')
print(codebreakers.print())