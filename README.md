# Sign Language Detection Web App

Ứng dụng này sử dụng webcam để nhận diện ký hiệu tay và hiển thị kết quả dự đoán trên giao diện web.

## Hướng dẫn cài đặt và chạy

1. **Clone repository này về máy:**

   ```bash
   git clone <link-repo>
   cd sign-language-detection
   ```

2. **Tạo môi trường ảo (khuyến nghị):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Cài đặt các thư viện cần thiết:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Đảm bảo file mô hình `best.pt` đã có trong thư mục dự án.**

5. **Chạy ứng dụng:**

   ```bash
   python app.py
   ```

6. **Mở trình duyệt và truy cập:**
   ```
   http://127.0.0.1:5000/
   ```

## Lưu ý

- Ứng dụng yêu cầu webcam hoạt động trên máy tính.
- Nếu gặp lỗi về mô hình, kiểm tra lại đường dẫn file `best.pt` trong `app.py`.

---

Link file runs (sau khi training): https://drive.google.com/drive/folders/1-IkfhouvqcwEJLXUFiBa-MseJiKA2Td-?usp=drive_link
