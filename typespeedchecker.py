from time import *
import random as r


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error =error+1
        except :
            error =error+1
    return  error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e-time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

while true:
    ck = input("reaady to test")
    if ck=="y":
        test =["sanjay kadel is my name","ok any i am starting .","last string at all","ok all out"]
        test1 = r.choice(test)
        print("typing speed calculator")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput=input("enter : ")
        time_2 =time()
        print('Speed: ',speed_time(time_1,time_2,testinput),"w/s")
        print("error" , mistake(test1,testinput))
    elif ck == 'no':
        print("thanks")
        break

    else:
        print("wrong input")