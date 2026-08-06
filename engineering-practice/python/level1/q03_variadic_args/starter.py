def calc(a, b, *args, **kwargs):
    # TODO: args の合計と kwargs の中身を表示する
    print(f"args合計: {sum(args)}")
    print(f"kwargs: {kwargs}")
    pass


if __name__ == "__main__":
    calc(1, 2, 3, 4, mode="sum", verbose=True)
