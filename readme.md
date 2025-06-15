# Insightify 

**Author:** [Vaibhav Sonawane](mailto:work.vaibhav1308@gmail.com)  
**Model Used:** `SmolVLM2-500M-Video-Instruct` by HuggingFaceTB  
**Frameworks:** PyTorch, Transformers (Hugging Face) <br>
**Reference**: Xuan-Son Nguyen

**Insightify** is an experimental project that allows real-time scene understanding using a webcam and AI. It has two versions:

---

## 🧪 Version 1 – **Python-based Desktop Application**

This version uses **OpenCV**, **Hugging Face Transformers**, and **SmolVLM2** to describe the live scene from your webcam in real-time, directly in a Python environment.

### ✨ Features
- Captures live webcam feed using OpenCV
- Processes one frame every few seconds for efficiency
- Sends the frame with a natural language instruction to SmolVLM2
- Outputs real-time scene descriptions in the console
- Fully runs on CPU (no GPU required)

### 📦 Requirements

- Python 3.8+
- `transformers`, `torch`, `opencv-python`, `Pillow`, `numpy`

### 🔧 Installation

```bash
pip install transformers torch opencv-python pillow numpy
```
### ▶️ Run
```python insightify_v1.py ``` <br>
press q to quit the video feed.

## 🌐 Version 2 – Web-Based Application
This version is a browser-based interface built with HTML, CSS, and JavaScript that:

- Captures webcam feed from the browser

- Sends base64-encoded images to an OpenAI-compatible API

- Receives and displays the response inline

- Allows configuration of instruction prompts and request intervals

### 🌟 Highlights
- No installation needed, runs in any modern browser

- Customizable API endpoint, prompt, and interval

- Clean dark UI using CSS variables

- Fully client-side with no image storage (privacy-friendly)

### 📁 Usage
- Open the ```realtime_video_processing_v0.1.html``` file in your browser.

- Grant camera access.

- run following commands as per you choice:
```
(tool_name) -hf ggml-org/SmolVLM-Instruct-GGUF

(tool_name) -hf ggml-org/SmolVLM-256M-Instruct-GGUF

(tool_name) -hf ggml-org/SmolVLM-500M-Instruct-GGUF

(tool_name) -hf ggml-org/SmolVLM2-2.2B-Instruct-GGUF
```
note: you may need to add ```-ngl 99``` to enable GPU acceleration.

- Click "Start" on webpage to begin real-time scene interpretation


## 📜 License
### MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

- The Software shall be used for personal or educational purposes only.

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.