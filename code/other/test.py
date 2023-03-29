array = [[0] * 2 for k in range(10)]

count = 1


for i in range(2):
    a = open("test" + str(count) + '.txt', 'w', encoding='utf-8')
    a.write(f"大家好我是林佳生\n")
    a.write(f"我現在非常想睡覺\n")
    a.close()
    count += 1
