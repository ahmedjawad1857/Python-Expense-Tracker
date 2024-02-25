# Expense-Tracker
from typing import Any
from datetime import datetime
import pandas as pd
import time
import random
class App: 
    def __init__(self)->None:
        self.currentBalance:int = 0
        self.expense:int  = 0
        self.income:int = 0
        self.history:list[dict[str,Any]] = []
        
    def addTransaction(self, transaction:int,description:str)->None:
        if transaction >= 0:
            self.currentBalance += transaction
            self.income += transaction
        else:    
            self.currentBalance += transaction
            self.expense = abs(self.expense + transaction)
        timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
        random_num = random.randint(0, 1000)  # Random number between 0 and 1000
        unique_id = f"{timestamp}-{random_num}"    
        newHistory:dict[str,Any] = {"id":str(unique_id), "amount":transaction,"description":description,"Created-On":datetime.now().strftime("%y/%m/%d %I:%M:%S %p"),"Last-Updated":"Not Updated" }   
        self.history.append(newHistory)    
    def deleteTransaction(self, id:str):
        for transaction in self.history:
            if transaction["id"] == id:
                index:int=self.history.index(transaction)
                removedTransaction : Any =  self.history.pop(index)
                if removedTransaction["amount"] >= 0:
                    self.currentBalance -= removedTransaction["amount"]
                    self.income -= removedTransaction["amount"]
                else:
                    self.currentBalance += -removedTransaction["amount"]
                    self.expense -= abs(removedTransaction["amount"])    
                print(f"Transaction {id} deleted successfully.")
                return
        print("Transaction not found.")
    def viewTransaction(self)->None:
        history_df:pd.DataFrame = pd.DataFrame(self.history)
        if self.history:
            print(history_df)    
        else:
            print("No transactions found.") 
            
            
    def updateTransaction(self, id: str, newAmount: int, newDescription: str) -> None:
     for transaction in self.history:
        if transaction["id"] == id:
            oldAmount:int = transaction["amount"]
            transaction["amount"] = newAmount
            transaction["description"] = newDescription
            transaction["Last-Updated"] = datetime.now().strftime("%y/%m/%d %I:%M:%S %p")
            # Update currentBalance, expense, and income
            self.currentBalance += newAmount - oldAmount
            if oldAmount >= 0:
                self.income -= oldAmount
            else:
                self.expense += oldAmount

            if newAmount >= 0:
                self.income += newAmount
            else:
                self.expense -= newAmount

            print("Transaction updated successfully.")
            return
    print("Transaction not found.")


            
app:App=App()            
while True:
    print("Welcome to the Expense Tracker!")
    print(f"Your Current Balance:  {app.currentBalance}")
    print(f"Your Expenses :  {app.expense}")
    print(f"Your Incomes : {app.income}")
    print("1. Add Transaction")
    print("2. Delete Transaction")
    print("3. Update Transaction")
    print("4. View Transaction")
    print("5. Exit")
    choice:str = input("Enter your choice: ")
    match choice:
      case "1":  
        amount:int = int(input("Enter the amount:Rs. "))
        description:str = input("Enter the description: ")
        app.addTransaction(amount,description)
      case "2":
        id:str = input("Enter the id: ")
        app.deleteTransaction(id)
      case "3":
          id1:str = input("Enter the id: ")
          Updated_Amount:int = int(input("Enter the Updated Amount:Rs. "))
          Updated_Description:str = input("Enter the Updated_Description: ")
          app.updateTransaction(id1,Updated_Amount,Updated_Description)  
      case "4":
        app.viewTransaction()
      case "5":
        break
      case _:
        print("Invalid choice.")