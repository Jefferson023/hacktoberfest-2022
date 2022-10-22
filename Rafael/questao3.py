def compute_balance(balance,debt,credit):
    return balance + credit - debt

if __name__ == '__main__':
    account_number = input()
    balance = float(input())
    debt = float(input())
    credit = float(input())
    actual_balance = compute_balance(balance,debt,credit)
    print(f"Saldo da conta {account_number}: {actual_balance:.2f}")
    if actual_balance < 0:
        print("Saldo negativo")
    else:
        print("Saldo Posistivo")