# import math
# n = int(input())
# if n not in range(20,31):
#     print("Invalid Input.")
# else:
#     area = math.pi*n*n
#     print(round(area,2))


str = input()
l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
for i in str:
    index = l1.index(i)
    print(l2[index],end="")