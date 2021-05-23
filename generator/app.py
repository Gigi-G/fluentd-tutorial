import threading
import time
import random
from fluent import sender
from fluent import event

thread_name = {
    'one':      '{\"message\":\"Hello\",\"from\":\"thread.one\"}', 
    'two':      'Hello thread.two', 
    'three':      'Hello thread.three', 
    'four':    '{\"message\":\"Hello\",\"from\":\"thread.four\"}'
}

def generator(name):
    time.sleep(5)
    sender.setup("thread", host='fluentd', port=9888)
    while(True):
        event.Event(name, {
            'log': thread_name[name]
        })
        time.sleep(random.randint(1,5))

if __name__ == "__main__":
    print("Starting threads")
    for name in thread_name:
        threading.Thread(target=generator, args=(name, )).start()