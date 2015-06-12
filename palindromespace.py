from datastructure.deque.Deque import Deque

def checkPalindrome(value):
    deque = Deque()
    for val in value:
        deque.addRear(val)

    stillFalse = True

    while deque.size() > 1 and stillFalse:
        front = deque.removeFront()
        rear = deque.removeRear()

        while front == ' ':
            front = deque.removeFront()

        while rear == ' ':
            rear = deque.removeRear()

        print('Front = %s, Rear = %s' %(front, rear))

        if not front == rear:
            stillFalse = False
            print('This string is not a palindrome')

    return stillFalse




if __name__ == '__main__':
    value = 'I PREFER PI'
    print('Is Palindrome : %s' %checkPalindrome(value))

