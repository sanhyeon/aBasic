# Ex12_oracle_csv.py
import  cx_Oracle as oci
import csv

def createTable():
    conn = oci.connect('scott/tiger@192.168.0.79:1521/xe')
    sql = '''
        CREATE TABLE supply
        (
            id              number  primary key,
            Supplier_Name   varchar2(50), 
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(30),
            Cost            number,
            Purchase_Date   date
        )
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)

    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@192.168.0.79:1521/xe')
    sql = '''
        INSERT INTO supply
        VALUES(seq_supply_id.NEXTVAL,:0,:1,:2,:3,:4)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, data)
    cursor.close()
    conn.commit()   # 잊지말자
    conn.close()

def viewDBTable(tableName):
    # 넘겨받은 테이블 명의 데이터 화면에 출력
    # 1. 연결객체 얻어오기 ( Connection )
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장
    sql = '''select * from ''' + tableName


    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql)
    datas = cursor.fetchall()
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()

    # print(datas)
    for row in datas:
        print(row)


if __name__ =='__main__':
    # (1) 테이블 생성
    # createDBTable()

    # (2) 입력 확인
    # imsi = ['kosmo','9999','8888',1000,'2022-12-24']
    # saveDBTable(imsi)

    # (2-1 ) Csv 파일 읽어서 db입력

    # file = open('supply.csv','r',encoding='utf-8')
    # datas = csv.reader(file)
    # # print(datas)        # <_csv.reader object at 0x0000022B13AB3520>
    # header = next(datas,None)
    # print(header)   # ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date'] 제목만 뜸
    # print('='*50)
    # for row in datas:
    #     # print(row)  # ['Samsung', '1001', '2521', '50000', '2025-01-01'] 제목 이후 값만 뜸
    #     saveDBTable(row)

    # (3) 테이블 내용 출력
    viewDBTable('supply')