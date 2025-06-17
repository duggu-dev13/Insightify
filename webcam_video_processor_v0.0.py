import cv2
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import numpy as np

# Load the model and processor
processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM2-256M-Video-Instruct")
model = AutoModelForImageTextToText.from_pretrained(
    "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    torch_dtype=torch.float32,  # Use float32 for CPU
    device_map="cpu"
)

# Initialize webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

frame_interval = 30  # Process 1 frame every 30 frames
frame_count = 0

print("🔁 Starting real-time video description... Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    frame_count += 1

    # Display the live feed
    cv2.imshow('Live Feed', frame)

    if frame_count % frame_interval == 0:
        # Convert BGR (OpenCV) to RGB (PIL)
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Prepare conversation
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": "Describe this scene briefly."}
                ]
            }
        ]

        # Preprocess inputs
        inputs = processor.apply_chat_template(
            conversation,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt"
        ).to(model.device)

        # Generate output
        output_ids = model.generate(**inputs, max_new_tokens=64)
        generated_text = processor.batch_decode(output_ids, skip_special_tokens=True)[0]

        print(f"[Frame {frame_count}] 🧠 Description: {generated_text}")

    # Stop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
