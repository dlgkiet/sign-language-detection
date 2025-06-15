from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import threading

app = Flask(__name__)
model = YOLO('best.pt')

latest_label = "Đang nhận diện..."

def generate():
    global latest_label
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model.predict(source=frame, conf=0.25, verbose=False)
        annotated_frame = results[0].plot()

        # Lấy tên nhãn nếu có
        if results[0].boxes:
            classes = results[0].boxes.cls.tolist()
            names = results[0].names
            labels = [names[int(c)] for c in classes]
            latest_label = labels[0] if labels else "Không nhận diện được"
        else:
            latest_label = "Không phát hiện"

        # Encode ảnh
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/label')
def label():
    return jsonify({'label': latest_label})

if __name__ == '__main__':
    app.run(debug=True)
