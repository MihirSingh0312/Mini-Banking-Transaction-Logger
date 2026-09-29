from datahandler import getNextId, findTransaction

def addDeposit(transactions, amount, note):
    if amount <= 0:
        print("Amount must be positive")
        return
    newItem = {}
    newItem["id"] = getNextId(transactions)
    newItem["type"] = "Deposit"
    newItem["amount"] = amount
    newItem["note"] = note
    transactions.append(newItem)
    print("Deposit added successfully")

def addWithdraw(transactions, amount, note, balance):
    if amount <= 0:
        print("Amount must be positive")
        return
    if amount > balance:
        print("Not enough balance")
        return
    newItem = {}
    newItem["id"] = getNextId(transactions)
    newItem["type"] = "Withdraw"
    newItem["amount"] = amount
    newItem["note"] = note
    transactions.append(newItem)
    print("Withdrawal done")

def deleteTransaction(transactions, tid):
    item = findTransaction(transactions, tid)
    if item == None:
        print("Transaction not found")
        return
    transactions.remove(item)
    print("Transaction deleted")