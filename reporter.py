from calculator import getBalance, getTotalDeposits, getTotalWithdrawals

def showTransactions(transactions):
    if len(transactions) == 0:
        print("No transactions yet")
        return
    print("\nID   Type       Amount      Note")
    print("-" * 40)
    for item in transactions:
        print(item["id"], "  ", item["type"], "   ", item["amount"], "   ", item["note"])
    print("-" * 40)

def showSummary(transactions):
    bal = getBalance(transactions)
    dep = getTotalDeposits(transactions)
    wit = getTotalWithdrawals(transactions)
    print("\nACCOUNT SUMMARY")
    print("Total Transactions :", len(transactions))
    print("Total Deposits     :", dep)
    print("Total Withdrawals  :", wit)
    print("Current Balance    :", bal)

def filterType(transactions, kind):
    result = []
    for item in transactions:
        if item["type"].lower() == kind.lower():
            result.append(item)
    return result