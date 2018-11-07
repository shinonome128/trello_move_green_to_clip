
"""
必要モジュールロード
"""
from trello import TrelloClient
import configparser
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
            config.read(conf_file)
         
            # パラメータの読み込み
            API_Key = config.get('API', 'API_Key')
            API_SECRET = config.get('API', 'API_SECRET')
            OAUTH_TOKEN = config.get('API', 'OAUTH_TOKEN')
            OAUTH_TOKEN_SECRET = config.get('API', 'OAUTH_TOKEN_SECRET')
            # import pdb; pdb.set_trace()

        # 失敗した時はエラーとだけ伝える
        except:
            print("Error occured")
            exit()

        # クライアントを作成
        client = TrelloClient(API_Key, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        # 全ボードをリスト
        all_boards = client.list_boards()

        # インデクシングしてボード名を変数に格納
        board = all_boards[1]

        # ボードの全カードを取得
        board.all_cards()  
        # import pdb; pdb.set_trace()
        
        # カード名を出力
        for card in board.all_cards():
            print(card.name)

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
