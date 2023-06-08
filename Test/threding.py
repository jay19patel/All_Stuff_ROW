import threading

def print_numbers():
    for i in range(1, 11):
        print("First Funtion",i)

def print_letters():
    for i in range(1, 11):
        print("second Funtion",i)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print('Done!')
