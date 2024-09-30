import sqlite3
from random import randint
from blockchainDB import BlockchainDatabase

class TransactionDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('money.db')
        self.cursor = self.connection.cursor()

    def create_transaction(self, userid: int, amt: int) -> None:
        transaction_id = randint(1, 1000000)
        self.cursor.execute("""INSERT INTO transactions (?, ?, ?, ?)""", (userid, transaction_id, amt, 0))
        self.connection.commit()


    def approve_transaction(self, userid: int, transaction_id: int) -> bool:
        self.cursor.execute("""SELECT * FROM transactions WHERE userid = ? AND transactionid = ?""", (userid, transaction_id))
        row = self.cursor.fetchone()
        if row is None:
            return False
        else:
            self.cursor.execute("""UPDATE transactions SET approved = ? WHERE userid = ? AND transactionid = ?""", (1, userid, transaction_id))
            self.connection.commit()
            return True


    def claim_transaction(self, server_id: str, userid: int, transaction_id: int) -> None:
        self.cursor.execute("""SELECT * FROM transactions WHERE userid = ? AND transactionid = ?""", (userid, transaction_id))
        row = self.cursor.fetchone()
        if row is None:
            return
        else:
            bc = BlockchainDatabase()
            bc.add_balance(server_id, userid, row[2])
            bc.close_connection()

