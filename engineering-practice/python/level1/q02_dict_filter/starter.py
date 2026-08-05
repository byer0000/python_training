def filter_expensive(prices: dict, threshold: int = 100) -> dict:
    """threshold以上の商品だけを辞書内包表記で抽出する"""
    # TODO: 実装する
    pass


if __name__ == "__main__":
    prices = {"apple": 120, "banana": 80, "orange": 150}
    print(filter_expensive(prices))
