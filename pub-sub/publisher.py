import zmq, time, random
from const import PORT

def publisher():
  context = zmq.Context()
  socket = context.socket(zmq.PUB)
  socket.bind("tcp://*:" + PORT)
  print("Publisher a emitir na porta " + PORT + "...")

  while True:
    time.sleep(3)
    t = "TIME " + time.asctime()
    socket.send(t.encode())

    temp = "TEMP " + str(round(random.uniform(15.0, 35.0), 1))
    socket.send(temp.encode())

    print("Publicado -> " + t + " | " + temp)

if __name__ == "__main__":
  publisher()
