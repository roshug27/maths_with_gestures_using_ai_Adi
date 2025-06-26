
# ✍️ Maths with Gestures using AI

A real-time hand-gesture-based math-solving application built with OpenCV, MediaPipe, Streamlit, and Google's Gemini AI. This app allows users to draw mathematical problems in the air using their fingers, then sends the drawing to Gemini to solve it and return the answer—all hands-free!

## 🚀 Features

* ✋ Real-time hand tracking and gesture detection
* 🧠 Google Gemini AI integration for math problem solving
* 🎨 Canvas drawing using only your index finger
* 🪄 Gesture-based control for clearing the canvas or submitting the problem
* 🖼️ Streamlit-based interactive GUI

## 🛠️ Technologies Used

* Python
* OpenCV
* cvzone (HandTrackingModule)
* MediaPipe
* NumPy
* Google Generative AI (Gemini)
* Streamlit
* PIL (Python Imaging Library)

## ✍️ Gesture Controls

| Gesture              | Action              |
| -------------------- | ------------------- |
| Only Index Finger Up | Draw on canvas      |
| Index + Pinky Up     | Clear canvas        |
| All Fingers Up       | Submit to Gemini AI |

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/roshug27/maths_with_gestures_using_ai_Adi.git
cd maths_with_gestures_using_ai_Adi
```

2. **Install Dependencies**

Make sure you have Python 3.9+ and install the required libraries:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install opencv-python cvzone streamlit google-generativeai numpy pillow
```

3. **Add Google Gemini API Key**

Edit the following line in the script with your API key:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

## 🧠 How It Works

1. Uses your webcam to detect your hand.
2. Tracks the position of your index finger to draw.
3. Press all 5 fingers up to send the canvas to Gemini.
4. Gemini processes the drawing and returns the solution.
5. Displays the result in the Streamlit app.

## 🏃 Run the App

```bash
streamlit run app.py
```

(Or whatever your script filename is.)

## 📌 Notes

* Works best in good lighting conditions.
* Requires an active internet connection for Gemini AI.
* The model expects reasonably clear digit/character drawings.

## 🙌 Author

**Aditya Gupta** – [@roshug27](https://github.com/roshug27)


