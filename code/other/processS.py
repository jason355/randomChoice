import time 
import random

def process(count):
    c = 0
    k = 0
    q = 0
    r = 0
    w = 0
    d = 0
    f = 0
    date = ['4/10~4/14','4/10~4/14', '4/17~4/21','4/17~4/21', '4/24~4/28']
    knum = None
    condition = True

    while c < 1:
        try:
            stuQuan = int(input("輸入學生數> "))
            break
        except ValueError:
            print("請輸入數值，不接受文字、空值", end='\n')

    v = stuQuan - 1

    while knum == None:
        try:
            knum = int(input("輸入挑過學生數量，如無須跳過，按任意非數字鍵>"))
            if knum > stuQuan:
                print(f"請輸入< {stuQuan} 的數")
            else:
                break
        except ValueError:
            if knum == None:
                print("無須跳過", end='\n')
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
                print(f"Error: {tempA} or {tempB} get two or {tempB} > {stuQuan}. Please Check again.", end='\n')
                condition = True
            else:
                known[k][0] = tempA
                known[k][1] = tempB
                k += 1
                
        except ValueError:
            print("請輸入數值，不接受文字、空值", end='\n')
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
        
    for t in range(4):
        d = 0
        print("")
        print(f"第{t + 1}次:({date[t]})", end='\n')
        while d < 8:
            print(f"    第{d + 1}個:{data[f]}")
            #time.sleep(1)
            d += 1
            f += 1
    d = 0
    print("")
    print(f"第{t+2}次({date[4]}):")
    for r in range(7):
        print(f"    第{d + 1}個: {data[f]}")
        #time.sleep(1)
        f += 1
        d += 1

    print("")
    print("Writing to file...")
    
    f = 0
    
    result = open('List' + str(count) + '.txt', "w", encoding='utf-8')
    for t in range(4):
        d = 0
        print("")
        result.write(f"第{t + 1}次:({date[t]})\n")
        while d < 8:
            result.write(f"    第{d + 1}個:{data[f]}\n")
            d += 1
            f += 1
    d = 0
    result.write("")
    result.write(f"第{t+2}次({date[4]}):\n")
    for r in range(7):
        result.write(f"    第{d + 1}個: {data[f]}\n")
        f += 1
        d += 1
    result.close()
    m = 1

    while m > 0:
        state = input("輸入 s 結束程式.")
        if state == "s":
            m = 0
            print("Good Bye.")
            time.sleep(0.8)