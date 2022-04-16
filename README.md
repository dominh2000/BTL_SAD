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

Hướng dẫn sử dụng
---------

* Run server: `python manage.py runserver`
* Xem sách bằng cách get mã ISBN của bảng Book:
  * Url pattern: `http://127.0.0.1:8000/book/get/<isbn>`
  * Các ISBN có sẵn: `9780128119051`, `9781118804674`, `9781119559917`, `9781292096858`
* Xem điện thoại, laptop bằng cách get ID của bảng MobilePhone, Laptop
  * Url pattern: `http://127.0.0.1:8000/mobilephone/get/<id>`, `http://127.0.0.1:8000/laptop/get/<id>`
  * Các ID có sẵn cho điện thoại: `2`, `4`, `5`
  * Các ID có sẵn cho laptop: `1`, `2`, `3`

Cấu trúc ứng dụng
----------

* Project `Ex2_Re` được chia thành nhiều application
* Các thư mục tương ứng với từng application có cấp độ ngang bằng với thư mục project `Ex2_Re`
* Thư mục project `Ex2_Re` gồm các thành phần:
  * `settings.py`: Cấu hình cho toàn bộ project. Một số các trường quan trọng
    * `INSTALLED_APPS`: Danh sách các application của project (tự tạo + có sẵn)
    * `DATABASES`: Chỉ định sử dụng CSDL gì (SQLite / MySQL / ...)
    * `STATICFILES_DIRS`: Chỉ định thư mục chứa các tài nguyên tĩnh (hiển thị chung cho các file HTML)
    * `AUTH_USER_MODEL`: Lớp Model dùng để xác thực việc đăng nhập vào Django admin
    * `MEDIA_ROOT` và `MEDIA_URL`: Phục vụ cho việc upload file ảnh
  * `urls.py`: Các đường dẫn ở cấp độ project - Thường là các đường dẫn dẫn đến từng application, sau đó mỗi application sẽ làm rõ ra
* Mỗi application gần tương tự 1 package của package model trong thiết kế của thầy, đảm nhiệm 1 nhóm chức năng liên quan đến 1 loại model
  * `book`: Liên quan đến sách
  * `clothes`: Liên quan đến quần áo
  * `electronics`: Liên quan đến đồ điện tử
  * `laptop`: Liên quan đến laptop
  * `mobilephone`: Liên quan đến điện thoại
  * `user`: Liên quan đến người dùng
  * `core`: Đảm nhiệm việc hiển thị 1 số giao diện chính (Homepage,...)
  * ... - Các application cần được thêm vào kế tiếp gồm: `order`, `cart`,...
* Mỗi application gồm 3 thành phần tương ứng với mô hình MVT - MVC:
  * `models.py`: Model
  * `views.py`: View trong MVT - Controller trong MVC
  * Thư mục `templates\...` cùng cấp với thư mục project: Template trong MVT - View trong MVC
    * `templates\book`: chứa các file HTML cho application `book`
    * `templates\homepage`: chứa các file HTML cho application `core`
    * ...
  * `admin.py`: register các lớp model để các lớp này hiển thị thành bảng trong giao diện Django admin
  * `urls.py`: danh sách đường dẫn gọi đến từng hàm xử lý trong `views.py`. Đường dẫn này được ghép với đường dẫn của application trong `urls.py` của project, để tạo ra 1 đường dẫn đầy đủ
  * `forms.py`: các form được chuyển thể từ các lớp model, mục đích là để viết các form nhập liệu trong HTML & xử lý chúng nhanh chóng, đỡ phải viết lắm thẻ `<input>`
  * Thư mục `migrations`: chứa các file `.py` chạy khi có thay đổi trong file `models.py`, mục đích là để ORM - tự động đồng bộ SQLite với các thay đổi trong lớp Model
* Luồng đi cơ bản của 1 request như sau:
  * Người dùng nhập URL trên thanh địa chỉ
  * `urls.py` tìm đến URL pattern tương ứng với URL người dùng nhập, gọi đến hàm xử lý tương ứng trong `views.py`
  * `views.py` thực hiện xử lý request, lấy dữ liệu từ DB,... và gọi đến thành phần template (file HTML) được chỉ định trong `return render(request, <đường dẫn file HTML>,...)`
  * File HTML được hiển thị
* Một số thư mục khác cùng cấp với project:
  * `static`: Thư mục chứa các tài nguyên tĩnh (ảnh, CSS, JS, Bootstrap,...) dùng để hiển thị HTML cho project
  * `uploads`: Chứa các file ảnh upload lên