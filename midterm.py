import os
database_file = 'library.db'
from pack.modu import *

if not os.path.exists(database_file):
    create_database(database_file)
    insert_users_from_csv(database_file, 'users.csv')
    insert_books_from_json(database_file, 'books.json')

while True:
    student_id=input("請輸入帳號：")
    if student_id !="":
        student_paw=input("請輸入密碼：")
        while login(student_id,student_paw):
            sheet()
            choice = input("選擇要執行的功能 (Enter離開): ")
            if choice == "1":
                ti = input("請輸入要新增的標題： ")
                aut = input("請輸入要新增的作者： ")
                pub = input("請輸入要新增的出版社： ")
                yea = input("請輸入要新增的年份： ")
                if newdate(ti , aut , pub, yea):
                    print("異動 1 記錄")
                    showdate()
            elif choice == "2":
                showdate()
                ti = input("請問要刪除哪一本書？：")
                ddate(ti)

            elif choice == "3":
                showdate()
                key =input("請問要修改哪一本書的標題？：")
                ti = input("請輸入要更改的標題： ")
                aut = input("請輸入要更改的作者：")
                pub = input("請輸入要更改的出版社： ")
                yea = input("請輸入要更改的年份： ")
                update_book_title(key ,ti , aut , pub, yea)
            elif choice == "4":
                keyword = input("請輸入要查詢的關鍵字：")
                search_books(keyword)
            elif choice == "5":
                showdate()
            elif choice == "":
                exit()
            else:
                print("=>無效的選擇")
    else:
        break

