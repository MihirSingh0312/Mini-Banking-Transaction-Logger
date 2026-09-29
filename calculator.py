def getBalance(transactions):
    bal = 0
    for item in transactions:
        if item["type"] == "Deposit":
            bal = bal + item["amount"]
        else:
            bal = bal - item["amount"]
    return bal

def getTotalDeposits(transactions):
    total = 0
    for item in transactions:
        if item["type"] == "Deposit":
            total = total + item["amount"]
    return total

def getTotalWithdrawals(transactions):
    total = 0
    for item in transactions:
        if item["type"] == "Withdraw":
            total = total + item["amount"]
    return total