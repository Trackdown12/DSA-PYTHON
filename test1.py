import problem as pb
l=[13,11,9,7,5,3,1]
num=int(input("enter number to check:"))
result=pb.find_position(l,num)
print(result)


test={"input":{"cards":[10,8,6,4,2],"query":8},"output":1}
print(pb.find_position(test["input"]["cards"],test["input"]["query"]))
print("program ends")