# Face Swapper (CPU Version)

This project swaps a face from a **source image** into every frame of a given **input video** using [InsightFace](https://github.com/deepinsight/insightface).  
It runs **on CPU** for compatibility, but this means processing can take a while.

[![Watch the video](https://img.youtube.com/vi/aHa2Z-V2PAU/2.jpg)]([https://youtu.be/VIDEO_ID](https://youtu.be/aHa2Z-V2PAU))

---

## 📂 Files in this repo

- `f.py` — main Python script to perform the face swap.
- `run.sh` — shell script to activate the virtual environment and run `f.py`.

## Other files you need to get
-<a href="https://huggingface.co/ezioruan/inswapper_128.onnx/tree/main"> `inswapper_128.onnx`</a> — face swap model (must be downloaded separately).
- `source.jpg` — the face you want to use.
- `input_video.mp4` — the video whose faces you want to replace.

## File you create
- `output_swapped.mp4` — output video with swapped faces (generated after running).

---

## ⚙️ Requirements

- Python **3.8+**
- `venv` (built-in with Python)
- Dependencies listed below

---

## 📦 Installation & Setup

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/faceswapper.git
   cd faceswapper

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install opencv-python numpy insightface onnxruntime
```

Download <a href="https://huggingface.co/ezioruan/inswapper_128.onnx/tree/main"> inswapper_128.onnx</a>
Place it in the same directory as f.py.

### Add your source image and video

Place a face image named source.jpg in the same folder.

Place your video named input_video.mp4 in the same folder.

## ▶️ Running the script
You can run it in two ways:

Option 1 — Run directly:

```bash
source/activate
python f.py
```
Option 2 — Using run.sh (Linux/macOS):

```bash
chmod +x run.sh
./run.sh
```

This will:

Activate your virtual environment

Run f.py

## 🖼️ Output
After running, you’ll get:

output_swapped.mp4
This will be your original video but with the detected faces replaced by the one in source.jpg.

## ⏳ Notes
This script uses CPUExecutionProvider, so processing may be slow (especially on long videos).

Make sure your source image has a clear, front-facing face for best results.

If no face is detected in the source image, the script will stop with an error.
