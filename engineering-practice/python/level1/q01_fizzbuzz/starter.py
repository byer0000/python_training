def fizzbuzz_loop(n: int = 30) -> list:
    """for文とif文でFizzBuzzのリストを作る"""
    # TODO: 実装する
    pass


def fizzbuzz_comprehension(n: int = 30) -> list:
    """リスト内包表記でFizzBuzzのリストを作る"""
    # TODO: 実装する
    pass


if __name__ == "__main__":
    result_loop = fizzbuzz_loop()
    result_comp = fizzbuzz_comprehension()
    print(result_loop)
    assert result_loop == result_comp, "2つの実装結果が一致しません"
