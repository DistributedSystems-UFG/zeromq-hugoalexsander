import zmq, time, pickle, random
from constPipe import VENT_PORT

NTASKS = 100

def producer():
  context = zmq.Context()
  socket = context.socket(zmq.PUSH)
  socket.bind("tcp://*:" + VENT_PORT)

  print("Producer à espera que os workers se liguem...")
  time.sleep(2)

  total = 0
  for task_id in range(NTASKS):
    workload = random.randint(1, 100)
    total += workload
    print("Producer envia tarefa " + format(task_id, '03d') + " (custo " + format(workload, '03d') + ")")
    socket.send(pickle.dumps((task_id, workload)))

  print("Producer: total de trabalho gerado = " + str(total))

if __name__ == "__main__":
  producer()
