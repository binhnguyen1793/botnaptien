from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys
import subprocess

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

# Khởi tạo trình duyệt Chrome (chạy ở chế độ headless)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy không hiển thị giao diện
options.add_argument("--no-sandbox")  # Bắt buộc khi chạy trên server
options.add_argument("--disable-dev-shm-usage")  # Giúp giảm lỗi bộ nhớ
options.add_argument("--disable-gpu")  # Tắt GPU (không cần thiết trên server)
options.add_argument("--remote-debugging-port=9222")  # Cho phép gỡ lỗi
options.add_argument("--window-size=1920x1080")  # Định kích thước cửa sổ
options.add_argument("start-maximized")  # Giữ kích thước tối đa
options.binary_location = "/usr/bin/google-chrome"

# Khởi tạo trình duyệt
driver = webdriver.Chrome(options=options)

try:
    # Truy cập trang web
    driver.get("https://8xbet515.cc/deposit")
    wait = WebDriverWait(driver, 30)
    print(driver.current_url)  # Kiểm tra URL sau khi mở trang web

    # Chờ trang load sau đăng nhập
    time.sleep(5)

    # Click vào nút mở form đăng nhập
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

    # Xử lý pop-up "Cancel"
    try:
        cancel_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='hint-popup-guide-primary-btn' and (text()='Cancel' or text()='Hủy')]")
        ))
        cancel_button.click()
        print("✅ Click vào 'Cancel' hoặc 'Hủy'!")
    except:
        print("⚠️ Không tìm thấy nút 'Cancel' hoặc 'Hủy'!")

    # Xử lý pop-up "Later"
    try:
        later_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='hint-popup-guide-primary-btn' and (text()='Later' or text()='Lần Sau')]")
        ))
        later_button.click()
        print("✅ Click vào 'Later' hoặc 'Lần Sau'!")
    except:
        print("⚠️ Không tìm thấy nút 'Later' hoặc 'Lần Sau'!")

    # Nhập số tiền vào ô có `type="decimal"`
    try:
        amount_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='decimal']")
        ))
        amount_input.clear()
        amount_input.send_keys(AMOUNT)
        print(f"✅ Nhập số tiền: {AMOUNT} VND")
    except:
        print("⚠️ Không tìm thấy ô nhập số tiền!")

    # Click vào nút “Xác nhận nạp tiền”
    try:
        confirm_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-testid='deposit-third-party-submit-btn']")
        ))
        confirm_button.click()
        print("✅ Click 'Xác nhận nạp tiền'")
    except:
        print("⚠️ Không tìm thấy nút 'Xác nhận nạp tiền'!")

    # Chờ tab mới mở ra và chuyển sang tab mới
    time.sleep(3)
    new_tab = driver.window_handles[-1]  # Lấy tab mới nhất
    driver.switch_to.window(new_tab)
    print("✅ Đã chuyển sang tab mới chứa mã QR!")

    # Chụp ảnh toàn bộ màn hình của tab mới
    time.sleep(5)  # Chờ trang load hoàn tất
    screenshot_path = "static/qr_code.png"
    driver.save_screenshot(screenshot_path)
    print("✅ Ảnh chụp toàn màn hình đã được lưu:", screenshot_path)

except Exception as e:
    print(f"⚠️ Lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
