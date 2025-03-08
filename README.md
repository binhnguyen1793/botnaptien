# Game Platform Project

## 📌 Hướng dẫn cài đặt và chạy

### 1️⃣ **Cài đặt Backend (Flask)**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # (Windows dùng: venv\Scripts\activate)
pip install -r requirements.txt
python app.py
```
📌 **Backend chạy tại:** `http://127.0.0.1:5000/`

---

### 2️⃣ **Chạy Frontend (HTML, CSS, JS)**
Chỉ cần mở file `index.html` trong trình duyệt.

📌 **Trang chủ:** `index.html`
📌 **Trang tài khoản:** `account.html`
📌 **Trang game:** `game.html`

---

### 3️⃣ **Cấu trúc thư mục**
```
project/
├── backend/  # Flask API
│   ├── app.py  # Xử lý tài khoản, số dư, nạp tiền, game
│   ├── database.db  # SQLite database
│   ├── requirements.txt  # Thư viện Python cần cài đặt
│   ├── static/  # Chứa CSS, JS, Images
│   ├── templates/  # HTML giao diện Flask
│   ├── config.py  # Cấu hình API Binance
│   ├── utils.py  # Hàm hỗ trợ backend
│   ├── run.sh  # Script chạy nhanh
│
├── frontend/  # Giao diện HTML, CSS, JS
│   ├── index.html  # Trang chủ
│   ├── account.html  # Trang tài khoản
│   ├── game.html  # Trang chơi game
│   ├── login.html  # Đăng nhập
│   ├── register.html  # Đăng ký
│   ├── css/  # File CSS giao diện
│   ├── js/  # File JS xử lý
│   ├── images/  # Hình ảnh giao diện
```

✅ **Bạn chỉ cần làm theo hướng dẫn là có thể chạy ngay!** 🚀
