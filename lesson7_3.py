import random
while True:
    min = 1
    max = 10
    target=random.randint(1,10)
    count=0
    print("猜數字遊戲")
    while True:
        keyin=int(input(f'猜數字遊戲範圍{min}~{max}:'))
        count +=1
        if keyin<=max and keyin>=min :
            if keyin==target:
                print(f"對了 答案是{target}")
                print(f'你猜了{count}次')
                break
            elif keyin>target :
                print('錯了 小一點')
                print(f'你已經猜了{count}次')
            else :
                print('錯了 大一點')
                print(f'你已經猜了{count}次')
        else:
            print('請輸入提示範圍的數字')
    playagain=input("還要繼續嗎?(y,n)")
    if playagain =="n":
        break
print("遊戲結束")