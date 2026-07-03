import zmq, pickle, time
from constPipe import SINK_PORT

def sink():
  context = zmq.Context()
  receiver = context.socket(zmq.PULL)
  receiver.bind("tcp://*:" + SINK_PORT)

  print("Sink à espera de resultados...")
  total = 0
  count = 0
  start = None
  while True:
    wid, task_id, result = pickle.loads(receiver.recv())
    if start is None:
      start = time.time()
    total += result
    count += 1
    print("Sink recebeu resultado da tarefa " + format(task_id, '03d') + " do worker " + wid + " = " + str(result))
    if count % 10 == 0:
      elapsed = time.time() - start
      print("--- Resumo: " + str(count) + " tarefas, soma=" + str(total) + ", tempo=" + format(elapsed, '.2f') + "s ---")

if __name__ == "__main__":
  sink()
