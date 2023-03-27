import random
import time

c = 0
k = 0
q = 0
r = 0
w = 0
knum = None
condition = True

while c < 1:
    try:
        stuQuan = int(input("Enter student's quantity> "))
        break
    except KeyboardInterrupt:
        print("Good bye~")
    except ValueError:
        print("Please enter a number, not words or Null.")

v = stuQuan - 1

while knum == None:
    try:
        knum = int(input("Enter the quantity of the number or press ctrl^C to skip.> "))
        break
    except ValueError:
        print("Pleast enter quantity not words or Null.")
    except KeyboardInterrupt:
        print("")
        print("No known number.")
        knum = 0
        break

known = [[0]*2 for i in range(knum)]
note = [[0]*2 for m in range(stuQuan)]
nnote = [[0]*2 for e in range(stuQuan)]

for o in range(stuQuan):
    note[o][0] = o + 1
    note[o][1] = None

data = [0] * stuQuan


while k < knum:
    try:
        tempA = int(input("Enter a student number> "))
        while condition == True:
            if c + 1 == knum:
                c = 0
                break
            if tempA == known[c][0]:
                c = 0
                condition = False 
            c += 1
        tempB = int(input("Enter it's queue> "))
        while condition == True:
            if c+1 == knum:
                c = 0
                break 
            if tempB == known[c][1] or tempB > stuQuan:
                condition = False
            c += 1
        if condition == False:
            print(f"Error: {tempA} or {tempB} get two or {tempB} > {stuQuan}. Please Check again.")
            condition = True
        else:
            known[k][0] = tempA
            known[k][1] = tempB
            k += 1
            
        """ 
        if (tempA not in known) and (tempB not in known):
            if tempB < stuQuan:
                known[k][0] = tempA
                known[k][1] = tempB
                k += 1
                
            else:
                print(f"Please enter a quene that is smaller than {stuQuan}")
        else:
            print("Please enter a different student number or a different queue.") """
    except ValueError:
        print("Please enter a number, not words or Null.")
    except KeyboardInterrupt:
        print("Please enter student number and queue.")

for n in range(knum):
    #if known[k][0] not in data:
        #if known[k][1] not in data[range(stuQuan)]:
            #if known[k][1] < stuQuan:
                data[known[n][1] - 1] = known[n][0] 
            #else:
                #print(f"Error 003: Queue {known[k][1]} out of range. Please enter a queue that smaller than {stuQuan}")
                #known[k][1] = int(input(f"Enter a new queue for student {known[k][0]} that is smaller than {stuQuan}> "))
        #else:
            #print(f"Error 002: Queue {known[k][1]} has two number. Please check again.")
            #known[k][1] = int(input(f"Enter a new queue for student {known[k][0]}"))
    #else:
        #print(f"Error 001: Number {known[k][0]} has been in {known[k][1]}. Please check again.")
        #known[k][0] = int(input("Enter a new student number> "))
        #known[k][1] = int(input("Enter a new queue> "))


for l in range(stuQuan):
    if data[l] == 0 :
        note[l][1] = l
    elif data[l] != 0:
        note[data[l]-1][0] = None
#print(note)
while q < stuQuan:
    if note[q][0] != None: #and note[q][1] == None:
        nnote[w] = note[q][0]
        w += 1
    q += 1

for z in range(knum):
    del nnote[v]
    v -= 1

stuQuan_t = stuQuan
while r < stuQuan_t:
    if note[r][1] == None:
        del note[r]
        stuQuan_t -= 1
    else:
        r += 1   

for e in range((stuQuan - knum)):
    data[note[e][1]] = random.choice(nnote)
    del nnote[nnote.index(data[note[e][1]])]
    
for t in range(stuQuan):
    print(f"第{t + 1}個: {data[t]}")

print("")
print("Enter ctrl^c to end program.")
m = 1

while m > 0:
    try:
        input()
    except KeyboardInterrupt:
        m = 0
        print("Good Bye.")
        time.sleep(0.8)