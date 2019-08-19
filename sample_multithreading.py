from actionator import addAction, getStats
import threading
import json


def thread_task():
    for i in range(1, 100):
        addAction(json.dumps({"action": "jump", "time": i}))


thread1 = threading.Thread(target=thread_task)
thread2 = threading.Thread(target=thread_task)

# Kickoff threads
thread1.start()
thread2.start()

# Wait until all threads are done
thread1.join()
thread2.join()

result = getStats()
assert result == '[{"action": "jump", "avg": 50.0}]'

print(f"Expect the average time for the action jump to be 50\n{result}")
