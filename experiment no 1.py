start= int(input("Enter the start value:"))
stop=int(input("Enter the end value:"))
step=int(input("Enter trhe difference between each Number: "))


numbers_list= list(range(start,stop,step))

for num in numbers_list:
    print(num)