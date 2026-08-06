def filter_expensive(prices: dict, threshold: int = 100) -> dict:
    """threshold以上の商品だけを辞書内包表記で抽出する"""
    # result = {}
    # for k, v in prices.items():
    #     if v >= threshold:
    #         result[k] = v
    # return result
    return {k: v for k, v in prices.items() if v >= threshold}

if __name__ == "__main__":
    prices = {"apple": 120, "banana": 80, "orange": 150}
    print(filter_expensive(prices))
