# 問題

q11で作った `count_files.sh` を、どのディレクトリからでも実行できるように `PATH` に
登録してください。実行権限の付与も忘れずに。

# 期待する結果

```
$ cd /tmp
$ count_files.sh ~/practice/data
./data には 3 個のファイルがあります
```
（どのディレクトリからでもコマンド名だけで実行できる）

# ヒント

`chmod +x`, `export PATH=$PATH:...`（`.bashrc`/`.zshrc`に追記すると永続化できる）
