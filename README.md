# AIR-NAV
A hand gesture-based mouse control system that uses mediapipe for hand detection to simulate mouse actions like clicking and scrolling. It tracks finger movements, enabling hands-free interaction with the screen in real-time.

This project uses hand gesture recognition to control the mouse and keyboard. It leverages OpenCV, MediaPipe, and Python libraries for detecting hand landmarks and controlling system actions such as mouse movement, clicks, volume control, and screen zooming.

## Features:
- **Mouse control**: Move and click the mouse using hand gestures.
- **Volume control**: Adjust volume with pinch gestures.
- **Keyboard shortcuts**: Use gestures to trigger actions like screen capture, volume control, and zoom.
- **Gesture detection**: Recognizes up to two hands and interprets specific gestures for actions.

## Requirements:
- Python 3.x
- Install dependencies:
  1. Create a virtual environment:
     ```bash
     
     ```
     - On Windows:
       ```bash
       python -m venv myenv
       ```
     - On Mac/Linux:
       ```bash
       python3 -m venv env
       ```
  2. Activate the virtual environment:
     - On Windows:
       ```bash
       myenv/Scripts/activate
       ```
     - On Mac/Linux:
       ```bash
       source myenv/bin/activate
       ```
  3. Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```

## Usage:
1. Run the **AIR-NAV-MAIN.py** to start detecting hand gestures via webcam.
2. Perform the gestures to control the mouse, volume, or trigger keyboard shortcuts.

Press 'q' to exit the program.

## Libraries Used:
- OpenCV
- MediaPipe
- pynput
- keyboard
- numpy
- math

