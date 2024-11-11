![image](https://github.com/user-attachments/assets/d2704689-04cc-4650-b95a-5f9b231ed0cc)


# SimpleUniversalGuiClicker (SUGC)
I do love playing clicker/idle games. Most of the time i use some kind of autoclicker, which is just a macro on my mouse. 
Therefore i build this simple GUI-Programm with [Dearpygui](https://github.com/hoffstadt/DearPyGui) to create a Clicker which should work in every window.
 SUGC should be able to click into windows which are not active nor focused and utilizes the win32api from [pywin32](https://github.com/mhammond/pywin32)


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
