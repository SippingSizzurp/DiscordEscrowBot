import sqlite3

class BlockchainDatabase:
    def __init__(self):
        self.db = sqlite3.connect('money.db')
        self.cursor = self.db.cursor()

    def create_user(self, serverid: str, userid:int):
        self.cursor.execute("""INSERT INTO blockchain (serverid, userid, amount) VALUES (?, ?, ?)""", (serverid, userid, 0))

    def check_if_user_exists(self, serverid: str, userid: int) -> bool:
        self.cursor.execute("""SELECT userid FROM blockchain WHERE serverid = ? AND userid = ?""", (serverid, userid))
        row = self.cursor.fetchone()
        if row:
            return False
        else:
            return True

    def get_balance(self, serverid: str, userid: int) -> int:
        self.cursor.execute("""SELECT amount FROM blockchain WHERE serverid = ? AND userid = ?""", (serverid, userid))
        row = self.cursor.fetchone()
        return row[0] if row else 0


    def add_balance(self, serverid: str, userid: int, amt: int) -> None:
        if amt < 0:
            return
        if self.check_if_user_exists(serverid, userid):
            self.create_user(serverid, userid)

        current_balance = self.get_balance(serverid, userid)
        new_balance = amt + current_balance

        self.cursor.execute("""UPDATE blockchain SET amount = ? WHERE serverid = ? AND userid = ?""", (serverid, userid, new_balance))
        self.db.commit()


    def sub_balance(self, serverid: str, userid: int, amt: int) -> None:
        if amt < 0:
            return
        if self.check_if_user_exists(serverid, userid):
            self.create_user(serverid, userid)

        current_balance = self.get_balance(serverid, userid)
        new_balance = amt - current_balance

        self.cursor.execute("""UPDATE blockchain SET amount = ? WHERE serverid = ? AND userid = ?""", (serverid, userid, new_balance))
        self.db.commit()


    def close_connection(self):
        self.db.close()