from googlesearch import search
from time import strftime

pause_num = 2.0
query = input("請輸入想要搜尋的關鍵字或是網域: ")
stop_num = int(input("請輸入最多搜尋數量: "))
pause_num = float(input("請輸入暫停時間: "))

log_date = strftime('%Y_%m_%d-%H_%M_%S')  # 提取時間
path = 'log/output-' + log_date +'.txt'
f = open(path, 'w')

print("\n相關網址:")
for web_url in search(query, stop=stop_num, pause=pause_num):
    print(web_url)
    f.write(web_url)
    f.write('\n')
f.close()
print("\n搜尋完畢! 資料在 " + 'log/output-' + log_date +'.txt')