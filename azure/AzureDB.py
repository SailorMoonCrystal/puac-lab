import pypyodbc
import azure.azurecred as azurecred


class AzureDB:
    dsn = (
        "DRIVER="
        + azurecred.AZDBDRIVER
        + ";SERVER="
        + azurecred.AZDBSERVER
        + ";PORT=1433;DATABASE="
        + azurecred.AZDBNAME
        + ";UID="
        + azurecred.AZDBUSER
        + ";PWD="
        + azurecred.AZDBPW
    )

    def __init__(self):
        self.conn = pypyodbc.connect(self.dsn)
        self.cursor = self.conn.cursor()

    def finalize(self):
        if self.conn:
            self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def __enter__(self):
        return self

    def azureGetData(self):
        try:
            self.cursor.execute("SELECT nick,message,date from guestbook")
            data = self.cursor.fetchall()
            return data
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)

    def azureAddData(self, nick, message, date):
        try:
            self.cursor.execute(
                f"INSERT into guestbook (nick,message,date) values ('{nick}', '{message}', '{date}')"
            )
            self.conn.commit()
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)


# zakomentowana funkcja usuwająca rekord z bazy gdzie name = Adam
# def azureDeleteData(self):
# self.cursor.execute("DELETE FROM data WHERE name = 'Adam'")
# self.conn.commit()
