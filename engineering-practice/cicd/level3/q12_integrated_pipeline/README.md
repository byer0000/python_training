# 問題

これまでの内容を統合し、「コードをpush → Lint → テスト → Dockerイメージビルド →
レジストリにpush」という一連のCI/CDパイプラインを1つの `ci.yml` として完成させてください。
ジョブを `test` と `build-and-push` の2つに分割し、`test` が成功した場合のみ
`build-and-push` が動くように `needs:` で依存関係をつけてください。

# 期待する結果

`test` ジョブが失敗すると `build-and-push` ジョブがそもそも開始されない
（Actionsのグラフ表示で依存関係が矢印で示される）。

# ヒント

`needs: test` をジョブに追加する。
