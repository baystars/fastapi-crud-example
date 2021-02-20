# contest-backend

品評会審査プログラムのバックエンド

## 設定

### ライブラリのインストール

pipで必要ライブラリをインストール

```shell
make pip
```

dockerで稼働させている場合はそのイメージにも同じライブラリをインストールする必要がある。

### 環境変数の準備

.envで定義(テスト時にしか使わない変数はtests/env.jsonで定義)

* 全般
  * `DEBUG`: デバッグモードの場合は`True`
  * `OPENAPI_URL`: プロダクション環境等openapiを使用しない場合は設定しない
  * `BACKEND_CORS_ORIGINS`=CORSの対処ドメインをカンマ区切りで設定
* データベース関連
  * `MSSQL_HOST`: SQL Serverのホスト
  * `MSSQL_DATABASE`: 同データベース名
  * `MSSQL_USER`: 同ユーザ名
  * `MSSQL_PASSWORD`: 同パスワード
  * `MSSQL_TEST_TABLE_SUFFIX`: ワークテーブル(テスト用)のテーブル名サフィックス
* テスト
  * `TEST_ENDPOINT`

注記

* .envはアプリケーション用(.env.localはfablicなどローカルでしか使わないもの)
* HEROKUやCI/CDツールを通すことを考えると環境変数で一元管理するのが望ましい
* env以下に各環境用のファイルがある

## テスト

```shell
make test
```

curlを使う場合は[Makefile](./Makefile)を参照

## その他

### SQL Serverのエラーログ

マルチバイト文字はエンコードして解読する

```python
error = b'Invalid column name ...'
print(error.encode())'
Invalid column name ...
```

## リンク

* [FastAPIを使ってCRUD APIを作成する \- Qiita](https://qiita.com/t-iguchi/items/d01b24fed05db43fd0b8)
* [Async SQL \(Relational\) Databases \- FastAPI](https://fastapi.tiangolo.com/advanced/async-sql-databases/)
