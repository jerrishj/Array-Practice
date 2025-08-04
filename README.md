# 🧱 3D Object Sorting

This Python project demonstrates how to sort 3D objects based on their distance from the camera using the [Ursina Game Engine](https://www.ursinaengine.org/). It visually shows how render order affects transparency and occlusion, essential for real-time rendering.

<img width="1072" height="559" alt="visual" src="https://github.com/user-attachments/assets/45c7766e-c9ad-4370-9baf-9f9f54978e89" />
<img width="338" height="134" alt="sorting" src="https://github.com/user-attachments/assets/31a26d9a-9484-4285-bfe4-65ce47c8de70" />

## Getting Started

Follow these steps to set up the project in a Python virtual environment.

### 1. Create a virtual environment

```bash
python -m venv myenv
```

### 2. Activate the virtual environment

On Windows:

```
myenv\Scripts\activate
```

On macOS/Linux:

```
source myenv/bin/activate
```

### 3. Install package dependencies inside virtual environment

```
pip install ursina
```
### Files

1. game.py — Main script with camera, wall, and soldier entities.

2. soldier.glb — 3D model of soldier (replace with your own .glb if needed).
