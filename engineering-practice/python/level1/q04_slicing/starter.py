def slice_examples(nums: list) -> dict:
    # TODO: 3種類のスライス結果を辞書にまとめて返す
    return {
        "skip_first_two": list(nums[2:]),
        "last_two": list(nums[-2:]),
        "every_other": list(nums[::2]),
    }


if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50, 60]
    print(slice_examples(nums))
