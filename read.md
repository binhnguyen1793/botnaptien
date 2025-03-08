
1.1. Cập Nhật Hệ Thống
sudo apt update && sudo apt upgrade -y

1.2. Cài Đặt Python và pip
sudo apt install python3 python3-pip -y

1.3. Cài Đặt Google Chrome & ChromeDriver
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y

CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+')
wget https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
sudo chmod +x /usr/bin/chromedriver

1.4. Cài Đặt Selenium
pip3 install selenium

2.1. Tạo Thư Mục Chứa Script
mkdir selenium_script && cd selenium_script

2.2. Tạo File a.py
Sử dụng nano a.py để tạo file và dán code vào.

2.3. Chạy Script với Tham Số
python3 a.py 100000  # Thay số 100000 bằng số tiền cần nạp
