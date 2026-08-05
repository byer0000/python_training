# 問題

`push` のときはmainブランチのみ、`pull_request` のときは全ブランチでCIを走らせるように、
トリガー条件を絞り込んでください。

# 期待する結果

mainブランチ以外にpushしてもCIが実行されず、mainへのpushとどのブランチからのPRでも
CIが実行される。

# ヒント

`on: push: branches: [main]`
