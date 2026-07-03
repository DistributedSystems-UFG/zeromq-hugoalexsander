import zmq, sys
from const import PUB_IP, PORT

def subscriber(topic, n):
  context = zmq.Context()
  socket = context.socket(zmq.SUB)
  socket.connect("tcp://" + PUB_IP + ":" + PORT)
  socket.setsockopt(zmq.SUBSCRIBE, topic.encode())

  print("A subscrever o topico '" + topic + "'")
  for i in range(n):
    msg = socket.recv()
    print(msg.decode())

if __name__ == "__main__":
  topic = sys.argv[1] if len(sys.argv) > 1 else "TIME"
  n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
  subscriber(topic, n)
