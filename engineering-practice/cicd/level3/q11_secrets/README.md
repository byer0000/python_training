# 問題

Secretsを使って、APIキーやレジストリのパスワードなどの機密情報をワークフローファイルに
直接書かずに参照する方法を実装してください。

# 期待する結果

ワークフローファイル中に生の秘密情報が書かれておらず、`${{ secrets.MY_SECRET }}` の形で
参照されている。GitHubリポジトリの Settings > Secrets に値を登録しておく。

# ヒント

Settings > Secrets and variables > Actions
