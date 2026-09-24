"""Project 02: 猜数字游戏"""

import random

answer = random.randint(1, 100)
attempts = 0

print("我想了一个 1~100 的整数。")

while True:
    raw = input("猜一个数字：").strip()

    if not raw.isdigit():
        print("请输入整数。")
        continue

    guess = int(raw)
    attempts += 1

    if guess < answer:
        print("小了。")
    elif guess > answer:
        print("大了。")
    else:
        print(f"猜对了！答案是 {answer}，你一共猜了 {attempts} 次。")
        break
