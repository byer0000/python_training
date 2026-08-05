import csv
import json


class Inventory:
    def __init__(self):
        self.stock = {}

    def load_orders(self, csv_path: str) -> None:
        # TODO: CSVを読み込み、商品ごとの合計金額を self.stock に集計する
        pass

    def export_json(self, out_path: str = "stock_summary.json") -> None:
        # TODO: self.stock をJSONに書き出す
        pass


if __name__ == "__main__":
    inv = Inventory()
    inv.load_orders("orders.csv")
    inv.export_json()
