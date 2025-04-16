import time
from collections import Counter
import re
import os

class TextAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = None
    
    def read_file(self):
        """ファイルを読み込む"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
            return True
        except FileNotFoundError:
            print(f"エラー: ファイル '{self.file_path}' が見つかりません。")
            return False
        except Exception as e:
            print(f"エラー: ファイルの読み込み中にエラーが発生しました: {e}")
            return False

    def count_characters_simple(self):
        """単純な文字カウント"""
        if not self.text:
            return None
        return Counter(self.text)

    def count_characters_excluding_spaces(self):
        """空白を除外した文字カウント"""
        if not self.text:
            return None
        return Counter(char for char in self.text if not char.isspace())

    def count_japanese_characters(self):
        """日本語文字（ひらがな、カタカナ、漢字）のカウント"""
        if not self.text:
            return None
        
        # 日本語文字のパターン
        japanese_pattern = re.compile(r'[ぁ-んァ-ン一-龥]')
        japanese_chars = japanese_pattern.findall(self.text)
        return Counter(japanese_chars)

    def print_statistics(self):
        """テキストの統計情報を表示"""
        if not self.text:
            print("テキストが読み込まれていません。")
            return

        print("\n=== テキスト統計 ===")
        print(f"総文字数: {len(self.text)}")
        print(f"空白を除いた文字数: {len(''.join(self.text.split()))}")
        print(f"行数: {len(self.text.splitlines())}")
        print(f"単語数: {len(self.text.split())}")

def measure_performance(func):
    """関数の実行時間を計測するデコレータ"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}の実行時間: {(end_time - start_time)*1000:.2f}ミリ秒")
        return result
    return wrapper

@measure_performance
def analyze_text_file(file_path):
    """テキストファイルを分析"""
    analyzer = TextAnalyzer(file_path)
    
    if not analyzer.read_file():
        return

    # 基本的な統計情報を表示
    analyzer.print_statistics()

    # 文字カウントの結果を表示
    print("\n=== 文字カウント（上位10件）===")
    char_count = analyzer.count_characters_simple()
    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        if char.isspace():
            char_display = f"空白文字(\\{char})" if char in ['\n', '\t'] else "空白"
        else:
            char_display = char
        print(f"'{char_display}': {count}")

    # 日本語文字のカウント
    print("\n=== 日本語文字カウント（上位10件）===")
    jp_char_count = analyzer.count_japanese_characters()
    if jp_char_count:
        for char, count in sorted(jp_char_count.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"'{char}': {count}")

if __name__ == "__main__":
    # ファイルパスを指定して実行
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "sample.txt")
    analyze_text_file(file_path)
