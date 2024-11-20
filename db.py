import sqlite3
from typing import Tuple

from hashMD5 import hash_md5


def get_user(username: str) -> Tuple[str, str]:
    with sqlite3.connect("User.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
    return user


def check_username_password(username: str, password: str) -> bool:
    user = get_user(username)
    if user == (username, hash_md5(password.encode("utf-8"))):
        return True
    return False


def main() -> None:
    with sqlite3.connect("User.db") as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                        username text,
                        password text
                        )""")
        c.execute(f"INSERT INTO users VALUES ('David', '{hash_md5(b'Lenovo')}')")
        c.execute(f"INSERT INTO users VALUES ('Moshe', '{hash_md5(b'Asus')}')")
        conn.commit()
        data = c.fetchall()


if __name__ == '__main__':
    main()
