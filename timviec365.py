import requests
from bs4 import BeautifulSoup
 
url = "https://www.vietnamworks.com/"
 
# Gửi 1 request đến url phía trên và nhận lại source page của nó
r = requests.get(url)
 
print(r.status_code) # 200 là thành công
 

soup = BeautifulSoup(r.content, 'lxml')




print("============Name job=============")

job = soup.select_one('#pageContentWrapper > section:nth-child(6)' )
print(job.get('id'))
















 
 
