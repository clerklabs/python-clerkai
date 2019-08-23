# lhv.ee.csv-specific parsing:
import datetime

import pandas as pd

from clerkai.transactions.parsers.parse_utils import amount_to_rounded_decimal


def ymd_date_to_datetime_obj(datetime_str):
    datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    return datetime_obj


def import_lhv_ee_csv_transaction_file(transaction_file):
    return pd.read_csv(transaction_file)


def lhv_ee_csv_transactions_to_general_clerk_format(df):
    normalized_df = pd.DataFrame()

    normalized_df['Date'] = df['Date'].apply(ymd_date_to_datetime_obj)
    normalized_df['Payee'] = df['Sender/receiver name']
    normalized_df['Memo'] = df['Description']
    normalized_df['Amount'] = df['Amount'].apply(amount_to_rounded_decimal)
    normalized_df['Balance'] = None

    normalized_df['Original data'] = df[
        ['Customer account no', 'Document no', 'Date', 'Sender/receiver account',
         'Sender/receiver name', 'Sender bank code', 'Empty',
         'Debit/Credit (D/C)', 'Amount', 'Reference number', 'Archiving code',
         'Description', 'Fee', 'Currency', 'Personal code or register code',
         'Sender/receiver bank BIC', 'Ultimate debtor name',
         'Transaction reference', 'Account servicer reference']].to_dict(
        orient='records')
    return normalized_df[['Date', 'Payee', 'Memo', 'Amount', 'Balance', 'Original data']]


def lhv_ee_csv_transactions_parser(transaction_file):
    df = import_lhv_ee_csv_transaction_file(transaction_file)
    return lhv_ee_csv_transactions_to_general_clerk_format(df)