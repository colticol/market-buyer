# market-buyer

設定された額を成行買いするスクリプト．  
定期実行させることで，積立することができる．

## 設定

`buyer/settings.yaml`を書き換えて設定する．

- exchange
    - name : 取引所名（[ccxt](https://github.com/ccxt/ccxt/wiki/Exchange-Markets)参照）
    - api_key : APIキー
    - secret_key : 秘密キー
    - symbol : 取引通貨（[ccxt](https://github.com/ccxt/ccxt/wiki/Manual#markets)参照）
    - yen : いくら買うのか
- notify
    - line
        - token : LINEのトークン

## 使い方

cronやsystemdを使用して定期実行させる．
