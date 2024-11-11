import dearpygui.dearpygui as dpg
import threading
from pynput.keyboard import Key,KeyCode
from pynput import keyboard
from utils.convert_pynput_to_vk import convert_from_string_to_vk_keycode
from utils.convert_from_int_to_vk import vk_code_to_key_name
import config.config as config
import win32api
import logic.clicker as clicker 
import time

is_capturing = False

def is_hotkey_already_used(key: int)-> bool:
    for hotkey in config.hotkeys:
        if config.hotkeys[hotkey] == key:
            return True

def get_thread_by_name(thread_name:str)->threading.Thread | None:
    for thread in threading.enumerate():
        if thread.name == thread_name:
            return thread
    return None

def capture_hotkey(sender : str | int)-> None:
    t = get_thread_by_name("hotkey_thread")
    if t is not None:
        if t.is_alive():
            t.do_run = False
    global is_capturing
    if is_capturing:
        dpg.configure_item(sender,enabled=True)
        return
    is_capturing = True
    def on_press(key : Key):
        global is_capturing
        if isinstance(key, KeyCode):
            hotkey = key.char 
        elif isinstance(key, Key):
            hotkey = key  
        else:
            hotkey = None
        if hotkey is not None:
            vk_code = convert_from_string_to_vk_keycode(hotkey)
            if not is_hotkey_already_used(vk_code) and vk_code is not None:
                config.hotkeys[sender] = vk_code 
                dpg.configure_item(sender,label=vk_code_to_key_name(vk_code))
        is_capturing = False
        t.do_run= True
        dpg.configure_item(sender, enabled=True)
        listener.stop()


    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def process_hotkey_pressed_thread()-> None:
    t = threading.current_thread()
    while True:
        while getattr(t,"do_run",True):
            for key in config.hotkeys:
                if win32api.GetAsyncKeyState(config.hotkeys[key]) & 0x8000:
                    if key == "hotkey_button_stop": 
                        clicker.stop_clicker()
                    elif key == "hotkey_button_start": 
                        clicker.start_clicker()
            time.sleep(0.01)
        time.sleep(0.5)


def set_hotkey(sender : int | str)-> None:
        dpg.configure_item(sender,enabled=False)
        capture_hotkey(sender)