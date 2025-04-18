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

    result = subprocess.run(["python", "bot.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    image_path = os.path.join("static", "qr_code.png")

    if os.path.exists(image_path):
        # ✅ Đánh dấu sẽ xóa sau khi gửi file
        @after_this_request
        def remove_file(response):
            try:
                os.remove(image_path)
                print("🗑️ Đã xóa ảnh:", image_path)
            except Exception as e:
                print("❌ Lỗi xóa ảnh:", e)
            return response

        return send_file(image_path, mimetype="image/png")
    else:
        return "Không tìm thấy ảnh chụp!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
