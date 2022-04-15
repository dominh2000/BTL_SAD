BTL_SAD
========================

Bài tập lớn môn Kiến trúc &amp; Thiết kế phần mềm

Các chức năng đã cài đặt
--------

1. Trang chủ (đang hiện ra giao diện clone, chưa sửa): http://127.0.0.1:8000/home
2. Xem chi tiết sách: http://127.0.0.1:8000/book/get/9781292096858/
3. Xem chi tiết điện thoại: http://127.0.0.1:8000/mobilephone/get/2
4. Xem chi tiết laptop: http://127.0.0.1:8000/laptop/get/1
5. Thêm sách: http://127.0.0.1:8000/book/addBook
6. Thêm điện thoại: http://127.0.0.1:8000/mobilephone/addPhone
7. Thêm laptop: http://127.0.0.1:8000/laptop/addLaptop

Đăng nhập SQLite
---------

* http://127.0.0.1:8000/admin
* Username: `dominh` 
* Password: `Hello123!`

Một số hướng dẫn
---------

* Run server: `python manage.py runserver`
* Xem sách bằng cách get mã ISBN của bảng Book:
  * Url pattern: `http://127.0.0.1:8000/book/get/<isbn>`
  * Các ISBN có sẵn: `9780128119051`,`9781118804674`,`9781119559917`,`9781292096858`
* Xem điện thoại, laptop bằng cách get ID của bảng MobilePhone, Laptop
  * Url pattern: `http://127.0.0.1:8000/mobilephone/get/<id>`, `http://127.0.0.1:8000/laptop/get/<id>`
  * Các ID có sẵn cho điện thoại: `2`,`4`,`5`
  * Các ID có sẵn cho laptop: `1`,`2`,`3`