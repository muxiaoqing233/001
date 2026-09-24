"""Project 03: 简易命令行待办清单"""


def show_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("当前没有待办事项。")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main() -> None:
    tasks: list[str] = []

    while True:
        print("\n1. 查看  2. 添加  3. 删除  0. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("输入待办事项：").strip()
            if task:
                tasks.append(task)
                print("已添加。")

        elif choice == "3":
            show_tasks(tasks)
            raw = input("输入要删除的序号：").strip()
            if raw.isdigit():
                index = int(raw) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"已删除：{removed}")
                else:
                    print("序号不存在。")

        elif choice == "0":
            print("再见。")
            break

        else:
            print("无效选项。")


if __name__ == "__main__":
    main()
