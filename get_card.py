
"""
必要モジュールロード
"""
from trello import TrelloClient
import configparser
import codecs

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

                                # カード名を出力
                                print(card.name)

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
