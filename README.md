# Mini-Banking-Transaction-Logger
The goal of this project is to make a simple program that can keep track of money transactions like deposits and withdrawals. It also helps in calculating the current balance and showing a summary. This project is made to practice the basic Python concepts we learned in class such as lists, dictionaries, functions, loops and conditionals.

# Goals
The goal of this project is to make a simple program that can keep track of money transactions like deposits and withdrawals. It also helps in calculating the current balance and showing a summary. This project is made to practice the basic Python concepts we learned in class such as lists, dictionaries, functions, loops and conditionals.

# Overview
Many times we need to note down our daily money transactions but doing it on paper is not convenient. This program allows the user to add deposits and withdrawals, check the balance, view all transactions and also delete any wrong entry. Everything is done through a simple menu. The data stays only while the program is running.

# Notes
This is a console based program. It does not use any external libraries. All data is stored in a list while the program is running. Once you close the program the data is lost because no file is used. 

# Requirements
- Python 3 should be installed
- No extra packages are needed

# Technologies Used
- Python 3
- Only basic Python features (lists, dictionaries, functions, loops)

# Features
- Add deposit
- Add withdrawal
- View all transactions
- View account summary (balance, total deposits, total withdrawals)
- View only deposits
- View only withdrawals
- Delete a transaction

# Project Structure
If using multiple files:
- main.py → contains the menu and main program flow
- transactionmanager.py → handles adding and deleting transactions
- calculator.py → calculates balance and totals
- reporter.py → shows transactions and summary
- datahandler.py → helps in finding transactions and generating IDs

You can also run everything from a single file if needed.

# How to Run
1. Keep all the files in the same folder (or use the single file version)
2. Open terminal in that folder
3. Type the command: python main.py
4. Follow the menu options

# Testing
You can test the program by adding some deposits and withdrawals. Check if the balance is calculated correctly. Try viewing only deposits or only withdrawals. Also test deleting a transaction and see if it gets removed. Enter wrong values to check if the program handles them properly. Finally check the summary to confirm totals are correct.

# Screenshots
0.Main Menu
<img width="1917" height="1020" alt="Screenshot 2026-09-29 220302" src="https://github.com/user-attachments/assets/71acc648-99ca-4b8e-852d-790c04c16d1b" />
1.Add Deposit
<img width="1916" height="1015" alt="Screenshot 2026-09-29 220738" src="https://github.com/user-attachments/assets/56018c2b-27e7-46e1-ba40-0cc9ad521333" />
2. Add Withdrawal
  <img width="1916" height="685" alt="Screenshot 2026-09-29 220813" src="https://github.com/user-attachments/assets/cf62fc92-67a3-429b-97eb-4baf35f88d1f" />
3. View All Transactions
<img width="1917" height="1016" alt="Screenshot 2026-09-29 220838" src="https://github.com/user-attachments/assets/1f405d20-cc19-4dce-936a-2d769de37860" />
4. View Account Summary
<img width="1917" height="1017" alt="Screenshot 2026-09-29 220858" src="https://github.com/user-attachments/assets/53f312ae-c9ee-4f3b-8024-5daae4f8dc94" />
5. View Only Deposits
<img width="1917" height="1016" alt="Screenshot 2026-09-29 220918" src="https://github.com/user-attachments/assets/022ece6c-7816-4e60-b201-8ce54348c1cf" />
6. View Only Withdrawals
<img width="1917" height="1015" alt="Screenshot 2026-09-29 220932" src="https://github.com/user-attachments/assets/83bdc165-607a-4e17-bdf7-46a7222546cb" />
7. Delete Transaction
<img width="1917" height="1017" alt="Screenshot 2026-09-29 220956" src="https://github.com/user-attachments/assets/33798db1-ad63-46ab-9d15-8a9a92a61679" />
8. Exit
<img width="1917" height="1020" alt="Screenshot 2026-09-29 221012" src="https://github.com/user-attachments/assets/460092ea-bca1-4b17-acb4-9ccb06528a27" />

