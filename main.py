def add_expense(expenses, category, amount):
    expense = {"category": category, "amount": amount}
    expenses.append(expense)
    return True

def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    return total

def show_stats(expenses):
    if not expenses:
        print("Пока нет расходов.")
        return
    stats = {}
    for item in expenses:
        cat = item["category"]
        stats[cat] = stats.get(cat, 0) + item["amount"]
    print("\nСтатистика по категориям")
    for cat, total in stats.items():
        print(f"{cat}: {total:.2f} RUB")
    print(f"ИТОГО: {calculate_total(expenses):.2f} RUB\n")

def main():
    my_expenses = []
    print("Добро пожаловать в Кошелёк")
    while True:
        print("\n1. Добавить расход")
        print("2. Показать статистику")
        print("3. Выход")
        choice = input("Выбери действие (1-3): ")

        if choice == "1":
            category = input("Категория расхода: ")
            try:
                amount = float(input("Введи сумму расхода: "))
                if amount <= 0:
                    print("Введена некорректная сумма")
                else:
                    add_expense(my_expenses, category, amount)
                    print(f"Расход добавлен")
            except ValueError:
                print("Введена некорректная сумма")

        elif choice == "2":
            show_stats(my_expenses)

        elif choice == "3":
            print("До свидания! Будем ждать Вас снова.")
            break
        else:
            print("Это действие недоступно")

test_expenses = []
add_expense(test_expenses, "Транспорт", 150)
add_expense(test_expenses, "Одежда", 500)
assert calculate_total(test_expenses) == 650
assert calculate_total([]) == 0
print("Автотесты пройдены успешно! Программа готова к работе.\n")

if __name__ == "__main__":
    main()