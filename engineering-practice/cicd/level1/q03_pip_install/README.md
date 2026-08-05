# 問題

`../../sample_app/requirements.txt` をCI上で `pip install -r requirements.txt` する
ステップを追加してください。GitHub Actionsの実行ログで成功を確認してください。

# 期待する結果

Actionsのログで `Successfully installed pytest flake8` のような表示が出る。

# ヒント

`run: pip install -r requirements.txt`
