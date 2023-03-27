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
        stuQuan = int(input("輸入學生數> "))
        break
    except KeyboardInterrupt:
        print("Good bye~")
    except ValueError:
        print("請輸入數值，不接受文字、空值")

v = stuQuan - 1

while knum == None:
    try:
        knum = int(input("輸入挑過學生數量，如無須跳過，按 ctrl^c> "))
        break
    except ValueError:
        print("請輸入數值，不接受文字、空值")
    except KeyboardInterrupt:
        print("")
        print("無須跳過")
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
        tempA = int(input(f"輸入跳過學生之號碼> "))
        while condition == True:
            if c + 1 == knum:
                c = 0
                break
            if tempA == known[c][0]:
                c = 0
                condition = False 
            c += 1
        tempB = int(input(f"輸入{tempA}號之順序> "))
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
            
    except ValueError:
        print("請輸入數值，不接受文字、空值")
    except KeyboardInterrupt:
        print("請輸入數值")

for n in range(knum):
    data[known[n][1] - 1] = known[n][0] 

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
    print(f"第{t + 1}個: {data[t]} 號")

print("")
print("按 ctrl^c 結束程式")
m = 1

while m > 0:
    try:
        input()
    except KeyboardInterrupt:
        m = 0
        print("Good Bye.")
        time.sleep(0.8)