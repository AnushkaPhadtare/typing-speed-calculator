from time import *
import random as r


def mistake(par,usertest):
    error=0
    for i in range(len(par)):
        try:
            if par[i]!= usertest[i]:
                error+=1
        except:
            error+=1
    return error 

def speed_time(start,end,userinput):
    time_delay=end-start
    roundoff_time=round(time_delay,2)   
    speed=len(userinput)/roundoff_time
    return round(speed) 

               
if __name__=='__main__':   
    while True:
        response=input("Are you redy to take the typing test: yes/no: ")
        if response=="yes":
            test=['The old oak tree whispered secrets to the wind as the sun set behind the mountains','My name is Python','Welcome to Typing Speed Test']
            test1=r.choice(test)
            print("*****Typing Speed Calculator*****")
            print(test1)
            print()
            print()
            time1=time()
            test_input=input("Enter: `")
            time2=time()

            print('Speed: ',speed_time(time1,time2,test_input),'w/sec')
            print("Error: ",mistake(test1,test_input))
                
        elif response=="no":
                print("Thankyou for using the typing Test Calculator: ")
                break
        else:
                print("Invalid Input")
                
                    

