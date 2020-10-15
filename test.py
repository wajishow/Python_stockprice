# coding: UTF-8
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#jsonファイルを指定
credentials = ServiceAccountCredentials.from_json_keyfile_name('stockrprice-0ca98fe01516.json', scope)

# 認証
gc = gspread.authorize(credentials)

# 読み込むスプレッドシートをファイル名で指定
target_book = gc.open('Python_stockprice')

# 読み込むシートをシート名で指定
target_sheet = target_book.worksheet('シート1')

#対象のセルに文字列を書き込み
target_sheet.update_acell('A1', 'test')
