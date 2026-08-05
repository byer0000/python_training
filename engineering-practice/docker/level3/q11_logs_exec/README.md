# 問題

q09/q10の環境を起動した状態で、`docker logs` でAPIコンテナのログを確認し、
`docker exec` でコンテナの中に入ってファイル構成を確認してください。

# 期待する結果

```
$ docker logs -f <container名 or ID>
$ docker exec -it <container名 or ID> /bin/bash
root@xxxx:/app# ls
main.py  requirements.txt
```

# ヒント

`docker logs -f`, `docker exec -it <container> /bin/bash`
