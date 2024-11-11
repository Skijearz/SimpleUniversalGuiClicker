import gui.main_window as mw
import threading
import logic.hotkey as hotkey
import config.config as config
def main():
    hot_key_thread = threading.Thread(target=hotkey.process_hotkey_pressed_thread,name="hotkey_thread")
    hot_key_thread.start()
    mw.init_window()


if __name__ == "__main__":
    config.read_hotkeys_from_config()
    main()

