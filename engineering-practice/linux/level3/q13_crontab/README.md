# 問題

cronの書式を調べ、「毎日午前6時にPythonスクリプト `daily_report.py` を実行する」設定を
crontabの記法で書いてください（実際に登録する必要はありません）。

# 期待する結果

```
0 6 * * * /usr/bin/python3 /home/user/scripts/daily_report.py
```

# ヒント

`crontab -e`, `分 時 日 月 曜日 コマンド`
