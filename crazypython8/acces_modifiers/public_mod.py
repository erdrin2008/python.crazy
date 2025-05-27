class Myclass:

    def __init__(self):
        self._public_variable = "this is a public variable"

    def _public_method(self):
        print("this is a public method")


my_class = Myclass()

print(my_class._public_variable)
my_class._public_method()