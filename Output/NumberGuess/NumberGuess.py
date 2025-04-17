import random

def number_guessing_game():
    # 1から100までのランダムな数を生成
    target = random.randint(1, 100)
    attempts = 0
    
    print("1から100までの数字を当ててください！")
    
    while True:
        try:
            # ユーザーからの入力を受け取る
            guess = int(input("数字を入力してください: "))
            attempts += 1
            
            # 入力値のチェック
            if guess < 1 or guess > 100:
                print("1から100までの数字を入力してください")
                continue
            
            # 数字を判定
            if guess == target:
                print(f"正解です！{attempts}回目で当たりました！")
                break
            elif guess < target:
                print("もっと大きい数字です")
            else:
                print("もっと小さい数字です")
                
        except ValueError:
            print("正しい数字を入力してください")

# ゲームを開始
if __name__ == "__main__":
    number_guessing_game()
