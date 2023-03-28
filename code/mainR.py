import process as p
main = 1
while main == 1:
    try:
        print("""歡迎使用本抽籤系統 v1.2.0
    使用方法: 
    1.先輸入班級人數
    2.輸入需跳過人入，如果無須跳過，按非數字任意鍵跳過
    3.如需跳過，接下來輸入均為號碼再順序
    4.如有輸入錯誤或需重新執行，只需按下"ctrl + 任意鍵"重新啟動 
                                                by Jason Lin  """)
        p.process()
        main = 0
    except KeyboardInterrupt:
        print("")
        print("重新啟動...", end='\n')
        
