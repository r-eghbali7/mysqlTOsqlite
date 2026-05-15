from mysql_to_sqlite3 import MySQLtoSQLite

def convert_database():
    converter = MySQLtoSQLite(
        sqlite_file="output_database.sqlite3", # نام فایل خروجی SQLite
        mysql_user="root",                     # نام کاربری دیتابیس MySQL
        mysql_password="123456",        # رمز عبور دیتابیس MySQL
        mysql_database="qqq",   # نام دیتابیس MySQL
        mysql_host="127.0.0.1",                # آدرس هاست
        mysql_port=3306                        # پورت (معمولا 3306)
    )
    
    # اجرای عملیات انتقال
    converter.transfer()
    print("انتقال با موفقیت انجام شد!")

if __name__ == "__main__":
    convert_database()



        # 'NAME': 'yhvwlzia_AR_aidaBD',
        # 'USER': 'yhvwlzia_AR_Aida_gold',
        # 'PASSWORD': r'\Ql|6J@Tu.n"GfU[',