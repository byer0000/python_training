# engineering-practice

Python / Linux / Docker / CI-CD の演習問題リポジトリです。
問題ごとにフォルダを分けているので、1問終わるごとに `git add` → `git commit` してコミット履歴として
学習の進捗を残せます。

## 使い方

```bash
cd engineering-practice
git init
git add .
git commit -m "init: 演習問題の雛形を追加"
```

1問解いたら、そのフォルダの中のスターターファイルを編集し、コミットしてください。

```bash
git add python/level1/q01_fizzbuzz
git commit -m "solve: python level1 q01 fizzbuzz"
```

## ディレクトリ構成

- `python/level1〜3/`
- `linux/level1〜3/`
- `docker/level1〜3/`
- `cicd/level1〜3/`

各問題フォルダには `README.md`（問題文・期待する結果・ヒント）と、必要な場合はスターターファイル／サンプルデータが入っています。
