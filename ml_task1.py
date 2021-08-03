sum=0
print("Enter 6 numbers")

num_list=[]

for i in range(6):
    val=int(input())
    num_list.append(val)
    
for j in range(6):
    sum=sum + num_list[j]
num_list.sort()
print(num_list)
print("Largest:",num_list[5])
print("Smallest:",num_list[0])
print(sum)

