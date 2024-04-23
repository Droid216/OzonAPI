# -*- coding: utf-8 -*-

import asyncio
from datetime import datetime, timedelta

from ozon_sdk.ozon_api import OzonApi
from database import *
from config import *

import pprint


def get_db_table():
    conn_settings = ConnectionSettings(server=SERVER,
                                       database=DATABASE,
                                       driver=DRIVER,
                                       username=USER,
                                       password=PASSWORD,
                                       timeout=LOGIN_TIMEOUT)
    db_conn = AzureDbConnection(conn_settings=conn_settings)
    db_conn.get_tables()


def custom_json_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif not isinstance(obj, (int, str)):
        return obj.__dict__
    else:
        return obj


async def main():
    api_user = OzonApi(client_id=CLIENT_ID, api_key=API_KEY)
    end_month_day = datetime.now()
    start_month_day = end_month_day.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    print(start_month_day.strftime("%B %Y"), file=open('test.txt', 'a'))
    answer = await api_user.get_posting_fbo_list(dir="asc",
                                                 since=start_month_day.astimezone().isoformat(),
                                                 status="delivered",
                                                 to=end_month_day.astimezone().isoformat(),
                                                 financial_data=True,
                                                 analytics_data=True)

    for i, order in enumerate(answer.result):
        for product in order.products:
            print(product.offer_id)
            if product.offer_id == "8003/татумаш":
                print(f'date_of_sale: {order.created_at.strftime("%Y-%m-%d %H:%M:%S")}',
                      f'article: {product.offer_id}',
                      f'sales_price: {product.price},',
                      f'quantity: {product.quantity}',
                      sep="  /  ")
    print(len(answer.result))


async def main2():
    api_user = OzonApi(client_id=CLIENT_ID, api_key=API_KEY)
    end_month_day = datetime.now()
    start_month_day = end_month_day.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    answer = await api_user.get_finance_transaction_list(from_field=start_month_day.astimezone().isoformat(),
                                                         to=end_month_day.astimezone().isoformat(),
                                                         operation_type=["OperationAgentDeliveredToCustomer"])
    print(len(answer.result.operations))


async def main3():
    api_user = OzonApi(client_id=CLIENT_ID, api_key=API_KEY)
    answer = await api_user.get_posting_fbo(posting_number="28140089-0357-1",
                                            analytics_data=True,
                                            financial_data=True,
                                            translit=True)
    print(answer)


async def main4():
    client_id = CLIENT_ID
    operation_type = "delivered"
    api_user = OzonApi(client_id=CLIENT_ID, api_key=API_KEY)
    end_month_day = datetime.now()
    start_month_day = end_month_day.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    answer_transaction = await api_user.get_finance_transaction_list(from_field=start_month_day.astimezone().isoformat(),
                                                                     to=end_month_day.astimezone().isoformat(),
                                                                     operation_type=["OperationAgentDeliveredToCustomer"])
    for operation in answer_transaction.result.operations:
        delivery_schema = operation.posting.delivery_schema
        if not delivery_schema:
            continue
        posting_number = operation.posting.posting_number
        order_date = operation.posting.order_date
        if delivery_schema == 'FBO':
            answer_fbo = await api_user.get_posting_fbo(posting_number=posting_number,
                                                        analytics_data=True,
                                                        financial_data=True,
                                                        translit=True)
            if not answer_fbo.result:
                print(delivery_schema, posting_number)
            for product in answer_fbo.result.products:
                sku = product.sku
                offer_id = product.offer_id
                price = product.price
                quantity = product.quantity
                print(client_id, order_date, operation_type, offer_id, posting_number, sku, price, quantity,
                      sep=' / ', file=open('test.txt', 'a'))
        elif delivery_schema in ['FBS', 'RFBS']:
            answer_fbs = await api_user.get_posting_fbs(posting_number=posting_number,
                                                        analytics_data=True,
                                                        financial_data=True,
                                                        translit=True)
            if not answer_fbs.result:
                print(delivery_schema, posting_number)
            for product in answer_fbs.result.products:
                sku = product.sku
                offer_id = product.offer_id
                price = product.price
                quantity = product.quantity
                print(client_id, order_date, operation_type, offer_id, posting_number, sku, price, quantity,
                      sep=' / ', file=open('test.txt', 'a'))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main4())


