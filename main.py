from transactionmanager import addDeposit, addWithdraw, deleteTransaction
from reporter import showTransactions, showSummary, filterType
from calculator import getBalance

def main():
    transactions = []
    print("Welcome to Mini Banking Logger")

    while True:
        print("\nMINI BANKING LOGGER")
        print("1. Add Deposit")
        print("2. Add Withdrawal")
        print("3. View All Transactions")
        print("4. View Account Summary")
        print("5. View Only Deposits")
        print("6. View Only Withdrawals")
        print("7. Delete Transaction")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amt = float(input("Enter deposit amount: "))
                note = input("Enter note: ")
                if note == "":
                    note = "No note"
                addDeposit(transactions, amt, note)
            except:
                print("Invalid amount")

        elif choice == "2":
            try:
                amt = float(input("Enter withdrawal amount: "))
                note = input("Enter note: ")
                if note == "":
                    note = "No note"
                bal = getBalance(transactions)
                addWithdraw(transactions, amt, note, bal)
            except:
                print("Invalid amount")

        elif choice == "3":
            showTransactions(transactions)

        elif choice == "4":
            showSummary(transactions)

        elif choice == "5":
            onlyDep = filterType(transactions, "Deposit")
            showTransactions(onlyDep)

        elif choice == "6":
            onlyWit = filterType(transactions, "Withdraw")
            showTransactions(onlyWit)

        elif choice == "7":
            showTransactions(transactions)
            try:
                tid = int(input("Enter ID to delete: "))
                deleteTransaction(transactions, tid)
            except:
                print("Invalid ID")

        elif choice == "8":
            print("Thank you. Bye!")
            break

        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")

main()