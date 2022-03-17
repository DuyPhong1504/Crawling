from mysql.connector import MySQLConnection, Error
import requests
from bs4 import BeautifulSoup
 
url = "https://topdev.vn/"
 
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


def insert_job(namejob, salary, destiny,detail):
    query = "INSERT INTO topdev(id,name_job,salary,destiny,detail) " \
            "VALUES(NULL,%s,%s,%s,%s)"
    args = (namejob, salary, destiny, detail)
 
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
    insert_job(job.get("title"),salary.text,destiny.text,detail.text)