  
# README.md  
  
## 目的  
  
plan の効率化  
WoX から起動して trello で緑タグが付いているものだけをクリップボードにいれるスクリプト  
  
## 参照  
  
このドキュメントのコード管理  
https://github.com/shinonome128/trello_move_green_to_clip  
  
py-trello 本家  
https://github.com/sarumont/py-trello  
  
py-trello 使い方  
https://qiita.com/nozomale/items/c2c30fc2a8a89b37e921  
  
WoX 本家  
http://www.wox.one/  
  
## 使い方  
  
1. WoX 起動  
2. get_green.bat を呼び出す  
3. 緑ラベルがついたカード名がクリップボードに格納される  
  
## セットアップ  
  
1. Trello のトークン取得、 py-trello 本家取説を参照  
```  
Getting your Trello OAuth Token  
  
Make sure the following environment variables are set:  
  
    TRELLO_API_KEY  
    TRELLO_API_SECRET  
  
These are obtained from the link mentioned above.  
  
TRELLO_EXPIRATION is optional. Set it to a string such as 'never' or '1day'. Trello's default OAuth Token expiration is 30 days.  
  
Default permissions are read/write.  
  
More info on setting the expiration here: https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user  
  
Run  
  
python ./trello/util.py  
```  
  
2. conf.txt を作成、トークン、 取得したいボード名、ラベル名を入れる  
```  
[API]  
API_Key = hoge  
API_SECRET = hoge  
OAUTH_TOKEN = hoge  
OAUTH_TOKEN_SECRET = hoge  
  
[ENV]  
BOARD_NAME = hoge  
TAG_NAME = hoge  
```  
  
3. WoX 呼び出し用のバッチファイルの中身でパスを修正  
  
## ファイルの説明  
  
get_card.py  
指定したボードの、緑ラベルのカード名をクリップに移す処理  
  
conf_sample.txt  
設定ファイル  
中身を書き換えたら、conf.txt にリネーム  
  
get_green.bat  
WoX から呼び出す時にラッパー  
  
py-trello/  
Trello クライアント  
  
memo.md  
作成時のメモ書き  
  
EOF  
