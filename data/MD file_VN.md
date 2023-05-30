
Version 1.0.3 （2022/11/17）

## 変更履歴

| 更新日        | API                                                                | 変更内容               |
|------------|--------------------------------------------------------------------|--------------------|
| 2022/07/21 | 新規作成                                                               |                    |
| 2022/08/01 | LINEアカウント連携作成/LineAccountCreate<br>LINEアカウント連携削除/LineAccountDelete | ベーシックIDのパラメーター名を変更 |
| 2022/08/08 | LINEアカウント連携作成/LineAccountCreate                                    | プレミアムIDのパラメーターを削除  |
| 2022/11/16 | LINEアカウント連携削除/LineAccountDelete                                    | LINEユーザーIDを任意項目に変更 |
| 2022/11/17 | LINEアカウント連携情報取得/LineAccountInfo                                    | コマンド新規追加           |

## 共通仕様

### 用語説明

#### Request Parameters

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ParameterName       | HTTPリクエストパラメータ名                                                                                                             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Description         | リクエストパラメータ名についての説明                                                                                                   |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Require             | リクエストパラメータ名＋値が必須で有るか （Yes:必須で有る/No:必須で無い）                                                              |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Blank               | リクエストパラメータ名に対する、空白値の指定（消去）が可能か (Yes:可/No:不可)                                                          |
|                     | ”Yes”の項目については、値の無いリクエストパラメータ名を指定する事によって値を消去する事が可能。 例：..&**regFax=**&otherParam=value&.. |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Type                | 値のデータタイプ(String:文字列/Number:数値のみ)                                                                                        |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| MaxParams           | 同じリクエストパラメータ名の指定可能最大数                                                                                             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| MaxSize             | 値に指定可能な最大文字列長                                                                                                             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+

#### Response Parameters

|               |                                                                      |
|---------------|----------------------------------------------------------------------|
| ParameterName | HTTPレスポンスで返却される処理結果電文(BODY)内での、返却値識別タグ。     |
| Description   | 返却値についての説明                                                  |

## LINE

### LINEアカウント連携作成/LineAccountCreate

|            |                          |
|------------|--------------------------|
| actionType | LineAccountCreate         |
| 用途       | LINEのユーザーIDとアカウントIDの連携を作成します   |
| 備考       | 既に連携が作成済の場合はエラーが返ります。<br>作成済かどうかはアカウントID/LINEユーザーID/LINEベーシックIDの3つで判定されます。 |

#### 特記事項

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータ** |                                    |         |        |            |           |         |
| loginId            | ログイン名                         | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワード                         | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID                       | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ                   | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット             | Yes     | No     | String     | 1         | 4       |
| **LINE連携**       |                                    |         |        |            |           |         |
| lineUserId         | LINEのユーザーID                   | Yes     | No     | String     | 1         | 100     |
| lineBasicId        | LINE公式アカウントのベーシックID   | Yes     | No     | String     | 1         | 50      |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=477302&actionType=LINEAccountCreate&responseFormat=json&lineUserId=u123456789&basicId=%40123onamae
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード                    |
| ResultMessage | 処理結果メッセージ                |
| ReceiptNo     | 受付番号                          |

#### Response Sample

##### responseFormatに"json"を指定

```json
{"responseBean": {
  "result": {
    "actionType": "LineAccountCreate",
    "resultCode": "10000",
    "resultMsg": "Command completed successfully.",
    "receiptNo": "202207211249000849097141CE",
    "terminate": "no"
  },
  "parameters": {
    "list": [
      {
        "key": "accountId",
        "value": "477302"
      },
      {
        "key": "actionType",
        "value": "LineAccountCreate"
      },
      {
        "key": "requester",
        "value": "TestClient"
      },
      {
        "key": "responseFormat",
        "value": "json"
      },
      {
        "key": "lineUserId",
        "value": "*********"
      },
      {
        "key": "lineBasicId",
        "value": "@123onamae"
      }
    ]
  }
}}
```

### LINEアカウント連携削除/LineAccountDelete

|            |                                                                                              |
|------------|----------------------------------------------------------------------------------------------|
| actionType | LineAccountDelete                                                                            |
| 用途       | LINEユーザーIDの連携を削除します                                                                          |
| 備考       | 指定されたアカウントIDとLINE公式アカウントの紐づけを削除します |

#### 特記事項

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータ** |                                    |         |        |            |           |         |
| loginId            | ログイン名                         | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワード                         | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID                       | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ                   | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット             | Yes     | No     | String     | 1         | 4       |
| **LINE連携**       |                                    |         |        |            |           |         |
| lineUserId         | LINEのユーザーID                   | No      | No     | String     | 1         | 100     |
| lineBasicId        | LINE公式アカウントのベーシックID   | Yes     | No     | String     | 1         | 50      |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=546804&actionType=LINEAccountDelete&responseFormat=json&basicId=%40123onamae
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード                    |
| ResultMessage | 処理結果メッセージ                |
| ReceiptNo     | 受付番号                          |

#### Response Sample

##### responseFormatに"json"を指定

```json
{"responseBean": {
  "result": {
    "actionType": "LineAccountDelete",
    "resultCode": "10000",
    "resultMsg": "Command completed successfully.",
    "receiptNo": "202207211249000849097141CE",
    "terminate": "no"
  },
  "parameters": {
    "list": [
      {
        "key": "accountId",
        "value": "546804"
      },
      {
        "key": "actionType",
        "value": "LineAccountDelete"
      },
      {
        "key": "requester",
        "value": "TestClient"
      },
      {
        "key": "responseFormat",
        "value": "json"
      },
      {
        "key": "lineBasicId",
        "value": "@123onamae"
      }
    ]
  }
}}
```

### LINEアカウント連携情報取得/LineAccountInfo

|            |                                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------|
| actionType | LineAccountInfo                                                                                                    |
| 用途       | 対象アカウントのLINE連携情報を取得します                                                                           |
| 備考       | 指定されたアカウントのLINE連携情報を返します。                                                                     |

#### 特記事項

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータ** |                                    |         |        |            |           |         |
| loginId            | ログイン名                         | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワード                         | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID                       | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ                   | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット             | Yes     | No     | String     | 1         | 4       |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=546804&actionType=LINEAccountInfo&responseFormat=json
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード                     |
| ResultMessage | 処理結果メッセージ                 |
| ReceiptNo     | 受付番号                           |

#### Response Sample

##### responseFormatに"json"を指定

```json
{"responseBean": {
  "result": {
    "actionType": "LineAccountInfo",
    "resultCode": "10000",
    "resultMsg": "Command completed successfully.",
    "receiptNo": "202211171011121714187114CE",
    "terminate": "no"
  },
  "body": {
    "list": [
      "@ew4342",
      "@ewq7eha",
      "@992ywqqq"
    ]
  },
  "parameters": {
    "list": [
      {
        "key": "accountId",
        "value": "546804"
      },
      {
        "key": "actionType",
        "value": "LineAccountInfo"
      },
      {
        "key": "requester",
        "value": "TestClient"
      },
      {
        "key": "responseFormat",
        "value": "json"
      }
    ]
  }
}}
```
