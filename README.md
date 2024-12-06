# AIR-NAV
A hand gesture-based mouse control system that uses mediapipe for hand detection to simulate mouse actions like clicking and scrolling. It tracks finger movements, enabling hands-free interaction with the screen in real-time.

This project uses hand gesture recognition to control the mouse and keyboard. It leverages OpenCV, MediaPipe, and Python libraries for detecting hand landmarks and controlling system actions such as mouse movement, clicks, volume control, and screen zooming.

## Features:

### 1. **Volume Control:**
- **Toggle Volume On/Off**: Raise both **Index fingers** of both hands to toggle the volume on/off.
- **Increase Volume**: Place the **Index finger and Thumb** of one hand at a certain distance to increase the volume.
- **Decrease Volume**: Reduce the gap between the **Index finger and Thumb** of one hand to decrease the volume.

### 2. **Mouse Control:**
- **Move Mouse**: Raise the **Index finger** of one hand to move the mouse pointer.
- **Left Click**: Raise both the **Index and Middle fingers** of one hand to simulate a left-click.
- **Right Click**: Raise the **Index, Middle, and Ring fingers** of one hand to simulate a right-click.

### 3. **Window Change:**
- **Switch Windows (Windows + Tab)**: Raise the **Index, Middle, Ring, and Pinky fingers** of one hand to trigger the window switch action (`Windows + Tab`).

### 4. **Pause and Resume Gesture Activities:**
- **Pause**: Open all **5 fingers** of one hand to pause all gesture activities.
- **Resume**: After the pause, show all **5 fingers** again to resume gesture activities.

### 5. **Screenshot:**
- **Take Screenshot**: Pinch the **Thumb, Index, and Middle fingers** to take a screenshot (`Windows + Print Screen`).

### 6. **Scrolling:**
- **Scroll Screen**: Pinch and move the **Index and Thumb fingers** to scroll the screen.
  
### 7. **Content Navigation (e.g., YouTube Shorts):**
- **Next Content**: Raise the **Pinky finger** to move to the next content in platforms like YouTube Shorts.
- **Previous Content**: Raise the **Ring finger** to move to the previous content.

### 8. **Zoom:**
- **Zoom In**: Raise the **Index and Middle fingers** of both hands to zoom in.
- **Zoom Out**: Raise the **Index, Middle, and Ring fingers** of both hands to zoom out.

### 9. **Stop the Program:**
- **Exit Program**: Press `q` on the keyboard or **cross both Thumb fingers** to stop the program.

## Requirements:
- Python 3.x
- Install dependencies:
  1. Create a virtual environment:
     - On Windows:
       ```bash
       python -m venv myenv
       ```
  2. Activate the virtual environment:
     - On Windows:
       ```bash
       myenv/Scripts/activate
       ```
  3. Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```

## Usage:
1. Run the **AIR-NAV-MAIN.py** to start detecting hand gestures via webcam.
2. Perform the gestures to control the mouse, volume, or trigger keyboard shortcuts.

Press 'q' or follow the gestures to exit the program.

## Libraries Used:
- OpenCV
- MediaPipe
- pynput
- keyboard
- numpy
- math

