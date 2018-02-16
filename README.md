# TrelloMemeberCount
可以透過此程式，看到 Trello 所有成員負責的卡片數量。

## 初次使用

1. 安裝並開啟虛擬環境。
   ```
   $ virtualenv venv
   $ source venv/bin/activate
   ```
   
1. 安裝所需套件。
   ```
   $ pip install -r requirements.txt
   ```
1. 編輯 `main.py` ，將金鑰 、 Token 、 看板 ID 依序填上。
1. 金鑰至 https://trello.com/app-key/ 取得。
1. Token 透過 https://trello.com/1/authorize?expiration=1day&name=MyPersonalToken&scope=read&response_type=token&key={YourAPIKey} 取得，記得要將 {YourAPIKey} 改成剛剛拿到的金鑰。
1. 看板 ID 請至看板後，在網址後方加上 reports.json ，如 https://trello.com/b/********/reports.json ，第一行即可看到 ID 。
   
## 執行程式

```
python main.py
```
