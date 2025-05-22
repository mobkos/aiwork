import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

def nothing(x):
    pass

cv2.namedWindow("YOLO Webcam")
cv2.createTrackbar("Confidence", "YOLO Webcam", 50, 100, nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (320, 240))

    conf_thresh = cv2.getTrackbarPos("Confidence", "YOLO Webcam") / 100.0

    results = model(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    df = results.pandas().xyxy[0]
    new_df = df[df['confidence'] >= conf_thresh]

    img = frame.copy()
    for _, row in new_df.iterrows():
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        label = f"{row['name']} {row['confidence']:.2f}"
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(img, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow("YOLO Webcam", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
