import zmq, time
from const import PORT

def server():
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:" + PORT)
  print("Server à espera de pedidos na porta " + PORT + "...")

  while True:
    message = socket.recv().decode()
    if message == "STOP":
      socket.send(b"BYE")
      break
    elif message == "TIME":
      reply = time.asctime()
    elif message.startswith("UPPER:"):
      reply = message[len("UPPER:"):].upper()
    elif message.startswith("ECHO:"):
      reply = message[len("ECHO:"):] + "*"
    else:
      reply = "ERRO: comando desconhecido"
    print("Pedido: " + message + " -> Resposta: " + reply)
    socket.send(reply.encode())

if __name__ == "__main__":
  server()
