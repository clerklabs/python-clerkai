from os.path import dirname, join, realpath

from clerkai.time_tracking.parsers.neamtime.tslog import \
    neamtime_tslog_time_tracking_entries_parser

test_data_dir_path = join(dirname(realpath(__file__)), "test_data")


def test_neamtime_tslog_time_tracking_entries_parser():
    # type: () -> None
    transaction_file_path = join(test_data_dir_path, "an-hour-of-something.tslog")
    transactions_df = neamtime_tslog_time_tracking_entries_parser(transaction_file_path)
    assert not transactions_df.empty
    actual = transactions_df.to_csv(index=False)
    actual_file_path = "%s%s" % (transaction_file_path, ".actual.csv")
    with open(actual_file_path, "w") as f:
        f.write(actual)
    expected_file_path = "%s%s" % (transaction_file_path, ".expected.csv")
    with open(expected_file_path, "r") as f:
        expected = f.read()
    assert actual == expected


def test_neamtime_tslog_time_tracking_entries_parser_2():
    # type: () -> None
    transaction_file_path = join(test_data_dir_path, "example-1-from-neamtime-reporting-2010-docs.with-paus-typo.tslog")
    transactions_df = neamtime_tslog_time_tracking_entries_parser(transaction_file_path)
    assert not transactions_df.empty
    actual = transactions_df.to_csv(index=False)
    actual_file_path = "%s%s" % (transaction_file_path, ".actual.csv")
    with open(actual_file_path, "w") as f:
        f.write(actual)
    expected_file_path = "%s%s" % (transaction_file_path, ".expected.csv")
    with open(expected_file_path, "r") as f:
        expected = f.read()
    assert actual == expected


def test_neamtime_tslog_time_tracking_entries_parser_3():
    # type: () -> None
    transaction_file_path = join(test_data_dir_path, "pause-handling.tslog")
    transactions_df = neamtime_tslog_time_tracking_entries_parser(transaction_file_path)
    assert not transactions_df.empty
    actual = transactions_df.to_csv(index=False)
    actual_file_path = "%s%s" % (transaction_file_path, ".actual.csv")
    with open(actual_file_path, "w") as f:
        f.write(actual)
    expected_file_path = "%s%s" % (transaction_file_path, ".expected.csv")
    with open(expected_file_path, "r") as f:
        expected = f.read()
    assert actual == expected
