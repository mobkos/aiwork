import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

img_path = '/home/hsb/Pictures/zoo.jpg'
image = cv2.imread(img_path)
results = model(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
df = results.pandas().xyxy[0]

def nothing(x):
    pass

cv2.namedWindow("YOLO Detection")
cv2.createTrackbar("Confidence", "YOLO Detection", 50, 100, nothing)

while True:
    conf_thresh = cv2.getTrackbarPos("Confidence", "YOLO Detection") / 100.0
    img_copy = image.copy()

    for _, row in df.iterrows():
        if row['confidence'] >= conf_thresh:
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            label = f"{row['name']} {row['confidence']:.2f}"
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img_copy, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLO Detection", img_copy)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
