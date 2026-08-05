# 問題

`.github/workflows/ci.yml` を作成してください。`main` ブランチへのpushとpull request作成を
トリガーに、単に `echo "CI started"` を実行するだけのワークフローを動かしてください。

# 期待する結果

GitHubのActionsタブでワークフローが実行され、ログに `CI started` と表示される。

# ヒント

`on: [push, pull_request]`, `jobs:`, `steps:`
