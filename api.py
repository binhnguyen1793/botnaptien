from flask import Flask, request, send_file, after_this_request
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route("/run-bot", methods=["POST"])
def run_bot():
    price = request.form.get("price", "no-price")
    print(f"💰 Nhận yêu cầu chạy bot với giá: {price}")

    # Gọi bot xử lý
    result = subprocess.run(["python", "bot.py", price], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    # Đường dẫn ảnh QR đã cắt và ảnh toàn trang
    qr_image_path = os.path.join("static", "qr_code_detected.png")
    full_image_path = os.path.join("static", "full_page.png")

    if os.path.exists(qr_image_path):
        # ✅ Sau khi gửi file QR đã cắt, xóa cả 2 ảnh
        @after_this_request
        def remove_files(response):
            for path in [qr_image_path, full_image_path]:
                try:
                    if os.path.exists(path):
                        os.remove(path)
                        print(f"🗑️ Đã xóa ảnh: {path}")
                except Exception as e:
                    print(f"❌ Lỗi khi xóa ảnh {path}:", e)
            return response

        return send_file(qr_image_path, mimetype="image/png")
    else:
        return "Không tìm thấy ảnh QR đã cắt!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
