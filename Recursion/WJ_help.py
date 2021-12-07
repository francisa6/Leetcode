class MyClass:
    # def __init__(self, *args):
    #     self.asdf = 234
    #     self.asdfasdf = 234

    def blah(asdfadsfasd, asdfads):
        # self can actually be anything e.g. here we defined it as asdfadsfasd 
        asdfadsfasd.field = asdfads

def my_blah(asdfadsfasd, asdfads):
    asdfadsfasd.field = asdfads
    print(asdfadsfasd.field)

# We can use __init__ to define it neatly or we can also just define it inside 
# the function eg. blah we have defined the field variable
# x = MyClass(234, 2343)

x = MyClass() # x is equal to asdfadsfasd
x.blah(23432)
# this is equivalent to...
MyClass.blah(x, 23432)
x.field

# Can then add extra functions into MyClass which then shows up in x
MyClass.foo = my_blah
x.foo(23432)
MyClass.foo(x, 23432)

# Cute function
my_blah(x, 23432)


class OtherObj:
    """
    __str__ and __repr__ are used to give you different views of the result e.g. str is usually 
    gives you the shorter/simpler view of the data whereas repr gives you more context/info. 


    """
    def __str__(self) -> str:
        # if you call x = OtherObj(); str(x) you get the same result as 
        return "hello"
    def __repr__(self) -> str:
        # if you call x = OtherObj(); repr(x) you get the same result as 
        return "goodbye"
    def __getattribute__(self, name: str):
        if name.startswith("anny"):
            return "hello " + name
        print("no")
    def __setattr__(self, name, value) -> None:
        # Can use this if you have a frozen Class and you want to restrict 
        # whether people can add extra variables into the class or not. If
        # field is not specified the class inherits from Object.__setattr__ 
        # (the parent class) and that allows for setting for fields. Note 
        # that methods can be set and are not frozen. Here we have restricted 
        # that only when name == "anny" can be set OtherObj().name = value otherwise
        # you get an error message.
        if name == "anny":
            print(f"it's ok anny, you can set it to {value}")
            super().__setattr__(name, value)
        else:
            print(f"haha you tried to set {name} to {value}. you fail")

x = OtherObj()
x.__repr__
x.__str__
x.asdfsf
x.anny1234 = 1234
x.anny = 1234
# We set x.anny to 1234 but when we print it out we get the __getattribute__ stuff
x.anny
# To get the 1234 we use __get__attribute command:
object.__getattribute__(x, "anny")



from dataclasses import dataclass

@dataclass(frozen=True)
class MyData:
    x:int
    y:str

old_to_str = MyData.__repr__

def new_to_str(obj):
    return old_to_str(obj) + f" AND ALSO blah={obj.blah}"

MyData.__str__ = new_to_str
MyData.__repr__ = new_to_str

z = MyData(12341234, "asdfasdf")
