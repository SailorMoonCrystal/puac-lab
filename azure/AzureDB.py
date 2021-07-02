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
            self.cursor.execute("SELECT id,name,message,date from guestbook")
            data = self.cursor.fetchall()
            return data
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)

    def azureAddData(self, name, message, date):
        try:
            self.cursor.execute(
                f"INSERT into guestbook (name,message,date) values ('{name}', '{message}', '{date}')"
            )
            self.conn.commit()
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)

    def azureDeleteData(self, id):
        try:
            self.cursor.execute(f"DELETE FROM guestbook WHERE id = '{id}'")
            self.conn.commit()
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)

    def azureUpdateData(self, id, name, message):
        try:
            self.cursor.execute(f"UPDATE guestbook SET name='{name}', message='{message}' WHERE id = '{id}'")
            self.conn.commit()
        except pypyodbc.DatabaseError as exception:
            print("Failed to execute query")
            print(exception)
            exit(1)