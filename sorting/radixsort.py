from datastructure.queue.Queue import Queue
import math

def radixsort(queue):
    size = 11
    length = paddingzero(queue)
    queueArr = []
    for i in range(size):
        queueArr.append(Queue())
    queueArr[0] = queue
    for i in range(length):
        while not queueArr[0].isEmpty():
            value = queueArr[0].dequeue()
            index = findindex(int(value), i+1)
            queueArr[index+1].enqueue(value)
        for jqueue in queueArr[1:]:
            while not jqueue.isEmpty():
                val = jqueue.dequeue()
                queueArr[0].enqueue(val)
    print 'Sorted Items: '
    while not queueArr[0].isEmpty():
        print int(queueArr[0].dequeue())

def findindex(value, pos):
    for i in range(pos):
        reminder = value % 10
        value = value / 10
    return reminder

def reverse(str):
    return reduce(lambda x, y: y + x, str)

def paddingzero(queue):
    list = []
    while not queue.isEmpty():
        list.append(queue.dequeue())
    length = findpaddinglength(list)
    if queue.isEmpty():
        for item in list:
            queue.enqueue(str(item).zfill(length))
    return length

def findpaddinglength(list):
    bigNumber = findBiggestNumber(list)
    length = int(math.log10(bigNumber)) + 1
    return length

def findBiggestNumber(list):
    maxValue = list[0]
    for item in list[1:]:
        if(maxValue < item):
            maxValue = item
    return maxValue;


queue = Queue()
queue.enqueue(170)
queue.enqueue(45)
queue.enqueue(75)
queue.enqueue(90)
queue.enqueue(802)
queue.enqueue(2)
queue.enqueue(24)
queue.enqueue(66)
radixsort(queue
#print(reverse('004'))
