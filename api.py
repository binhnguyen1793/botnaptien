from flask import Flask, request, send_file
from flask_cors import CORS  # NEW
import subprocess
import os

app = Flask(__name__)
CORS(app)  # NEW: Cho phép gọi từ web bên ngoài

@app.route("/run-bot", methods=["POST"])
def run_bot():
    price = request.form.get("price")
    if not price:
        return "Thiếu giá trị 'price'!", 400

    print(f"💰 Nhận yêu cầu chạy bot với giá: {price}")
    result = subprocess.run(["python", "bot.py", price], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)

    image_path = os.path.join("static", "qr_code.png")
    if os.path.exists(image_path):
        response = send_file(image_path, mimetype="image/png")
        try:
            os.remove(image_path)
        except Exception as e:
            print(f"⚠️ Không thể xoá ảnh: {e}")
        return response
    else:
        return "Không tìm thấy ảnh chụp!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
