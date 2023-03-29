import processS as p
main = 1
count = 1 

while main == 1:
    try:
        print("""歡迎使用本抽籤系統 v1.2.0
    使用方法: 
    1.先輸入班級人數
    2.輸入需跳過人入，如果無須跳過，按非數字任意鍵跳過
    3.如需跳過，接下來輸入均為號碼再順序
    4.如有輸入錯誤或需重新執行，只需按下"ctrl + 任意鍵"重新啟動 

    時間表:
        第一週: 4/10~4/14 第1~8、9~16個(第一天、第二天) 
        第二週: 4/17~4/21 第17~24、25~32個
        第三週: 4/23~4/28 第33~39個 
                                                by Jason Lin  """)
        p.process(count)
        main = 0
    except KeyboardInterrupt:
        print("")
        count += 1
        print("重新啟動...", end='\n')
        
