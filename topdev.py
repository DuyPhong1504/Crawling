import requests
from bs4 import BeautifulSoup
 
url = "https://topdev.vn/"
 
# Gửi 1 request đến url phía trên và nhận lại source page của nó
r = requests.get(url)
 
print(r.status_code) # 200 là thành công
 

soup = BeautifulSoup(r.content, 'lxml')

for i in range(1,10):

    
 
    # print("============TITLE=============")
    # # Lấy thẻ tiêu đề bài báo
    # print(soup.title)
    # # Lấy nội dung tiêu đề
    # print(soup.title.text)



    print("============Name job=============")

    job = soup.select_one('#_platinum > li:nth-child('+ str(i) +') > div > a' )
    print(job.get("title"))

    print("============Salary job=============")
    salary = soup.select_one('#_platinum > li:nth-child('+ str(i) +') > div > div:nth-child(4) > div.col-12.pos_relative > p > span')
    print(salary.text)

    print("============Destiny=============")
    destiny = soup.select_one('#_platinum > li:nth-child('+ str(i) +') > div > div:nth-child(4) > div.col-8 > p')
    print(destiny.text)



    print("============Detail=============")
    detail = soup.select_one('#_platinum > li:nth-child('+ str(i) +') > div > div.row.top-benefits > div > ul > ul > li')
    print(detail.text)







 
 
