  
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
モジュールないよと怒られる  
  
ConfigParser のインスト  
```  
cd C:\Users\shino\AppData\Local\Programs\Python\Python36\Scripts  
pip3.6.exe install ConfigParser  
```  
```  
C:\Users\shino\AppData\Local\Programs\Python\Python36\Scripts>pip3.6.exe install ConfigParser  
Requirement already satisfied: ConfigParser in c:\users\shino\appdata\local\programs\python\python36\lib\site-packages (3.5.0)  
You are using pip version 10.0.1, however version 18.1 is available.  
You should consider upgrading via the 'python -m pip install --upgrade pip' command.  
```  
pip が古いと怒られる  
  
pip のアップグレード  
```  
cd C:\Users\shino\AppData\Local\Programs\Python\Python36  
python -m pip install --upgrade pip  
```  
  
ConfigParser のインスト  
```  
cd C:\Users\shino\AppData\Local\Programs\Python\Python36\Scripts  
pip3.6.exe install ConfigParser  
```  
```  
C:\Users\shino\AppData\Local\Programs\Python\Python36\Scripts>pip3.6.exe install ConfigParser  
Requirement already satisfied: ConfigParser in c:\users\shino\appdata\local\programs\python\python36\lib\site-packages (3.5.0)  
```  
既にあると怒られる  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
Traceback (most recent call last):  
  File "get_board.py", line 8, in <module>  
    import ConfigParser  
ModuleNotFoundError: No module named 'ConfigParser'  
```  
モジュールが無いと怒られる、状態かわらず  
  
調査結果  
In Python 3, ConfigParser has been renamed to configparser for PEP 8 compliance. It looks like the package you are installing does not support Python 3.  
モジュール名を変更  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
Traceback (most recent call last):  
  File "get_board.py", line 56, in <module>  
    main()  
  File "get_board.py", line 24, in main  
    config = ConfigParser.SafeConfigParser()  
NameError: name 'ConfigParser' is not defined  
```  
関数名も変更する必要がある  
  
関数名変更  
```  
%s/ConfigParser/configparser/gc  
```  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
Traceback (most recent call last):  
  File "get_board.py", line 56, in <module>  
    main()  
  File "get_board.py", line 24, in main  
    config = configparser.Safeconfigparser()  
AttributeError: module 'configparser' has no attribute 'Safeconfigparser'  
```  
モジュール無しと怒られる  
  
Python3 configparser モジュールの使い方が違う  
```  
import configparser  
  
cfg = configparser.ConfigParser()  
cfg.read('example.cfg')  
  
# Set the optional *raw* argument of get() to True if you wish to disable  
# interpolation in a single get operation.  
print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"  
print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"  
```  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
```  
Traceback (most recent call last):  
  File "get_board.py", line 48, in <module>  
    main()  
  File "get_board.py", line 39, in main  
    boards = client.list_boards()  
  File "C:\Users\shino\AppData\Local\Programs\Python\Python36\lib\site-packages\trello\trelloclient.py", line 87, in list_boards  
    json_obj = self.fetch_json('/members/me/boards/?filter=%s' % board_filter)  
  File "C:\Users\shino\AppData\Local\Programs\Python\Python36\lib\site-packages\trello\trelloclient.py", line 223, in fetch_json  
    raise Unauthorized("%s at %s" % (response.text, url), response)  
trello.exceptions.Unauthorized: invalid key at https://api.trello.com/1/members/me/boards/?filter=all (HTTP status: 401)  
```  
クレデンシャルがまちがっとる  
  
格納した変数値をデバッグして解析する  
格納処理後に書きを挿入  
```  
import pdb; pdb.set_trace()  
```  
デバッグ実施  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
API_Key  
API_SECRET  
OAUTH_TOKEN  
OAUTH_TOKEN_SECRET  
```  
```  
(Pdb) API_Key  
"'15798efd0f84d7a491bbc7c6303bcccb'"  
(Pdb) API_SECRET  
"'4017860a380c9f7a663f799eef583c151da66d2f47f6772044744eff855b1d03'"  
(Pdb) OAUTH_TOKEN  
"'24e41ac3532525d0bbefcc546eb0201f6e54983512586f6b0f7b0ce468b97ecd'"  
(Pdb) OAUTH_TOKEN_SECRET  
"'71dd7323e3ee99ae8e91ee6513b4d824'"  
```  
あー、シングルコーテーションが入っとる、、、削除必要  
  
コンフィグファイルの値を修正  
  
修正後のテスト  
```  
cd C:\Users\shino\doc\trello  
py get_board.py  
```  
うごいたぁー！！  
  
デバッグと不要コメントを削除  
  
## 非管理対象に加えてから Git 管理にする  

非管理対象を .gitignore に追加
```
cd C:\Users\shino\doc\trello_move_green_to_clip  
echo conf.txt>> .gitignore  
git add *
git commit -m "Add conf.txt"  
git push
```

管理対象をコピー
クレデンシャル情報が削除されていることを確認
```
cd C:\Users\shino\doc\trello  
copy get_board.py C:\Users\shino\doc\trello_move_green_to_clip\
copy py-trello C:\Users\shino\doc\trello_move_green_to_clip\
copy util.py C:\Users\shino\doc\trello_move_green_to_clip\
copy conf.txt C:\Users\shino\doc\trello_move_green_to_clip\
```
失敗、切り戻し、ディレクトをコピーしたい
```
del CHANGELOG
del CHANGELOG.md
del get_board.py
del LICENSE
del MANIFEST.in
del README.rst
del requirements.txt
del setup.py
del tox.ini
del AUTHORS.md
```

ディレクトリコピーの方法
最後のバックスラッシュは不要？
```
cd C:\Users\shino\doc\trello  
mkdir hoge
copy hoge C:\Users\shino\doc\trello_move_green_to_clip
```
```
hoge\*
指定されたファイルが見つかりません。
        0 個のファイルをコピーしました。
```
ディレクトリは copy コマンドダメ

D:\hoge ディレクトリを Z:\Backup 内にコピーする
```
xcopy hoge Z:\Backup\hoge /s/e/i
```

リトライ
```
cd C:\Users\shino\doc\trello  
copy get_board.py C:\Users\shino\doc\trello_move_green_to_clip
copy util.py C:\Users\shino\doc\trello_move_green_to_clip
copy conf.txt C:\Users\shino\doc\trello_move_green_to_clip
xcopy py-trello C:\Users\shino\doc\trello_move_green_to_clip\py-trello /s/e/i
```

管理対象ファイルをコミット、プッシュ
```
cd C:\Users\shino\doc\trello_move_green_to_clip  
git add *
git commit -m "Add first commit"  
git push
```

## 緑タグのタスクを取得 
  
## 変数に格納  
  
## 取得した情報を整形  
  
## 整形した情報をクリップボードにコピー  
  
## wox から呼び出せるようにするためにバッチファイルの作成  
  
## モバイル上でも動作するように GCP のラムダのような機能を追加  
  
## 変更管理ができるように CICD パイプライン処理を追加  
  
以上  
