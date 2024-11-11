import dearpygui.dearpygui as dpg
import threading
import win32gui
import win32api
import win32con
import time
import ast
import logic.windows as windows
from logic.target import clicker_target

should_run = False

def clicker_thread_loop() -> None:
    global should_run
    hwnd = clicker_target.target_hwnd
    mouse_position = win32api.MAKELONG(clicker_target.clicker_pos[0],clicker_target.clicker_pos[1])
    while should_run and hwnd !=0:
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, mouse_position)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, mouse_position)
        time.sleep(1 / clicker_target.cps)

def change_clicker_target()->None:
    selected_value = dpg.get_value("hwnd_listbox")
    dpg.delete_item("popup_window")
    selected_value_tuple = ast.literal_eval(selected_value)
    hwnd = selected_value_tuple[0]
    window_title = selected_value_tuple[1]

    clicker_target.change_target(hwnd)
    clicker_target.change_window_title(window_title)
    windows.change_selected_window_text(window_title)
    windows.change_selected_window_icon(hwnd)

def update_clicker_status()->None:
    if should_run:
        dpg.set_value("clicker_running_status", "True")
        dpg.configure_item("clicker_running_status", color=(0, 255, 0))  # Grün, wenn der Thread läuft
    else:
        dpg.set_value("clicker_running_status", "False")
        dpg.configure_item("clicker_running_status", color=(255, 0, 0))  # Rot, wenn der Thread gestoppt ist


def start_clicker()-> None:
    if clicker_target.target_hwnd == 0:
        return
    clicker_thread = threading.Thread(target=clicker_thread_loop)
    clicker_thread.daemon = True
    if not clicker_thread.is_alive():
        global should_run
        should_run = True
        update_clicker_status()
        clicker_thread.start()

def stop_clicker()-> None:
    global should_run
    if not should_run:
        return
    should_run = False
    update_clicker_status()

def change_clicker_speed(sender : str | int)-> None:
    new_cps = dpg.get_value(sender)
    clicker_target.change_cps(new_cps)