from mysql.connector import MySQLConnection, Error
import requests
from bs4 import BeautifulSoup
 
url = "https://123job.vn/"
 
# Gửi 1 request đến url phía trên và nhận lại source page của nó
r = requests.get(url)
 
print(r.status_code) # 200 là thành công
 

soup = BeautifulSoup(r.content, 'lxml')
 
# Hàm kết nối
def connect():
    """ Kết nối MySQL bằng module MySQLConnection """
    db_config = {
        'host': 'localhost',
        'database': 'crawling',
        'user': 'root',
        'password': '15042000'
    }
 
    # Biến lưu trữ kết nối
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn
 
# Test thử
conn = connect()
print(conn)


# def show_job():
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM new_table")
 
#         row = cursor.fetchone()
 
#         while row is not None:
#             print(row)
#             row = cursor.fetchone()
 
#     except Error as e:
#         print(e)
 
#     finally:
#         # Đóng kết nối
#         cursor.close()
#         conn.close()


def insert_job(namejob, company, destiny,salary):
    query = "INSERT INTO 123job(id,name_job,company,destiny,salary) " \
            "VALUES(NULL,%s,%s,%s,%s)"
    args = (namejob, company, destiny, salary)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('ID insert là:', cursor.lastrowid)
        else:
            print('Insert thất bại')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # Đóng kết nối
        cursor.close()
        conn.close()

# insert_job("IT", "123","destiny","detail")
# show_job()
for i in range(1,10):

    print("============Name job=============")

    job = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > h2 > a' )
    print(job.get("title"))
    jobstr=""+job.get("title")


    print("============COMPANY=============")

    company = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > a' )
    print(company.text)
    companystr=""+company.text


    print("============DESTINY=============")

    destiny = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > div.info-loction.text-collapse' )
    print(destiny.text)
    


    print("============SALARY=============")

    salary = soup.select_one('#carousel-feature-job > div > div:nth-child('+ str(i) +') > div > div.item-job-cpn__info > div.info-salary > strong' )
    print(salary.text)
    insert_job(job.get("title"),company.text,destiny.text,salary.text)