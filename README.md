![image](https://github.com/user-attachments/assets/d2704689-04cc-4650-b95a-5f9b231ed0cc)


# SimpleUniversalGuiClicker (SUGC)
I enjoy playing clicker and idle games, but using a basic macro on my mouse as an autoclicker often feels limiting. To address this, I developed a simple GUI program using  [Dearpygui](https://github.com/hoffstadt/DearPyGui), designed to function as a versatile autoclicker for any window. SUGC (Simple Universal GUI Clicker) can simulate clicks in windows that are neither active nor focused, leveraging the win32api from the [pywin32](https://github.com/mhammond/pywin32) library.



## Limitations
- **Only Windows support:** Because of the usage of the win32api, only windows is supported.
- **Mouseposition-error:** Some windows ignore the given coordinates and try to click at the position where the physical mouse is at that moment.
 
## Features
- **Window Selection:** Select Window to click in (Window selection is inspired from [CheatEngine](https://www.cheatengine.org/))
- **Dynamic Clicks per Second:** Change Clicks per Second (CPS) on the fly without stopping the clicker
- **Mouseposition Detection:** Get Mouseposition in desired Window
- **Hotkey support:**  Define your own hotkeys to start and stop the clicker (Not all Keys might work)
## Installation - Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Skijearz/SimpleUniversalGuiClicker.git
   cd SimpleUniversalGuiClicker
    ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
    python3 -m venv venv
    venv\Scripts\activate.ps1  # for Windows
    ```

3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
   ```
4. **Start the Programm:**
   ```bash
    python main.py
   ```
