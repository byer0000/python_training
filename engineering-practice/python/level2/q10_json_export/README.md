# 問題

q09で作った集計結果を `summary.json` というJSONファイルに書き出してください。

# 期待する結果

`summary.json` の中身:
```json
{"りんご": 600, "バナナ": 480, "みかん": 300}
```

# ヒント

`import json`, `json.dump(data, f, ensure_ascii=False, indent=2)`
