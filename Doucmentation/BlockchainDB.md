# Database Class

This class manages a simple database for tracking user balances using SQLite. It interacts with a table named `blockchain` that stores information such as server ID, user ID, and the amount of currency (or any numeric value) associated with that user in the system.

## Methods

---

### `__init__()`

**Description:**:  <br>
This is the constructor method. It initializes the connection to the SQLite database `money.db` and sets up a cursor to interact with the database.

**Usage**:<br>
```python
db = Database()
```

---

### `create_user(serverid: str, userid: int)`
**Description**:<br>
Inserts a new user into the `blockchain` table with the specified `serverid` and `userid`, initializing their balance to `0`

**Parameters:**<br>
- `serverid` (str): The ID of the server where the user belongs.<br>
- `userid` (int): The ID of the user being created.

**Usage:**
```python
db.create_user("12345", 67890)
```

---

### `check_if_user_exists(serverid: str, userid: int) -> bool`
**Description**:<br>
Checks if a user exists in the `blockchain` table by querying based on the `serverid` and `userid`.

**Returns:**

- `True` if the user does *not* exist in the database.<br>
- `False` if the user exists.

**Usage:**
```python
exists = db.check_if_user_exists("12345", 67890)
```

---

### `get_balance(serverid: str, userid: int) -> int`
**Description**:<br>

Retrieves the current balance of the specified user from the `blockchain` table. If the user does not exist, it returns `0`.

**Returns:**

`int`: The user's current balance.

**Parameters:**

- `serverid` (str): The ID of the server where the user belongs.<br>
- `userid` (int): The ID of the user whose balance is being retrieved.

**Usage:**
```python
balance = db.get_balance("12345", 67890)
```

---

### `add_balance(serverid: str, userid: int, amt: int) -> None`

**Description:**<br>
Adds a specified amount to a user's balance in the `blockchain` table. If the user does not exist, they are automatically created with an initial balance of `0`. Negative amounts are ignored.

**Parameters:**<br>
- `serverid` (str): The ID of the server where the user belongs.
- `userid` (int): The ID of the user whose balance is being updated.
- `amt` (int): The amount to add to the user's balance. Negative amounts are ignored.

**Usage:**<br>
```python
db.add_balance("12345", 67890, 100)
```

---

### `sub_balance(serverid: str, userid: int, amt: int) -> None`

**Description:**<br>
Subtracts a specified amount from a user's balance in the `blockchain` table. If the user does not exist, they are automatically created with an initial balance of `0`. Negative amounts are ignored.

**Parameters:**<br>
- `serverid` (str): The ID of the server where the user belongs.
- `userid` (int): The ID of the user whose balance is being updated.
- `amt` (int): The amount to subtract from the user's balance. Negative amounts are ignored.

**Usage:**<br>
```python
db.sub_balance("12345", 67890, 50)
```

---

# NOTES:
- The database is committed (self.db.commit()) every time a balance update is performed.
- The code assumes a table named blockchain exists with columns for serverid, userid, and amount.
