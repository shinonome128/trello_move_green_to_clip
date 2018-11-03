
# README.md

## 目的

plan の効率化
trello で緑タグが付いているものだけをクリップボードにいれるスクリプト

## 参照

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

## 取得した情報を整形

## 整形した情報をクリップボードにコピー

## wox から呼び出せるようにするためにバッチファイルの作成

## モバイル上でも動作するように GCP のラムダのような機能を追加

## 変更管理ができるように CICD パイプライン処理を追加

以上
