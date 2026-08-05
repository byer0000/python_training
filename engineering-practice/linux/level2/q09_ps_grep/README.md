# 問題

現在実行中のプロセスの中からPythonに関連するプロセスだけを抽出してください
（Pythonを何か実行しながら試すこと）。

# 期待する結果

```
$ ps aux | grep python
user  12345  0.0  0.1  ...  python3 some_script.py
```

# ヒント

`ps aux | grep python`
