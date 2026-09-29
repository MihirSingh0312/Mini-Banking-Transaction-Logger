def getNextId(transactions):
    if len(transactions) == 0:
        return 1
    biggest = 0
    for item in transactions:
        if item["id"] > biggest:
            biggest = item["id"]
    return biggest + 1

def findTransaction(transactions, tid):
    for item in transactions:
        if item["id"] == tid:
            return item
    return None