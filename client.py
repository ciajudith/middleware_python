import Pyro4

uri = input("Enter the URI of the greeting object: ")
greeting_maker = Pyro4.Proxy(uri)

name = input("What is your name? ")
print(greeting_maker.get_fortune(name))
