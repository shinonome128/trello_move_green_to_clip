
"""
必要モジュールロード
"""
from trello import TrelloClient
import configparser
import codecs
import pyperclip

"""
主処理
"""
def main():

        # 設定ファイルの読込
        conf_file = 'conf.txt'
        config = configparser.ConfigParser()

        # 気持ち程度のエラー処理
        try:
            # configのファイルを開く
            config.readfp(codecs.open(conf_file, "r", "utf8"))
         
            # パラメータの読み込み
            API_Key = config.get('API', 'API_Key')
            API_SECRET = config.get('API', 'API_SECRET')
            OAUTH_TOKEN = config.get('API', 'OAUTH_TOKEN')
            OAUTH_TOKEN_SECRET = config.get('API', 'OAUTH_TOKEN_SECRET')
            BOARD_NAME = config.get('ENV', 'BOARD_NAME')
            TAG_NAME = config.get('ENV', 'TAG_NAME')

        # 失敗した時はエラーとだけ伝える
        except:
            print("Error occured")
            exit()

        # クライアントを作成
        client = TrelloClient(API_Key, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        # 緑ラベルカードの配列を呼び出し
        green_cards = get_green_cards(client, BOARD_NAME, TAG_NAME)

        # クリップボードにコピー
        copy_clipboard(green_cards)

"""
カードリストの整形・クリップボードへ格納
"""
def copy_clipboard(cards_list):

        # 空の文字列を作成
        line = ''

        # カードを取り出してループ処理
        for card in cards_list:

            # カード名と改行を格納
            line += card.name + '\n'

        # クリップボードにコピー
        pyperclip.copy(line)

        return

"""
緑ラベルカードの配列を取得
"""
def get_green_cards(client, BOARD_NAME, TAG_NAME):

        # 緑ラベルカードの空配列を作成
        green_cards = []

        # ボードリスト取得
        board_list = client.list_boards()

        # ボード名を取得してループ処理
        for board in board_list:

            # ボード名が一致するものを処理
            if board.name == BOARD_NAME:

                # リスト名を取得してループ処理
                for list in board.list_lists('open'):

                    # カード名を取得してループ処理
                    for card in list.list_cards():

                        # ラベルがついたものを処理
                        if len(card.labels) > 0:

                            # ラベル名が一致するものを処理
                            if card.labels[0].name == TAG_NAME:

                                # 緑ラベルのカードを配列に追加
                                green_cards.append(card)

        return green_cards

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
