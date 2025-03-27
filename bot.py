from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

# Thông tin đăng nhập
USERNAME = "kembong132"
PASSWORD = "Binh023456"

if len(sys.argv) < 2:
    print("⚠️ Lỗi: Không có số tiền truyền vào!")
    sys.exit(1)
AMOUNT = sys.argv[1]  # Lấy số tiền từ tham số dòng lệnh

# Tạo thư mục static nếu chưa có
if not os.path.exists("static"):
    os.makedirs("static")

# Khởi tạo trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Mở trình duyệt toàn màn hình
driver = webdriver.Chrome(options=options)

try:
    # Truy cập trang web
    driver.get("https://8xbet515.cc/deposit")
    wait = WebDriverWait(driver, 15)
    # Chờ trang load sau đăng nhập
    time.sleep(5)
    # Click vào nút mở form đăng nhập (có thể là "Login" hoặc "Đăng nhập")
    try:
        login_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='submit-btn']")
        ))
        login_button.click()
        print("✅ Click vào nút 'Đăng Nhập'")
    except:
        print("⚠️ Không tìm thấy nút 'Đăng Nhập'!")

    # Nhập username
    try:
        user_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        user_input.send_keys(USERNAME)
        print("✅ Nhập Username")
    except:
        print("⚠️ Không tìm thấy ô nhập Username!")

    # Nhập password
    try:
        pass_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        pass_input.send_keys(PASSWORD)
        print("✅ Nhập Password")
    except:
        print("⚠️ Không tìm thấy ô nhập Password!")

    # Click nút "Đăng Nhập"
    try:
        login_confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-btn']")))
        login_confirm_button.click()
        print("✅ Đăng nhập thành công!")
    except:
        print("⚠️ Không thể click vào nút 'Đăng Nhập'!")

    # Chờ trang load sau đăng nhập
    time.sleep(5)

    screenshot_path = "static/qr_code.png"
    driver.save_screenshot(screenshot_path)
    print("✅ Ảnh chụp toàn màn hình đã được lưu:", screenshot_path)

except Exception as e:
    print(f"⚠️ Lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
