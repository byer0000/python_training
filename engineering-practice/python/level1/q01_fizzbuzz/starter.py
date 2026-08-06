def fizzbuzz_loop(n: int = 30) -> list:
    """for文とif文でFizzBuzzのリストを作る"""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)

    return result

def fizzbuzz_comprehension(n: int = 30) -> list:
    """リスト内包表記でFizzBuzzのリストを作る"""
    result = [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0
        else "Fizz" if i % 3 == 0
        else "Buzz" if i % 5 == 0
        else i for i in range(1, n + 1)
    ]
    return result

if __name__ == "__main__":
    result_loop = fizzbuzz_loop()
    result_comp = fizzbuzz_comprehension()
    print(result_loop)
    assert result_loop == result_comp, "2つの実装結果が一致しません"
