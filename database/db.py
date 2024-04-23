from dataclasses import dataclass
from typing import Iterable
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import select, text
from sqlalchemy.orm import Session
import urllib
import json


@dataclass(frozen=True)
class ConnectionSettings:

    server: str
    database: str
    username: str
    password: str
    driver: str
    timeout: int


class AzureDbConnection:
    def __init__(self, conn_settings: ConnectionSettings, echo: bool = False) -> None:
        conn_params = urllib.parse.quote_plus(
            'Driver=%s;' % conn_settings.driver +
            'Server=tcp:%s.database.windows.net,1433;' % conn_settings.server +
            'Database=%s;' % conn_settings.database +
            'Uid=%s@%s;' % (conn_settings.username, conn_settings.server) +
            'Pwd=%s;' % conn_settings.password +
            'Encrypt=yes;' +
            'TrustServerCertificate=no;' +
            'Connection Timeout=%s;' % conn_settings.timeout
        )
        conn_string = f'mssql+pyodbc:///?odbc_connect={conn_params}'
        self.engine = create_engine(conn_string, echo=echo)
        self.session = Session(self.engine)

    def get_tables(self):
        inspector = inspect(self.engine)
        for table in inspector.get_table_names():
            result = self.get_select_table(table=table)
            print(result)

    def get_select_table(self, table: str):
        with self.session.begin():
            return self.session.execute(select('*').select_from(text(table))).fetchall()
