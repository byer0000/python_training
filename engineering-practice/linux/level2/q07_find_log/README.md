# 問題

`practice` 以下に模擬のログファイル(`.log`)を複数作成し、拡張子が `.log` のファイルだけを
再帰的に検索してください。

# 期待する結果

```
$ find ~/practice -name "*.log"
/home/user/practice/logs/app.log
/home/user/practice/logs/error.log
```

# ヒント

`find . -name "*.log"`
