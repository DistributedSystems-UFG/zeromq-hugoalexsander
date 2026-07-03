import zmq, pickle, sys, time
from constPipe import VENT_IP, VENT_PORT, SINK_IP, SINK_PORT

def worker(wid):
  context = zmq.Context()
  receiver = context.socket(zmq.PULL)
  receiver.connect("tcp://" + VENT_IP + ":" + VENT_PORT)

  sender = context.socket(zmq.PUSH)
  sender.connect("tcp://" + SINK_IP + ":" + SINK_PORT)

  print("Worker " + wid + " pronto")
  while True:
    task_id, workload = pickle.loads(receiver.recv())
    print("Worker " + wid + " recebeu tarefa " + format(task_id, '03d'))
    time.sleep(workload * 0.01)
    result = workload * 2
    sender.send(pickle.dumps((wid, task_id, result)))

if __name__ == "__main__":
  wid = sys.argv[1] if len(sys.argv) > 1 else "1"
  worker(wid)
