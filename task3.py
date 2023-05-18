# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔Любое действие выводит сумму денег

MULTIPLICATOR = 50
TAX_FOR_THE_RICH = 0.1
FEE = 0.015
MIN_FEE = 30
MAX_FEE = 600
RICHNESS_THRESHOLD = 5_000_000
BONUS = 0.03

balance = 0
log = list()


def input_sum(for_taking=False):
    i = 1
    while i % MULTIPLICATOR != 0:
        i = int(input(f"Введите сумму, кратную {MULTIPLICATOR}: "))
        if for_taking and i > balance:
            i = 1
            print("На балансе недостаточно средств.")
    return i


def operations(mode):
    global balance
    txt = ''
    if balance > RICHNESS_THRESHOLD:
        txt += f'Снят налог на богатство в размере {balance * TAX_FOR_THE_RICH}. '
        balance -= balance * TAX_FOR_THE_RICH

    if mode == 'put':
        txt += put_money()
    elif mode == 'take':
        txt += take_money()

    if len(log) % 3 == 2:
        txt += f'Бонус {balance * BONUS} добавлен. '
        balance += balance * BONUS

    balance = round(balance, 2)
    txt += f"Текущий баланс = {balance}"
    log.append(txt)
    print(txt, '\n')


def put_money():
    global balance
    amount = input_sum()
    balance += amount
    return f"Добавлено {amount}. "


def take_money():
    global balance
    amount = input_sum(for_taking=True)
    fee = amount * FEE
    if fee < MIN_FEE:
        fee = MIN_FEE
    elif fee > MAX_FEE:
        fee = MAX_FEE
    balance -= amount + fee
    return f"Снято {amount} и еще комиссия {fee}. "


def menu():
    print("""Выберите одно из действий:
    1. Пополнить
    2. Снять
    3. Посмотреть лог операций
    4. Выйти""")
    match (input()):
        case '1':
            operations('put')
        case '2':
            operations('take')
        case '3':
            print(*log, sep='\n')
        case '4':
            exit()


while True:
    menu()
