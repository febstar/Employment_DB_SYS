import sqlite3


class Database:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.data = ''

    def create_table(self, table_name, columns):
        columns_str = ', '.join([f'{name} {data_type}' for name, data_type in columns.items()])
        print(columns_str)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        values = tuple(data.values())
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        update_str = ', '.join([f'{column} = ?' for column in data.keys()])
        values = tuple(data.values())
        query = f'UPDATE {table_name} SET {update_str} WHERE {condition}'
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_data(self, table_name, condition):
        query = f'DELETE FROM {table_name} WHERE {condition}'
        self.cursor.execute(query)
        self.conn.commit()

    def select_data(self, table_name, columns=None, condition=None):
        if columns is None:
            column_str = '*'
        else:
            column_str = ', '.join(columns)

        query = f'SELECT {column_str} FROM {table_name}'
        if condition:
            query += f'WHERE {condition}'

        self.cursor.execute(query)
        self.data = self.cursor.fetchall()

    def close(self):
        self.conn.close()
