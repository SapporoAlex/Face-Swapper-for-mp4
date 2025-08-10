import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
import os

# ---- SETTINGS ----
SOURCE_IMAGE = "source.jpg"
INPUT_VIDEO = "input_video.mp4"
OUTPUT_VIDEO = "output_swapped.mp4"
SWAP_MODEL_PATH = "inswapper_128.onnx"  # Must be in the same directory

# ---- INIT FACE DETECTOR ----
print("[INFO] Loading face analysis model (buffalo_l)...")
app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# ---- LOAD FACE SWAPPER ----
print(f"[INFO] Loading face swap model from: {SWAP_MODEL_PATH}")
swapper = insightface.model_zoo.get_model(SWAP_MODEL_PATH, providers=['CPUExecutionProvider'])

# ---- LOAD SOURCE IMAGE ----
print("[INFO] Loading source image...")
source_img = cv2.imread(SOURCE_IMAGE)
if source_img is None:
    raise FileNotFoundError(f"Source image '{SOURCE_IMAGE}' not found.")

source_faces = app.get(source_img)
if len(source_faces) == 0:
    raise Exception("No face detected in the source image.")
source_face = source_faces[0]
print("[INFO] Source face detected.")

# ---- OPEN VIDEO ----
cap = cv2.VideoCapture(INPUT_VIDEO)
if not cap.isOpened():
    raise FileNotFoundError(f"Could not open input video: {INPUT_VIDEO}")

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"[INFO] Processing video: {INPUT_VIDEO}")
print(f"[INFO] Resolution: {width}x{height}, FPS: {fps}, Total frames: {frame_count}")

# ---- OUTPUT VIDEO WRITER ----
out = cv2.VideoWriter(OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

frame_idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_idx += 1

    # Detect faces in the frame
    faces = app.get(frame)
    for face in faces:
        try:
            # Apply the face swapper
            frame = swapper.get(frame, face, source_face, paste_back=True)
        except Exception as e:
            print(f"[WARN] Swap failed on frame {frame_idx}: {e}")

    out.write(frame)
    print(f"[INFO] Processed frame {frame_idx}/{frame_count}", end='\r')

# ---- CLEANUP ----
cap.release()
out.release()
print(f"\n[INFO] Done. Output saved to: {OUTPUT_VIDEO}")
