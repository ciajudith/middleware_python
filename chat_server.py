# chat_server.py
import Pyro4


@Pyro4.expose
class ChatServer(object):
    def __init__(self):
        self.messages = []

    def post_message(self, message):
        self.messages.append(message)
        return True

    def get_messages(self):
        return self.messages


daemon = Pyro4.Daemon()
uri = daemon.register(ChatServer)
print(f"Prêt. Object uri = {uri}")
daemon.requestLoop()
