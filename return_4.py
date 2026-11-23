import random 
# תרגיל 1
# i=0
# while i<10:
#     print(i)
#     i=i+1
    


# תרגיל 2
# for i in range(10):
#     print(i)
# print("START!")

# תרגיל 3
# i=0
# while i<50:
#     if i%2==0:
#         print(i)
#     i=i+1


# תרגיל 4
# i=0
# number=int(input("number"))
# while i<=(number*4):
#     if i%number==0:
#        print(i)
#     i=i+1
# תרגיל 5
# i=0
# while i<101:
#     i+=i
# print(i)
# total=0
# for i in range(100):
#     total+=i
# print(total)

# # תרגיל 6
# while True:
#     password=input("password")
#     if password==" Python123":
#         print("Welcome!")
        #    break
    
# תרגיל 7
# secret_number= 27
# while True:
#     password=int(input("password"))
#     if password==secret_number:
#         print("you succeeded")
#         break

# תרגיל 8
# secret_number= 0
# total=0
# while True:
#     password=int(input("number"))
#     total+=password

#     if password==secret_number:
#         print("you succeeded")
#         print(total)
#         break

        
# תרגיל 9    # 
# secret_number= 999
# total=0
# average=0
# counter=0
# while True:
#     grade=int(input("Enter a grade"))
#     if grade==secret_number:
#           break
#     counter+=1
#     total+=grade
    
# print(total)
# print(total/counter)
# print(counter)
    
# תרגיל 10
# secret_number= 0
# total=0
# average=0
# counter=0
# while True:
#     number=int(input("Enter a number"))
#     if number<0:
#           break
#     counter+=1
#     total+=number
    
# print(total)
# print(total/counter)
# print(counter)

# תרגיל 11
# number=int(input("Enter a number"))
# for i in range(11):
#     print(i*number)

# תרגיל 12
# counter=0
# number=int(input("Enter a number"))

    
# while number>0:
        
#         counter+=1
#         number=number//10
        
# print(counter)

# תרגיל 13
# output=0
# a=0
# output_1=0
# number=int(input("Enter a number"))
# t=0 
# while number>0:       
        
#         t=t*10+number%10      
#         number=number//10
        
# print(t)

# תרגיל 14
# conto=2
# number=int(input("Enter a number"))
# while conto<number:     
#     if number>1 and number % conto != 0:
#           print("Prime number")
#           break
#     elif number % conto == 0 :
        
#         conto+=1
#         continue
# print("A non-prime number")    
        
        
        
   
    
        




# תרגיל 15
# balance = 5000
# while True:
#         print("1. Check balance.")
#         print("2. Deposit money.")
#         print("3.  Withdraw money.")
#         print("4.  Log out.")
#         choice=input("choice")
#         if choice=="1":
#                 print(balance)

#         if choice=="2":
#                 choice_1=int(input("amoat"))
#                 balance+=choice
#         if choice=="3":
#                 choice_1=int(input("amoat"))
#                 balance-=choice

#         if choice=="4":
#                 break
# תרגיל 16
# conet=0
# while conet<15:
#     conet+=1
#     print(conet)
     

# תרגיל 17
# conet=0
# while conet<30:
#     conet+=1
#     if conet%3==0:
#        continue
#     print(conet)

# תרגיל 18
# secret_number= 100
# while True:
#     password=int(input("password"))
#     if password==secret_number:
#         print("you succeeded")
#         break

# תרגיל 19
# for i in range(1,21):
#     print(i)

# תרגיל 20
# for i in range(0,101,5):
#     print(i)

# תרגיל 21
# total=0
# for i in range(100):
#     total+=i
# print(total)

# תרגיל 22
# number=int(input("Enter a number"))
# for i in range(11):
#     print(i*number)

# תרגיל 23
# total=0
# number_1=int(input("Enter a number"))
# number_2=int(input("Enter a number"))
# for i in range(number_1,number_2+1):
#     total+=i
# print(total)

# תרגיל 24
# for i in range(100):
#     if i%3==0 and i%5==0:
#         print(i)

# תרגיל 25
# rows=int(input("rows"))
# columns=int(input("columns"))
# for i in range(columns):
#     print("*"*rows)
   

# תרגיל 26
# for i in range(6):
#     print("*"*i)

# תרגיל 27
# for i in range(1,11):
#     for g in range(1,11):
#          print(g*i, end=' ')
#     print()

# תרגיל 28
# for i in range(1,6):
#     for g in range(1,6):
#          print(i,g)
#     print()

# תרגיל מסכם
# while True:
#     print("===== MATH GAME =====")
#     print("1. Start Game")
#     print("2. View Instructions")
#     print("3. Exit")
#     choose=input("Choose:")
#     total=0


#     if choose=="1":
#         print("1")
#         for i in range(10):
#             # x=random.randint(1,10)
#             # print(x)
#             x=i+1
#             number=int(input(f"Answer the exercise  {i}  +1."))
#             if x==number:
#                 total+=1
#             else:
#                 continue
            
            
#         print(total)
#         break

#     if choose=="2":
#         print("""The program will present a series of 10 arithmetic exercises.
#             In each exercise, the user will enter an answer.
#             The program will check whether the answer is correct.
#             For each correct answer, the user will receive a point.
#             At the end, the final score will be displayed.""")
             
#     if choose=="3":
#         break
     







