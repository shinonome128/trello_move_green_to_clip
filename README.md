  
# README.md  
  
## 目的  
  
plan の効率化  
trello で緑タグが付いているものだけをクリップボードにいれるスクリプト  
  
## 参照  
  
このドキュメントのコード管理  
https://github.com/shinonome128/trello_move_green_to_clip  
  
Trello クライアントのローカル管理ディレクトリ  
C:\Users\shino\doc\trello  
  
ConfigParser の使い方、サンプルコード  
http://zacodesign.net/blog/?p=3336  
  
## やること  
  
レポジトリの作成  
Trello クライアントから緑タグだけ情報を取得  
取得した情報を整形  
整形した情報をクリップボードにコピー  
wox から呼び出せるようにするためにバッチファイルの作成  
モバイル上でも動作するように GCP のラムダのような機能を追加  
変更管理ができるように CICD パイプライン処理を追加  
  
## レポジトリの作成  
  
レポジトリ名  
```  
trello_move_green_to_clip  
```  
  
ディレクトリ  
```  
mkdir C:\Users\shino\doc\trello_move_green_to_clip  
```  
  
README 作成  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
echo # hoge>> README.md  
```  
内容をコピー  
  
.gitignore 作成  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
echo # .gitignore>> .gitignore  
echo *.swp>> .gitignore  
```  
  
github に登録  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
git init  
git config --local user.email shinonome128@gmail.com  
git config --local user.name "shinonome128"  
git add .gitignore  
git add README.md  
git commit -m "first commit"  
git remote add origin https://github.com/shinonome128/trello_move_green_to_clip.git  
git push -u origin master  
```  
  
## Trello クライアントから緑タグだけ情報を取得  
  
方針  
Trello クライアントの実装調査  
緑タグのタスクを取得  
変数に格納  
  
## Trello クライアントの実装調査  
  
あらー、全部ローカルに置いてあるみたい、 Git で管理してない  
  
管理ディレクトリ  
```  
C:\Users\shino\doc\trello  
```  
  
各ファイル  
```  
2018/05/27  04:16               823 get_board.py  
2018/05/27  03:56    <DIR>          py-trello  
2018/05/27  02:34             4,187 util.py  
```  
  
方針  
各モジュールを動かしてみる  
各モジュールの中身を見て説明文を作る  
  
get_board.py  
ボード名の取得  
動作例  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
  
出力  
```  
C:\Users\shino\doc\trello>py get_board.py  
[<Board test>,  
 <Board すべての結果は自分の決定の結果にある>,  
```  
OAUTH のクレデンシャルがべたうちなのでGit 管理できない  
先にこの問題を解決しないと開発ができない  
  
py-trello  
Trello クライアント  
  
util.py  
Trello クライアント初期セットアップ  
  
方針  
ローカル管理ディレクトリでクレデンシャルの外部ファイル化  
非管理対象に加えてから Git 管理にする  
Git 管理対象  
```  
2018/05/27  04:16               823 get_board.py  
2018/05/27  03:56    <DIR>          py-trello  
2018/05/27  02:34             4,187 util.py  
```  
  
  
## ローカル管理ディレクトリでクレデンシャルの外部ファイル化  
  
やること  
Json ファイルから読み込む方法を調査  
ファイルバックアップ  
外部クレデンシャルファイル作成  
実装  
テスト  
  
  
## Json ファイルから読み込む方法を調査  
  
Json 形式でない、 テキスト形式の方が簡単そう  
ConfigParser を使う  
  
## ファイルバックアップ  
  
```  
cd C:\Users\shino\doc\trello  
copy get_board.py get_board.py_bk  
```  
  
## 外部クレデンシャルファイル作成  
  
ファイル作成  
```  
cd C:\Users\shino\doc\trello  
echo hoge>> conf.txt  
```  
  
設定ファイルサンプル  
```  
[human]  
age = 20  
name = "Taro"  
lang = "Japanese"  
```  
  
中身を開いて API キー部分の変数を記載して保存  
  
## 実装  
  
get_board.py  を編集  
コンフィグファイル名は直接埋め込む  
  
## テスト  
  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
C:\Users\shino\doc\trello>py get_board.py  
  File "get_board.py", line 39  
    print "Error occured"  
                        ^  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(print "Error occured")?  
```  
あー、だめ、 2系の 構文だった  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
C:\Users\shino\doc\trello>py get_board.py  
  File "get_board.py", line 44  
    client = TrelloClient(API_Key, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)  
                                                                              ^  
TabError: inconsistent use of tabs and spaces in indentation  
```  
インデントにタブとスペースが混じってる。。  
  
変換コマン実行してスペースにする  
```  
%s/\t/        /gc | noh  
```  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
C:\Users\shino\doc\trello>py get_board.py  
Traceback (most recent call last):  
  File "get_board.py", line 8, in <module>  
    import ConfigParser  
ModuleNotFoundError: No module named 'ConfigParser'  
```  
pip コマンドでモジュール入れる  
  
ここから再開  
  
## 非管理対象に加えてから Git 管理にする  
  
## 緑タグのタスクを取得  
  
## 変数に格納  
  
## 取得した情報を整形  
  
## 整形した情報をクリップボードにコピー  
  
## wox から呼び出せるようにするためにバッチファイルの作成  
  
## モバイル上でも動作するように GCP のラムダのような機能を追加  
  
## 変更管理ができるように CICD パイプライン処理を追加  
  
以上  
