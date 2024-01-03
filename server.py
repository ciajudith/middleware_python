import Pyro4


@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, " + name + ". Have a great day!"


# Exécution du serveur
daemon = Pyro4.Daemon()  # Crée un serveur Pyro
uri = daemon.register(GreetingMaker)  # Enregistre l'objet comme un Pyro objet

print("Ready. Object uri =", uri)  # Imprime l'URI de l'objet
daemon.requestLoop()  # Commence la boucle d'écoute pour les requêtes
