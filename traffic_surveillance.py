from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "traffic.avi"

cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

out = cv2.VideoWriter(
    "traffic_final.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

vehicle_classes = ["car", "bus", "truck", "motorcycle"]

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    count = 0

    for box in results[0].boxes:
        cls = int(box.cls)
        label = model.names[cls]

        if label in vehicle_classes:
            count += 1

    output = results[0].plot()

    if count > 20:
        status = "Heavy Traffic"
    elif count > 10:
        status = "Medium Traffic"
    else:
        status = "Low Traffic"

    cv2.putText(
        output,
        f"Vehicle Count: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        f"Status: {status}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    out.write(output)

cap.release()
out.release()

print("Traffic surveillance completed!")
print("Output saved as traffic_final.mp4")
