import random
import time

class QueueError(IndexError):
    """Custom exception for queue operations."""
    pass

class Queue:
    def __init__(self):
        self._queue = []

    def put(self, item):
        self._queue.append(item)

    def get(self):
        if self.isempty():
            raise QueueError("Queue is empty!")
        return self._queue.pop(0)

    def isempty(self):
        return len(self._queue) == 0

    def __iter__(self):
        return iter(self._queue)

    def __len__(self):
        return len(self._queue)

class Train:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def __str__(self):
        return f"Train {self.name} to {self.destination}"

class SuperQueue(Queue):
    """A queue with additional utility methods."""
    def peek(self):
        if self.isempty():
            raise QueueError("Queue is empty!")
        return self._queue[0]

def train_arrival_generator(train_list):
    """Generator yielding arriving trains."""
    for train in train_list:
        yield train
        time.sleep(0.2)  # Simulate time between arrivals (can be removed for faster CLI)

def main():
    destinations = ["Edinburgh", "Glasgow", "Aberdeen", "Inverness", "Perth", "Dundee", "Bo'ness"]
    train_names = ["Caledonian", "Flying Scotsman", "Jacobite", "Tartan Trail", "Nessie Express", "Highland Coo"]
    queue = SuperQueue()

    # Simulate random arrivals
    train_list = [Train(random.choice(train_names), random.choice(destinations)) for _ in range(5)]
    arrivals = train_arrival_generator(train_list)

    print("\n--- Scottish Train Queue Simulator ---")
    while True:
        print("\nMenu:")
        print("1. Next train arrives")
        print("2. Dispatch (depart) next train")
        print("3. Peek at next train")
        print("4. View queue")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                train = next(arrivals)
                queue.put(train)
                print(f"Arrival: {train}")
            except StopIteration:
                print("No more arriving trains scheduled.")
        elif choice == "2":
            try:
                departed = queue.get()
                print(f"Dispatched: {departed}")
            except QueueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                print(f"Next train: {queue.peek()}")
            except QueueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            if queue.isempty():
                print("Queue is empty.")
            else:
                print("Trains in queue:")
                for t in queue:
                    print(f"  {t}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
