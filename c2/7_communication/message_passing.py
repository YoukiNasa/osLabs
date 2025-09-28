import multiprocessing
import time

class MessagePassingSystem:
    def __init__(self):
        self.queue = multiprocessing.Queue()
        
    def send(self, message):
        print(f"[SEND] Send: {message}")
        self.queue.put(message)
        
    def receive(self, timeout=None):
        try:
            message = self.queue.get(timeout=timeout)
            print(f"[RECV] Received: {message}")
            return message
        except:
            print("[RECV] Wait timeout, no message")
            return None

def producer(mps):
    for i in range(5):
        mps.send(f"Message #{i}")
        time.sleep(0.5)
    mps.send("End")

def consumer(mps):
    while True:
        msg = mps.receive(timeout=1)
        if msg == "End":
            print("Consumer received end signal")
            break
        # Process message
        time.sleep(1)

if __name__ == "__main__":
    mps = MessagePassingSystem()

    p_producer = multiprocessing.Process(target=producer, args=(mps,))
    p_consumer = multiprocessing.Process(target=consumer, args=(mps,))
    
    p_producer.start()
    p_consumer.start()
    
    p_producer.join()
    p_consumer.join()
    
    print("Finished.")