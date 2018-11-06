
"""
必要モジュールロード
"""
from trello import TrelloClient
from pprint import pprint
# コンフィグファイル読み込みのモジュール
import configparser
"""
主処理
"""
def main():

        ### 設定ファイルの読込を実行
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

        """
        #アカウントが作成したboard一覧を取得
        boards = client.list_boards()
        
        pprint(boards)
        """

        # 全ボードをリストし変数に格納
        all_boards = client.list_boards()

        # 最後のボード名を変数に格納
        last_board = all_boards[-1]

        # 最後のボードのリストを取得
        last_board.list_lists()
        import pdb; pdb.set_trace()

        # list_id の指定方法を調査
        my_list = last_board.get_list(list_id)
        
        for card in my_list.list_cards():
            print(card.name)

"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
