# 問題

`data` ディレクトリに `sample.csv` という適当な内容のCSVファイルを作成し、
所有者に実行権限は付けず、読み書き権限のみ与えてください。パーミッションを数値(例:644)で確認してください。

# 期待する結果

```
$ ls -l data/sample.csv
-rw-r--r-- 1 user user ... sample.csv
```

# ヒント

`chmod 644`, `ls -l`
