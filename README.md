# Gaole_map
這隻程式是用爬蟲將Gaole上面機台位子爬下來然後存到csv檔再匯入進goole map，我自己有匯入一分了網址在下面，需要的人可以直接點忽略下面步驟xD

**[地圖](https://www.google.com/maps/d/u/0/edit?mid=18T2qnfi810k2YQWNKnhhWzMgpyZjBBo&usp=sharing)**
---

## 1.介紹
這邊我分為兩個不同程度，擔心有人會不想下載執行檔害怕有病毒
**因為是爬蟲，所以記得要有網路!!**

- 直接下載exe檔
  - 在dist資料夾下，直接下載後執行，稍等一下在exe檔的路徑下就會出現address.csv的檔案，參考第二步驟即可匯入google map。
  - 要等大概5分鐘左右
- 複製code自己執行
  - 創一個XXX.py檔案，將code複製貼上後執行，相同路徑即會出現address.csv的檔案，參考第二步驟即可匯入google map。
  - **新增補充我的環境架設，可以參考第三點**
## 2.匯入Google map
這邊會教如何匯入剛剛的csv檔進入google map
- 進入[我的地圖](https://www.google.com/maps/d/u/0/)
- 點建立新地圖
- 左上角**匯入**
  - ![image](https://user-images.githubusercontent.com/65147485/232327568-e4016ecc-0fdd-4aac-9b3f-0ddb1a450097.png)
- 將address.csv上傳
- 選取您要放置地標的欄位:地址
- 請選擇一欄，作為標記的名稱:店名
- 完成
## 3.補充
我是用虛擬環境，所以這邊講一下如何使用
- 建立一個虛擬環境，這樣就建立一個乾淨的環境，這時候路徑會長這樣
  ```
  python -m venv gaole
  ```
  - (parent folder)
    -  gaole/
-  接下來進去之後再創建一個資料夾(gaole_code)，把Github上面通通丟進去gaole_code
-  啟動你的虛擬環境
    ```
    .\gaole\Scripts\activate.bat
    ```
- 安裝package，我都放在requirements.txt
  ```
  pip install -r .\gaole\gaole_code\requirements.txt
- 完成，這時候你就有跟我開發時候一樣的環境了，你可以隨意地玩XD