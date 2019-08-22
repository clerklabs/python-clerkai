from decimal import Decimal
from io import StringIO

import pandas as pd

from clerkai.transactions.parsers.parse_utils import \
    convert_european_amount_to_decimal


def test_convert_european_amount_to_decimal():
    foo = convert_european_amount_to_decimal("123.45")
    assert foo == Decimal("123.45")
    foo = convert_european_amount_to_decimal("123,45")
    assert foo == Decimal("123.45")
    foo = convert_european_amount_to_decimal(123.45)
    assert foo == Decimal("123.45")


def test_read_csv_with_decimal():
    df = pd.read_csv(StringIO("foo,bar,amount\nzoo,zar,123.45\n"),
                     converters={'amount': convert_european_amount_to_decimal})
    assert type(df["amount"][0]) == Decimal
    # df = pd.read_csv(StringIO("foo,bar,amount\nzoo,zar,123.45\n"), dtype={'amount': Decimal})
    # assert type(df["amount"][0]) == Decimal