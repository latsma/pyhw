import sqlite3
import mysql.connector
import requests
import json
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
url = "https://api.coingecko.com/api/v3/simple/price?"
print(requests.get(url).headers)
coin = input("Enter the name of your coin:")
payload = {'ids': coin, 'vs_currencies': "usd"}
status = requests.get(url,params=payload).status_code
if status >= 200 and status < 300 :
    ans = input("Successful connection. Would you like to create a file?").lower()
    print(ans)
resp = requests.get(url, params=payload)
res = json.loads(resp.text)
if ans == "yes" :
    with open('crypto.json', 'w') as f:
         json.dump(res, f, indent=4)
else:
    print("{coin} costs {x} USD".format(coin=coin, x=res[coin]['usd']))
conn = sqlite3.connect("cryptobase.sqllite3")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS crypto(
               crypto VARCHAR(50),
               price float);''')
cursor.execute('INSERT INTO crypto VALUES(?,?)',(coin, res[coin]['usd']))
conn.commit()
