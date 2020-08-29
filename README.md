# 使い方
## Dockerコマンド
#### 以下、flask-dockerディレクトリ直下にてコマンド実行

```$xslt
$ docker-compose build
```

#### 起動

```$xslt
$ docker-compose up
```

#### ログイン

```$xslt
$ docker exec -it flask-docker.api /bin/bash
$ flask run --host 0.0.0.0 --port 5000
```

## APIへのアクセス方法
- curl http://localhost:5000

