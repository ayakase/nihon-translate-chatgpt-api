


## 変更履歴 Change history

| 更新日Ngày update      | API                                                                | 変更内容 Nội dung update          |
|------------|--------------------------------------------------------------------|--------------------|
| 2022/07/21 | 新規作成                                                               |                    |
| 2022/08/01 | LINEアカウント連携作成/LineAccountCreate<br>LINEアカウント連携削除/LineAccountDelete | ベーシックIDのパラメーター名を変更 |
| 2022/08/08 | LINEアカウント連携作成/LineAccountCreate                                    | プレミアムIDのパラメーターを削除  |
| 2022/11/16 | LINEアカウント連携削除/LineAccountDelete                                    | LINEユーザーIDを任意項目に変更 |
| 2022/11/17 | LINEアカウント連携情報取得/LineAccountInfo                                    | コマンド新規追加           |

## 共通仕様 Common spec

### 用語説明 Giải thích thuật ngữ

#### Request Parameters

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ParameterName       | HTTPリクエストパラメータ 名   HTTP request paramter name                                                                                                          |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Description         | リクエストパラメータ名についての説明 Giải thích về request parameter name                                                                                                  |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Require             | リクエストパラメータ名＋値が必須で有るか （Yes:必須で有る/No:必須で無い）     Request parameter name + giá trị có bắt buộc không? (Yes: bắt buộc/No: không bắt buộc)                                                         |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Blank               | リクエストパラメータ名に対する、空白値の指定（消去）が可能か (Yes:可/No:不可)   Có thể set (xóa) giá trị blank đối với request parameter name không (Yes: Có thể/No: Không thể)                                                      |
|                     | ”Yes”の項目については、値の無いリクエストパラメータ名を指定する事によって値を消去する事が可能。 例：..&**regFax=**&otherParam=value&.. Đối với item "Yes": Có thể xóa giá trị tùy theo việc set request parameter name có giá trị không. Ví dụ: ..&**regFax=**&otherParam=value&..|
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Type                | 値のデータタイプ(String:文字列/Number:数値のみ)  Type data của giá trị (String:chuỗi kí tự/Number: Chỉ giá trị số)                                                                                      |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| MaxParams           | 同じリクエストパラメータ名の指定可能最大数   Số lượng tối đa có thể set với cùng 1 request parameter name                                                                                          |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| MaxSize             | 値に指定可能な最大文字列長 Độ dài chuỗi kí tự tối đa có thể set cho giá trị                                                                                                            |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------+

#### Response Parameters

|               |                                                                      |
|---------------|----------------------------------------------------------------------|
| ParameterName | HTTPレスポンスで返却される処理結果電文(BODY)内での、返却値識別タグ。Tag phân biệt giá trị trả về  ở trong   nội dung (body) kết quả xử lý được trả về bằng HTTP response  |
| Description   | 返却値についての説明 Giải thích về giá trị trả về                                                  |

## LINE

### LINEアカウント連携作成Tạo liên kết account LINE/LineAccountCreate

|            |                          |
|------------|--------------------------|
| actionType | LineAccountCreate         |
| 用途Cách dùng       | LINEのユーザーIDとアカウントIDの連携を作成します Tạo liên kết LINE User ID và account ID  |
| 備考 Ghi chú       | 既に連携が作成済の場合はエラーが返ります。Trường hợp đã tạo liên kết thì trả về error<br>作成済かどうかはアカウントID/LINEユーザーID/LINEベーシックIDの3つで判定されます。 Phán đoán đã tạo hay chưa bằng account ID/Line user ID/Line basic ID|

#### 特記事項 Mục chú ý

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータCommon Parameter** |                                    |         |        |            |           |         |
| loginId            | ログイン名Login name                         | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワードPassword                         | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID Account ID                      | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ Request type                  | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット Response format            | Yes     | No     | String     | 1         | 4       |
| **LINE連携 Liên kết LINE**       |                                    |         |        |            |           |         |
| lineUserId         | LINEのユーザーID  Line user ID                 | Yes     | No     | String     | 1         | 100     |
| lineBasicId        | LINE公式アカウントのベーシックID  Basic ID của account LINE chính thức   | Yes     | No     | String     | 1         | 50      |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=477302&actionType=LINEAccountCreate&responseFormat=json&lineUserId=u123456789&basicId=%40123onamae
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード Code kết quả xử lý                   |
| ResultMessage | 処理結果メッセージ Message kết quả xử lý               |
| ReceiptNo     | 受付番号 Mã tiếp nhận                         |

#### Response Sample

##### responseFormatに"json"を指定 Set json cho responseFormat

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

### LINEアカウント連携削除/LineAccountDelete  Xóa liên kết LINE account

|            |                                                                                              |
|------------|----------------------------------------------------------------------------------------------|
| actionType | LineAccountDelete                                                                            |
| 用途Cách dùng       | LINEユーザーIDの連携を削除します  Xóa liên kết của LINE user ID                                                                         |
| 備考Ghi chú       | 指定されたアカウントIDとLINE公式アカウントの紐づけを削除します Xóa ràng buộc của account ID đã set với account LINE chính thức|

#### 特記事項Mục chú ý

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータCommon parameter** |                                    |         |        |            |           |         |
| loginId            | ログイン名 Tên login                        | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワード PW                        | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID    Account ID                   | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ Request type                  | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット Response format            | Yes     | No     | String     | 1         | 4       |
| **LINE連携Liên kết LINE**       |                                    |         |        |            |           |         |
| lineUserId         | LINEのユーザーID User ID của LINE                  | No      | No     | String     | 1         | 100     |
| lineBasicId        | LINE公式アカウントのベーシックID  Basic ID của account LINE chính thức | Yes     | No     | String     | 1         | 50      |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=546804&actionType=LINEAccountDelete&responseFormat=json&basicId=%40123onamae
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード   Code kết quả xử lý                 |
| ResultMessage | 処理結果メッセージ Message kết quả xử lý               |
| ReceiptNo     | 受付番号   Mã tiếp nhận                       |

#### Response Sample

##### responseFormatに"json"を指定 Set json cho responseFormat

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

### LINEアカウント連携情報取得/LineAccountInfo   Get thông tin liên kết LINE account

|            |                                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------|
| actionType | LineAccountInfo                                                                                                    |
| 用途Cách dùng       | 対象アカウントのLINE連携情報を取得します   Get thông tin liên kết LINE của account đối tượng                                                                        |
| 備考 Ghi chú      | 指定されたアカウントのLINE連携情報を返します。   Trả về thông tin liên kết LINE của account đã được set                                                                  |

#### 特記事項Mục ghi chú

|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|

#### Request Parameters

| ParameterName      | Description                        | Require | Blank  | Type       | MaxParams | MaxSize |
|--------------------|------------------------------------|---------|--------|------------|-----------|---------|
| **共通パラメータ Common parameter** |                                    |         |        |            |           |         |
| loginId            | ログイン名  Login name                       | Yes/No  | No     | String     | 1         | 18      |
| loginPassword      | パスワード  PW                       | Yes/No  | No     | String     | 1         | 128     |
| accountId          | アカウントID  Account ID                     | Yes/No  | No     | Number     | 1         | 18      |
| actionType         | リクエストタイプ  Request type                 | Yes     | No     | String     | 1         | 50      |
| responseFormat     | レスポンスフォーマット  Response format           | Yes     | No     | String     | 1         | 4       |

#### Request Sample

```
https://test-des.onamae.com/des/ExecuteInternal.do?accountId=546804&actionType=LINEAccountInfo&responseFormat=json
```

#### Response Parameters

| ParameterName  | Description                       |
|----------------|-----------------------------------|
| ResultCode    | 処理結果コード  Code kết quả xử lý                   |
| ResultMessage | 処理結果メッセージ  Message kết quả xử lý               |
| ReceiptNo     | 受付番号   Mã tiếp nhận                        |

#### Response Sample

##### responseFormatに"json"を指定 Set "json" cho responseFormat

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
