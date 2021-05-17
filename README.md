# DSAI-HW3-2021

## 操作說明
下指令"python main.py"即可
預設資料路徑為"./data/consumption.csv"  
可使用參數"--consumption"來做更改  
例:"python main.py --consumption 'Your consumption data path' --generation 'Your generation data path' --bidresult 'Your bidresult data path'"
## 方法
在清晨的時候把電都賣出去(00:00-10:00，雖然好像都沒成交，所以15:00以後也懶得賣電了，可能自己要用，可能沒電可賣，不然就是有電也賣不出去)  
在要用電的時間(10:00-15:00)買一點便宜的電來貼補
## 想法
試過在不同時間買跟賣，以及不同價錢的組合。  
也看過第一名的媒合結果，覺得他都在賤賣自己的電，怎麼會贏過我們賣高的人。  
有一個猜測是我對題目理解有誤，所有的電不管是自己產的還是買進來的，都只能在那一個小時間使用，  
而不能留到之後的時間用。如果不是這樣，而是電可以無限期儲存，那應該是賣得比台電高，買得比台電低就會賺。
