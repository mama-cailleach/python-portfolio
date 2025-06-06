class QueueError(IndexError):  # Choose base class for the new exception.
        pass

#
#  Write code here
#


class Queue:
    def __init__(self):
        self.__list = []
        self.__bool = False



    def put(self, elem):
        self.__list.append(elem)



    def get(self):
        if len(self.__list) > 0:
            elem = self.__list[-1]
            del self.__list[-1]
            return elem


    def isempty(self):
        return len(self.__list) == 0


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)




que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
