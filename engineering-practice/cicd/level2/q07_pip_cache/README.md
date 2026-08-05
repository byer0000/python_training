# 問題

CIの実行時間を短縮するために、pipの依存関係をキャッシュするステップを追加してください。

# 期待する結果

2回目以降のCI実行で、`pip install` の時間が短縮されていることをActionsのログで確認する。

# ヒント

`actions/cache@v4`、キャッシュキーに `requirements.txt` のハッシュを使う
