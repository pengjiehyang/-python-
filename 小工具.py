import random
from datetime import datetime

def 猜數字遊戲():
    while True:
        print("歡迎來到猜數字遊戲！")
        隨機數字 = random.randint(1, 100)
        嘗試次數 = 0

        while 嘗試次數 < 10:
            嘗試次數 += 1
            猜測數字 = float(input(f"猜一個 1 到 100 的數字 (第 {嘗試次數} 次): "))

            if 猜測數字 < 隨機數字:
                print("太小了。")
            elif 猜測數字 > 隨機數字:
                print("太大了。")
            else:
                print(f"恭喜！答案是 {隨機數字}，你嘗試了 {嘗試次數} 次。")
                break
        else:
            print(f"很遺憾，答案是 {隨機數字}。")

        if input("重新開始遊戲? (Y/N): ").upper() != "Y":
            break

def 取得現在日期和時間():
    while True:
        now = datetime.now()
        print(f"現在是 {now.year}年 {now.month}月 {now.day}日 {now.strftime('%H:%M:%S')}")
        print(f"今天是 {now.strftime('%A')}")

        if input("重新取得時間? (Y/N): ").upper() != "Y":
            break

def 計算機():
    while True:
        第1個數字 = input("輸入第1個數字: ")
        計算符號 = input("輸入計算符號 (+ - * /): ")
        第2個數字 = input("輸入第2個數字: ")

        # 自動偵測數字類型
        if '.' in 第1個數字 or 'e' in 第1個數字.lower():
            第1個數字 = float(第1個數字)
        else:
            第1個數字 = int(第1個數字)

        if '.' in 第2個數字 or 'e' in 第2個數字.lower():
            第2個數字 = float(第2個數字)
        else:
            第2個數字 = int(第2個數字)

        if 計算符號 == "+":
            print(f"結果: {第1個數字 + 第2個數字}")
        elif 計算符號 == "-":
            print(f"結果: {第1個數字 - 第2個數字}")
        elif 計算符號 == "*":
            print(f"結果: {第1個數字 * 第2個數字}")
        elif 計算符號 == "/":
            if 第2個數字 != 0:
                print(f"結果: {第1個數字 / 第2個數字}")
            else:
                print("除數不能為0")
        else:
            print("無效的運算符號")

        if input("繼續計算? (Y/N): ").upper() != "Y":
            break

def 主程式():
    print("歡迎來到小工具")
    選擇 = int(input("選擇功能 (1)計算機 (2)取得時間 (3)猜數字: "))
    if 選擇 == 1:
        計算機()
    elif 選擇 == 2:
        取得現在日期和時間()
    elif 選擇 == 3:
        猜數字遊戲()
    else:
        print("錯誤的選擇")

主程式()
