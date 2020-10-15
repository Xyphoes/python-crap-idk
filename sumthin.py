import time
print("E for even O for odd")
answer = str(input())

if answer == "E":
    for i in range(0,10):
        time.sleep(1)
        a = i+2
        print(a+i)

elif answer == "O":
    for i in range(0,10):
        time.sleep(1)
        a = i+1
        print(a+i)




