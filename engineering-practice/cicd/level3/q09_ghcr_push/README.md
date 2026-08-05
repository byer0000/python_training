# 問題

ビルドしたDockerイメージをGitHub Container Registry（ghcr.io）にpushするワークフローを
作成してください（`GITHUB_TOKEN` を使った認証の仕組みを調べること）。

# 期待する結果

ghcr.io にイメージがpushされ、リポジトリのPackagesタブに表示される。

# ヒント

`docker/login-action`, `docker/build-push-action`
