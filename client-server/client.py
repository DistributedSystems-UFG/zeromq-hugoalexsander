import zmq, sys
from const import SERVER_IP, PORT

def client(cid):
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://" + SERVER_IP + ":" + PORT)

  requests = ["TIME", "ECHO:Hello world", "UPPER:zeromq e sistemas distribuidos", "STOP"]
  for req in requests:
    print("Cliente " + cid + " envia:  " + req)
    socket.send(req.encode())
    reply = socket.recv().decode()
    print("Cliente " + cid + " recebe: " + reply)

if __name__ == "__main__":
  cid = sys.argv[1] if len(sys.argv) > 1 else "1"
  client(cid)
