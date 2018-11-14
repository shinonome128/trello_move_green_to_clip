  
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
  
xcopy 使い方  
http://www.palm84.com/entry/20150525/1432550334  
  
py_trello 本家  
https://github.com/sarumont/py-trello  
  
py_trello 使い方  
https://qiita.com/nozomale/items/c2c30fc2a8a89b37e921  
  
Trello API ガイド、ボード配下のカード取得する cURL と 出力  
https://developers.trello.com/reference/#boardsboardidtest  
  
py-trello 使い方、コードとテストコードがドキュメントらしい  
http://thinkami.hatenablog.com/entry/2016/03/01/003050  
  
py-trello のテストコード  
https://github.com/shinonome128/trello_move_green_to_clip/tree/master/py-trello/test  
  
py-trello の条件式の書き方  
https://qiita.com/nozomale/items/c2c30fc2a8a89b37e921  
  
Python 関数の引数の解説、デフォルト値の作り方  
http://www.isl.ne.jp/pcsp/python/python24.html#third  
  
Trello API ガイド、/lists/{id}/cards  
https://developers.trello.com/reference/#listsidcards  
  
Trello API ガイド、/lists/{id}/cards、クエリパラメータ  
https://developers.trello.com/reference#cards-nested-resource  
  
Python で出力時に q932 コーデックエラーが出る原因  
https://qiita.com/butada/items/33db39ced989c2ebf644  
  
Python で出力時に q932 コーデックエラーが出る原因、コンフィグパーサでの対応方法  
https://stackoverflow.com/questions/17813310/configparser-which-encoding-on-windows  
https://stackoverflow.com/questions/1648517/configparser-with-unicode-items  
  
配列への追加方法、append の使い方  
https://note.nkmk.me/python-list-append-extend-insert/  
  
GCF 超入門  
https://qiita.com/kai_kou/items/dca21cdfd8375a247c2f  
  
JX 通信の小笠原先生、ディプロイ先の一つとして Lambda を考える、ローカルツールをラップする設計、 CI までの考え方  
https://employment.en-japan.com/engineerhub/entry/2018/07/03/110000  
  
GCF でアクセス認証する方法、バケットにトークンを準備して、トリガー HTTP に JSON 形式で付与して認証する方法  
http://studio-andy.hatenablog.com/entry/cloud-functions-iam  
  
GCP 本家、 Cloud Functions での認証方法の実装  
https://cloud.google.com/solutions/authentication-in-http-cloud-functions?hl=ja  
  
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
  
動作確認  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_board.py  
```  
  
## カード一覧を取得  
  
取説からカード取得方法を調査  
```  
all_boards = client.list_boards()  
last_board = all_boards[-1]  
last_board.list_lists()  
my_list = last_board.get_list(list_id)  
  
for card in my_list.list_cards():  
    print(card.name)  
```  
  
get_board.py  をコピー  
get_card.py を作成  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
copy get_board.py get_card.py  
```  
  
実装  
ボード取得部分を書き換え  
認証部分はそのまま  
  
テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
  File "get_card.py", line 49, in main  
    my_list = last_board.get_list(list_id)  
NameError: name 'list_id' is not defined  
```  
list_id が定義されていない、サンプルコード見てみる  
  
list_id が定義されていない、サンプルコード見てみる  
サンプル側でも定義されていない  
  
list_id を削除  
  
リトライ  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
  File "get_card.py", line 50, in main  
    my_list = last_board.get_list()  
TypeError: get_list() missing 1 required positional argument: 'list_id'  
  
```  
最低限、1つはリスト指定する必要がある  
  
デバッグ、変数の中身を追って処理を理解  
リトライ  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
p all_boards  
p last_board  
last_board.list_lists()  
```  
```  
(Pdb) p all_boards  
[<Board ●NRICloud [ネット自動化]>, <Board すべての結果は自分の決定の結果にある>, <Board みんなのトレロ（Trello日本語コ ミュニティ)>, <Board 黒田家>]  
  
(Pdb) p last_board  
<Board 黒田家>  
  
(Pdb) last_board.list_lists()  
[<List やること>, <List 買うもの>]  
  
(Pdb)         my_list = last_board.get_list(list_id)  
NameError: name 'list_id' is not defined  
(Pdb)  
```  
  
lit_id の指定の仕方を調査  
昔ボード指定したときの方法を見てみる  
```  
	board = client.get_board("SMBCユニット")  
```  
日本語部分を引用符で囲って表示  
  
  
同じ方法で実施  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
my_list = last_board.get_list("買うもの")  
```  
```  
(Pdb) my_list = last_board.get_list("買うもの")  
trello.exceptions.ResourceUnavailable: invalid id at https://api.trello.com/1/lists/買うもの (HTTP status: 400)  
```  
だめ、リクエスト形式が正しくない  
  
ソースコード全体で list_id を検索  
わからん  
  
list_id を正しく変数化してみる  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
list_id = last_board.list_lists()  
my_list = last_board.get_list(list_id)  
```  
```  
(Pdb) list_id = last_board.list_lists()  
(Pdb) my_list = last_board.get_list(list_id)  
TypeError: must be str, not list  
```  
リスト形式ではない  
  
ソースコードから get_list() を調べてみる  
```  
 list_json = self.fetch_json('/lists/' + list_id)  
```  
わからん  
  
有効なボードで、文字列で指定してみる  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
tmp_board = all_boards[1]  
tmp_board.list_lists()  
tmp_board.get_list("Plan")  
```  
だめ  
  
py-trello の使い方を検索  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
tmp_board = all_boards[1]  
tmp_board.list_lists()  
tmp_board.all_cards()  
```  
成功、むずかしいなぁ、まだ、 GitHub 上のソースコードが読めない  
日本語解説サイトのコーディングすると早い  
  
実装  
  
テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
完成  
  
## オープンしている緑カードのフィルタ  
  
py-trello 使い方サイトから調査  
```  
・ラベル一覧の取得  
  
>>> test_board.get_labels()  
[<Label test>, <Label test4>, <Label test3>, <Label test2>, <Label test5>, <Label test6>]  
  
・ラベルのidの取得  
  
>>> test_label = test_board.get_labels()[0] # <Label test>を変数化  
>>> test_label.id  
'5aee9e93841642c2a88e7ca1'  
```  
ラベル情報の出力はあるけど、カードフィルタ方法は記載なし  
  
ソースコードから調査  
all_cards() 関数でどのようなオプションが取れるか  
```  
	def all_cards(self, custom_field_items='true'):  
		"""Returns all cards on this board  
		:rtype: list of Card  
		"""  
		filters = {  
			'filter': 'all',  
			'fields': 'all',  
			'customFieldItems': custom_field_items  
		}  
		return self.get_cards(filters)  
```  
引数 fileters を get_cards() 関数に渡している  
引数 filters の filter, fields フィールド値 all になっているので、この部分でラベルと値を指摘できればよいかも  
緑ラベルのカード名を取得するときは all_cards() ではなく、 get_cards() を使う  
  
get_card() 関数で filters 引数を指定するとき、ラベルと値を指定できるかどうか  
```  
	def get_cards(self, filters=None, card_filter=""):  
		"""  
		:filters: dict containing query parameters. Eg. {'fields': 'all'}  
		:card_filter: filters on card status ('open', 'closed', 'all')  
		More info on card queries:  
		https://trello.com/docs/api/board/index.html#get-1-boards-board-id-cards  
		:rtype: list of Card  
		"""  
		json_obj = self.client.fetch_json(  
				'/boards/' + self.id + '/cards/' + card_filter,  
				query_params=filters  
		)  
  
		return list([Card.from_json(self, json) for json in json_obj])  
```  
filters 引数 は辞書形式でクエリパラメータを記載  
Trello API ガイド参照  
  
Trello API ガイド参照  
/boards/{id}/cards部分  
cURL  
```  
https://api.trello.com/1/boards/d2EnEWSY/cards/?limit=2&fields=name&members=true&member_fields=fullName&key=[yourKey]&token=[yourToken]  
```  
fields=name  
members=true  
member_fields=fullName  
でクエリ  
  
出力  
```  
  {  
    "id": "5941465a11d2c760d95b95ad",  
    "name": "Checklists",  
    "members": []  
  },  
  {  
    "id": "5939a829eba57d109331a289",  
    "name": "Design New System",  
    "members": [  
      {  
        "id": "5589c3ea49b40cedc28cf70e",  
        "fullName": "Bentley Cook"  
      }  
    ]  
  }  
]  
```  
  
結論  
get_card() の引数 filters は出力するフィールド名を指定するものなので、緑ラベルのみフィルタはできない  
  
やりたいこと  
card.name で指定したように dict 処理部分で緑ラベルのモノだけを表示  
  
方針1  
dict 形式の変数から情報を取得するとき AND 条件ができるかどうか  
.name 指定ないときの出力を確認  
  
.name 指定ないときの出力を確認  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
<Card 16:30に痛み止飲む>  
<Card 旧場のビッグローブを3/11に解約手続き>  
<Card 洗濯物>  
```  
だめだね。  
  
ソースコードみると、 labels メソッドがのでやってみる  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
[<Label 今日やる>]  
[]  
[]  
[<Label 今日やる>]  
```  
お、取れた  
  
名前とラベルのメソッドが同時に利用できるかやってみる  
出来ないです  
  
テストコードから使い方を調べてみる  
```  
    def test51_fetch_cards(self):  
        """  
        Tests fetching all attributes for all cards  
        """  
        boards = self._trello.list_boards()  
        for b in boards:  
            for l in b.all_lists():  
                for c in l.list_cards():  
                    c.fetch()  
  
                    self.assertIsInstance(c.date_last_activity, datetime,  
                                          msg='date not provided')  
                    self.assertTrue(len(c.board_id) > 0,  
                                    msg='board id not provided')  
                break  
            break  
        pass  
```  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
出力が同じ、、、、意味なし  
テストコード全部読んだけど、効果的な使い方のサンプルなし  
  
get_cards() の使い方を GitHub から使い方と出力を確認  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
board.get_cards()  
```  
```  
[<Card 面談セットアップ レバテック>, <Card How to live before you die 12>, (省略), <Card 歯医者予約>]  
```  
カードタイトルを返すので使えない  
  
list_cards() から fetch() の出力を確認  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
card = board.get_cards()[0]  
card.fetch()  
```  
出力がない、読み込んだ後、何か手続きが必要？？  
  
GitHub 上から fetch() の使い方を調査  
よくわからない。。。  
  
py-trello 使い方サイトから fetch() の使い方を調査  
よくわからん  
  
カード読み込んで、メソッドでラベルを取得  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
card = board.get_cards()[0]  
card.labels  
```  
```  
[<Label 今日やる>]  
```  
あー、やっとできた、メソッドで指定  
  
この後実装すること  
ボードから全リストを取得  
リストからカードを取得  
カードからラベルを取得  
ラベルで緑の場合は出力  
  
サンプルコード  
```  
board_list = client.list_boards()  
for board in board_list:  
    if board.name == "Test":  
        for list in board.list_lists():  
            if list.name == "完了":  
                for card in list.list_cards():  
                    one_week_before = datetime.now(timezone.utc) - timedelta(days=7)  
                    if card.dateLastActivity < one_week_before:  
                        card.set_closed(True)  
```  
あー、やっと動いた。出力で昔のアーカイブしたカードも出力されるので、条件式を追加する  
  
## trello_green_clip アーカイブ済みカードの除外  
  
list_cards() のソースコードから調査  
```  
    def list_cards(self, card_filter="open", actions=None):  
        """Lists all cards in this list"""  
        query_params = {}  
        if card_filter:  
            query_params['filter'] = card_filter  
        if actions:  
            query_params['actions'] = actions  
        query_params['customFieldItems'] = 'true'  
        json_obj = self.client.fetch_json('/lists/' + self.id + '/cards',  
                                          query_params=query_params)  
return [Card.from_json(self, c) for c in json_obj]  
```  
card_filter="open" の引数が使えそう  
  
関数での引数に card_filter="open" を使う  
引数がある場合は card_filter にその値を入れる  
引数が無い場合は card_filter に open を入れる  
query_params に filter = xxx として、URL が組み立てられる  
  
Trello API ガイドでの filter でとれる値を調査  
/lists/ 配下、 /cards のAPIガイドより  
```  
```  
設定できるクエリより  
```  
 open - Includes cards that are open in lists that have been archived.  
 visible - Only returns cards in lists that are not closed.  
```  
visible を入れれば行けそう  
  
デバッグ  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
p list.list_cards('visible')  
p list.list_cards('open')  
p list.list_cards('')  
```  
visible は使えない、原因はわからないけど、HTTP エラコード 400 を返す  
API ガイドが古いと思われる  
そもそも、　open で問題ない  
原因は、アーカイブ済みのリストが検査されていること  
  
list_lists() 関数のソースからアーカイブ済みリストの除外方法を調査  
```  
	def list_lists(self, list_filter='all'):  
		"""Get lists from filter  
		:rtype: list of List  
		"""  
		return self.get_lists(list_filter=list_filter)  
```  
デフォルト値で list_filter = 'all' を格納  
get_lists() に all を渡している  
  
get_lists() 関数のソース調査  
```  
	def get_lists(self, list_filter):  
		"""Get lists from filter  
		:rtype: list of List  
		"""  
		# error checking  
		json_obj = self.client.fetch_json(  
				'/boards/' + self.id + '/lists',  
				query_params={'cards': 'none', 'filter': list_filter})  
		return [List.from_json(board=self, json_obj=obj) for obj in json_obj]  
```  
query_parms の filter に all を格納  
  
Trello API で/boards/ .... /lists のクエリパラメータを調査  
```  
filter  
One of all, closed, none, open  
```  
Open を使えばいいかも  
  
デバッグ  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
p board.list_lists()  
p board.list_lists('all')  
p board.list_lists('open')  
```  
いいね、 open でいける  
  
実装  
  
テスト  
  
## ボード名、リスト名、タグ名を外部設定ファイル化  
  
変数名を決める  
```  
ENV  
BOARD_NAME  
TAG_NAME  
```  
  
コンフィグファイル作成  
  
コード修正  
  
テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
Error occured  
```  
コンフィグファイルの読み込みに失敗  
フォーマットが悪い？  
  
デバッグを仕込んで変数の中身を確認  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
p BOARD_NAME  
p TAG_NAME  
```  
デバッグで止まらない、もっと前で失敗している  
  
一度コンフィグファイルを閉じて実行  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
p BOARD_NAME  
p TAG_NAME  
```  
  
ファイルを開く前にデバッグを仕込んで実行  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
config.read(conf_file)  
```  
```  
(Pdb)             config.read(conf_file)  
UnicodeDecodeError: 'cp932' codec can't decode byte 0x86 in position 313: illegal multibyte sequence  
```  
ユニコードエラー、コンフィグファイルに日本語が混じったため事象が発生した  
UTF-8 へファイルをデコードし直して保存する  
  
UTF-8 へファイルをデコードし直して保存  
Gvim のスクリプトを利用  
```  
:set encoding=utf-8  
:set fileformat=unix  
```  
  
再テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
config.read(conf_file)  
```  
```  
(Pdb)             config.read(conf_file)  
UnicodeDecodeError: 'cp932' codec can't decode byte 0x86 in position 313: illegal multibyte sequence  
```  
効果なし  
エラーメッセージを調査  
  
cp932 でエンコードするときに、解釈出来ないコードを無視する  
サンプル  
```  
>>> s.encode('cp932')  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
UnicodeEncodeError: 'cp932' codec can't encode character '\xa0' in position 0: illegal multibyte sequence  
  
>>> s.encode('cp932', "ignore")  
b''  
```  
ダメだね、コンフィグパーサでは使えない  
  
  
コンフィグパーサでファイルオープン時に UTF で読み取るようにする  
サンプル  
```  
cfg.readfp(codecs.open("myconfig", "r", "utf8"))  
```  
  
再テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
import codecs  
config.readfp(codecs.open(conf_file, "r", "utf8"))  
```  
OK、うまくいった！  
  
コード修正後、コメント、デバッグ削除の再テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
  
## config サンプルを作成  
  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
copy conf.txt conf_sample.txt  
```  
  
conf_sample.txt の値を置換  
  
ステージングとコミット  
  
## 不要ボード削除  
  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
del get_board.py  
git add get_board.py  
git commit -m "Delete get_board.py"  
git push  
```  
  
## サンプルコンフィグに例を入れる  
  
sample_conf.txt に凡例を入れる  
行けてないのでやめ  
  
## 整形した情報をクリップボードにコピー  
  
vmlogin のコード部分からサンプル部分を抽出  
```  
import pyperclip  
pyperclip.copy(get_otp(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES, PIN))  
```  
  
デバッグ実装とテスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
```  
ビッグデータの正体  
```  
あー、だめだ、配列に入れたほうがコピーのとき配列に入れる  
  
配列に入れる方法を調査  
ログインスクリプトのライン処理を流用  
```  
    # 変数 pin の空の配列を作成  
    pin = []  
  
    # 変数 pin に文字列 PIN から一文字ずつスライシングして配列を作成  
    for i in range(len(PIN)):  
        # import pdb; pdb.set_trace()  
        pin += PIN[i]  
```  
  
デバッグ実装とテスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
+= 演算子使うと、一文字ずつ配列に格納されるので、 append を使う  
  
配列を整形してクリップボードに入れる  
  
ついでに処理まいに関数化  
  
テスト  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
py get_card.py  
```  
OK  
  
デバッグ削除とコメント整理  
  
## wox から呼び出せるようにするためにバッチファイルの作成  
  
vmlogin から、バッチファイルを流用  
```  
cd C:\Users\shino\doc\trello_move_green_to_clip  
copy C:\Users\shino\doc\autologin\otp.bat get_green.bat  
```  
  
バッチファイルの中身を修正  
  
テスト  
WOX から起動して緑ラベルカードがクリップボードに入ること  
OK!  
  
## python の実行環境を GCP に移動する  
  
コードだけを登録してクラウド上で実行、結果を返す、ローカルのコンピュートリソースを使わない方法  
  
サーバレス実装方法調査  
AWS Lambda の GCP バージョンを探す  
  
大まかなやり方  
Google Cloud Functionsを使う  
GCP コンソールから関数とトリガー HTTP を設定  
gcloud ツールならディプロイまでやってくれる  
トリガー となる URL にアクセスすると実行結果を受け取る  
  
GCF サンプル実行  
```  
gcf-demo プロジェクト作成  
Cloud Functionsの[関数を作成]  
[ランタイム]プルダウンメニューをみると[Python 3.7]が選べます！  
今回はトリガーを[HTTP]でサンプルそのままで関数を作成してみます。  
関数作成中。Stackdriver Loggingでログも確認できます。  
CurlでGETしてみた。  
```  
  
関数の削除  
手動でCloud Functionsの[関数を削除]  
  
セキュリティどうするんだろ  
アクセストークンで認証するらしい  
```  
Cloud Storage Bucketを作成し、承認を行うプロキシとして利用する  
Bucketの作成  
Access Tokenの取得  
Cloud Functionsを拡張する  
Access Tokenを付与してリクエスト  
```  
  
FIrebase の認証機能を使う  
うーん、めんどくさそう、別に Web アプリを作りたいわけではなく、安全にコード実行リソースをクラウドに移したいだけなので  
  
本番コードの移行  
Git から持ってきたコードとかどうすればいいんだろう、zip のアップロードができそう、だめ  
クリップボードに送れない場合はブラウザ出力で良い、これはできる  
serverless framework を使ってみる  
  
以上  
