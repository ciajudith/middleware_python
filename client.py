import Pyro4

uri = input("Enter the URI of the greeting object: ")  # L'URI du serveur
greeting_maker = Pyro4.Proxy(uri)                      # Utilise un proxy Pyro pour accéder à l'objet

name = input("What is your name? ")
print(greeting_maker.get_fortune(name))                # Appelle la méthode de l'objet serveur
