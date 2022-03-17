import requests
from bs4 import BeautifulSoup
 
url = "https://123job.vn/"
 
# Gửi 1 request đến url phía trên và nhận lại source page của nó
r = requests.get(url)
 
print(r.status_code) # 200 là thành công
 

soup = BeautifulSoup(r.content, 'lxml')


for i in range(1,10):

    print("============Name job=============")

    job = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > h2 > a' )
    print(job.get("title"))


    print("============COMPANY=============")

    company = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > a' )
    print(company.text)


    print("============DESTINY=============")

    destiny = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > div.info-loction.text-collapse' )
    print(destiny.text)


    print("============SALARY=============")

    salary = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > div.info-salary > strong' )
    print(salary.text)













 
 
