import random
import operator
again='no'

print("                             WELCOME TO THE MATHEMATICAL HUB\n \n")

while (again=='no' or again=='NO'):
    print("what you want to perform \n     1-Test your basic knowledge \n     2-Want to perform conversion \n  ")
    a=int(input("enter your choice :- "))
    if a==1:
        print("     1-TEST YOUR BASIC MATHEMATICAL KNOWLEDGE \n")
        def random_answer():
            num1=random.randint(1,10)
            num2=random.randint(1,10)
            operators={ '+':operator.add,
                        '-':operator.sub,
                        '*':operator.mul,
                        '/':operator.truediv }
            op=random.choice(list(operators.keys()))
            ans=operators.get(op)(num1,num2)
            print(f"What is {num1} {op} {num2} ?")
            return ans
            
        def check_answer():
            ans=random_answer()
            guess=float(input())
            return guess==ans 
        
        def final():
            print("how well u know maths ?")
            score=0
            for i in range(5):
                if check_answer()==True:
                    print("correct!!!!")
                    score+=1
                else:
                    print("wrong")
            
                print(f"your score is : {score}")
        final()
    elif a==2:
        print("     2-Want to perform conversioin  \n")
        print(" \n \n   PERFORM CONVERSIONS")
        print("\n you want to do converion of \n a)-Length \n b)-Volume \n c)-Mass \n d)-temperature \n e)- energy")
        choice=input(" \n What you want to perform enter your choice :- \t")
        val=float(input("enter the value :- "))
        if choice=='a':
            d=int(input("\n 1- km to m \n 2- km to cm \n 3- km to mm  \n 4- km to inch \n 5- m to km\n 6- m to cm\n 7- m to mm \n 8- m to inch\n 9- cm to km \n 10- cm to m \n 11- cm to mm \n 12- cm to inch \n 13- mm to km \n 14- mm to m \n 15- mm to cm \n 16- mm to inch \n 17- inch to km \n 18- inch to m \n 19- inch to cm \n 20- inch to mm \n"))
            if d==1:
                f=val*1000
            elif d==2:
                f=val*100000
            elif d==3:
                f=val*1000000
            elif d==4:
                f=(val*2.54)//100000
            elif d==5:
                f=val/1000
            elif d==6:
                f=val*100
            elif d==7:
                f=val*1000
            elif d==8:
                f=(val*100)//2.54
            elif d==9: 
                f=val//100000
            elif d==10:
                f=val//100
            elif d==11:
                f=val*10
            elif d==12:
                f=val//2.54    
            elif d==13:
                f=val/1000000
            elif d==14:
                f=val//10
            elif d==15:
                f=val//1000
            elif d==16:
                f=val//25.4
            elif d==17:
                f=(val*100000)//2.54
            elif d==18:
                f=(val*2.54)//100
            elif d==19:
                f=val*2.54
            elif d==20:
                f=val*25.4
            else:
                f="\" invalid input \""
            print(f"the coverted value is {f}")
        
        elif choice=='b':
            d=int(input("\n 1- ms to sec \n 2- ms to min \n 3- ms to hr  \n 4- ms to day \n 5- sec to ms \n 6- sec to min \n 7- sec to hr \n 8- sec to day \n 9- min to ms \n 10- min to sec \n 11- min to hr \n 12- min to day \n 13- hr- ms \n 14- hr to sec \n 15- hr to min \n 16- hr to day \n 17- day to ms \n 18- day to sec \n 19- day to min \n 20- day to hr \n\n enter your choice :- "))
            if d==1:        
                f=val*1000
            elif d==2:
                f=(val*1000)//60
            elif d==3:
                f=(val*1000)//3600
            elif d==4:
                f=(val*1000)//(3600*24) 
            elif d==5:
                f=val//1000
            elif d==6:
                f=val//60
            elif d==7:
                f=val//3600
            elif d==8:
                f=val//(3600*24) 
            elif d==9:
                f=val*1000*60
            elif d==10:
                f=val*60
            elif d==11:
                f=val//60
            elif d==12:
                f=val//(60*24) 
            elif d==13:
                f=val*3600
            elif d==14:
                f=val*60
            elif d==15:
                f=val*3600//1000
            elif d==16:
                f=val//24 
            elif d==17:
                f=val//1000
            elif d==18:
                f=val*24*60
            elif d==19:
                f=val*24
            elif d==20:
                f=val*3600*24           
            else:
                f="\"invalid input\""
            print(f" the converted value is {f}")
        if choice=='c':
            d=int(input("\n 1- kg to gm \n 2- kg to mg \n 3- kg to pound  \n 4- kg to ton \n 5- gm to kg \n 6- gm to mg \n 7- gm to pound \n 8- gm to ton \n 9- mg to kg \n 10- mg to gm \n 11- mg to pound \n 12- mg to ton \n 13- pound to kg \n 14- pound to gm \n 15- pound to mg \n 16- pound to ton \n 17- ton to kg \n 18- ton to gm \n 19- ton to mg \n 20- ton to pound \n"))
            if d==1:
                f=val*1000
            elif d==2:
                f=val*1000*1000
            elif d==3:
                f=val*1000*453.59237
            elif d==4:
                f=val*1000*453.59237*2000 
            elif d==5:
                f=val//1000
            elif d==6:
                f=val*1000
            elif d==7:
                f=val//453.59237
            elif d==8:
                f=val//(453.59237*2000) 
            elif d==9:
                f=val//1000000
            elif d==10:
                f=val//1000
            elif d==11:
                f=val//(453.59237*1000)
            elif d==12:
                f=val//(453.59237*1000*2000) 
            elif d==13:
                f=val//(1000*453.59237)
            elif d==14:
                f=val*453.59237
            elif d==15:
                f=val*453.59237*1000
            elif d==16:
                f=val//2000 
            elif d==17:
                f=val//(1000*2000*453.59237)
            elif d==18:
                f=val*453.59237*2000
            elif d==19:
                f=val*100
            elif d==20:
                f=val*3600*24 
            else:
                f="\"invalid input\""              
            print(f" the converted value is {f}")                                
            
        elif choice=='d':
            d=int(input("\n 1- farenhite to celcius \n 2- celcius to farenhite \n 3-kelvin to celcius \n 4- celcius to kelvin \n 5-kelvin to farenhite \n 6-farenhite to kelvin"))
            if d==1:
                f=(val-32)*(5//9)
            elif d==2:
                f=(val*(9//5))+32
            elif d==3:
                f=val-273.15
            elif d==4:
                f=val+273.15
            elif d==5:
                f=(val-273.15)*(9//5)+32
            elif d==6:
                f=(val-32)*(5//9)+273
            else:
                f="\"invalid input\""              
            print(f" the converted value is {f}")   
        
        elif choice=='e':
            d=int(input("\n 1- joule to calories \n 2- calories to joules \n"))
            if d==1:
                f=val*0.23901
            elif d==2:
                f=val*4.184
            print(f" the converted value is {f}")
    
    again=input("do you want to exit app ?  ")