import random

def 猜數字遊戲():
    while True:
        print("歡迎來到猜數字遊戲！")
        最小數字 = 1
        最大數字 = 100
        隨機數字 = random.randint(最小數字, 最大數字)

        嘗試次數 = 0
        最大嘗試次數 = 10

        while 嘗試次數 < 最大嘗試次數:
            嘗試次數 += 1
            猜測數字 = int(input(f"請猜一個介於 {最小數字} 和 {最大數字} 之間的數字 (第 {嘗試次數} 次嘗試): "))

            if 猜測數字 < 隨機數字:
                print("猜的數字太小了。")
            elif 猜測數字 > 隨機數字:
                print("猜的數字太大了。")
            else:
                print(f"恭喜你，猜對了！答案是 {隨機數字}。你總共嘗試了 {嘗試次數} 次。")
                break
        else:
            print(f"很遺憾，猜數字的次數已達到 {最大嘗試次數} 次。答案是 {隨機數字}。")

        是否重新 = input("是否要重新開始遊戲? (Y)是 (N)否: ").upper()
        if 是否重新 != "Y":
            print("已離開猜數字遊戲")
            break

# 程式的主要部分
print("歡迎來到小工具")

小工具 = int(input("請輸入要什麼小工具(1)計算機 (2)取得現在日期和時間 (3)猜數字遊戲:"))

def 取得現在日期和時間():
    from datetime import datetime

    while True:
        now = datetime.now()

        year = now.year
        month = now.month
        day = now.day
        time = now.strftime("%H:%M:%S")
        weekday = now.strftime("%A")

        print(f"現在是 {year}年")
        print(f"現在是 {month}月")
        print(f"現在是 {day}日")
        print(f"現在是 {time}")

        weekdays = {
            "Monday": "星期一",
            "Tuesday": "星期二",
            "Wednesday": "星期三",
            "Thursday": "星期四",
            "Friday": "星期五",
            "Saturday": "星期六",
            "Sunday": "星期日"
        }

        if weekday in weekdays:
            print(f"今天是{weekdays[weekday]}")

        是否重新 = input("是否要重新取得? (Y)是 (N)否: ").upper()
        if 是否重新 == "Y":
            print("已重新開始計算")
        else:
            print("已離開")
            break

def 計算機():
    while True:
        print("歡迎來到計算機，請按照步驟輸入")

        小數點使用 = input("是否要使用小數點(Y)是 (N)否:").upper()
        if 小數點使用 == "Y":
            第1個數字 = float(input("請輸入要計算的第1個數字: "))
        else:
            第1個數字 = int(input("請輸入要計算的第1個數字: "))

        計算符號 = input("請輸入你計算的符號(+-*/): ")

        if 小數點使用 == "Y":
            第2個數字 = float(input("請輸入要計算的第2個數字: "))
        else:
            第2個數字 = int(input("請輸入要計算的第2個數字: "))

        if 計算符號 == "+":
            總和_加 = 第1個數字 + 第2個數字
            print(f"={總和_加}")
        elif 計算符號 == "-":
            總和_減 = 第1個數字 - 第2個數字
            print(f"={總和_減}")
        elif 計算符號 == "*":
            總和_乘 = 第1個數字 * 第2個數字
            print(f"={總和_乘}")
        elif 計算符號 == "/":
            if 第2個數字 != 0:
                總和_除 = 第1個數字 / 第2個數字
                print(f"={總和_除}")
            else:
                print("除數不能為0")
        elif 計算符號 == "#":
            print("恭喜找到彩蛋")
        else:
            print("計算錯誤")

        是否繼續 = input("是否要繼續計算? (Y)是 (N)否: ").upper()
        if 是否繼續 == "Y":
            print("已重新開始計算")
        else:
            print("已離開")
            break

if 小工具 == 1:
    計算機()
elif 小工具 == 2:
    取得現在日期和時間()
elif 小工具 == 3:
    猜數字遊戲()
else:
    print("錯誤")
