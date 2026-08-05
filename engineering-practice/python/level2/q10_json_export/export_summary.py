import csv
import json


def aggregate(csv_path: str = "orders.csv") -> dict:
    # TODO: q09と同じ集計処理
    pass


def export_json(data: dict, out_path: str = "summary.json") -> None:
    # TODO: JSONファイルに書き出す
    pass


if __name__ == "__main__":
    export_json(aggregate())
