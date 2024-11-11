import win32gui
import win32con
import win32api
import time
import concurrent.futures
from logic.target import clicker_target
import dearpygui.dearpygui as dpg
import utils.get_icon_from_window as icons
def is_visible_window(hwnd: int)-> bool:
    return win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd)

def change_selected_window_text(title:str)->None:
    dpg.set_value("selected_window",title)

def change_selected_window_icon(hwnd: int)-> None:
    texture_data = icons.get_window_icon(hwnd)
    if texture_data is not None:
        dpg.set_value("dynamic_texture_icon",texture_data)
    else:
        dpg.set_value("dynamic_texture_icon",icons.get_default_texture())

def get_visible_windows()->list[(int,str)]:
    visible_windows = []
    def enum_windows_callback(hwnd, extra):
        if is_visible_window(hwnd):
            title = win32gui.GetWindowText(hwnd)
            visible_windows.append((hwnd, title))
    
    win32gui.EnumWindows(enum_windows_callback, None)
    return visible_windows

def capture_click()-> dict:
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) & 0x8000:
            mouse_x, mouse_y = win32api.GetCursorPos()
            hwnd = win32gui.WindowFromPoint((mouse_x, mouse_y))
            if hwnd:
                window_title = win32gui.GetWindowText(hwnd)
                in_window_mouse_pos = win32gui.ScreenToClient(hwnd,(mouse_x,mouse_y))
                return {
                    "hwnd": hwnd,
                    "window_title": window_title,
                    "mouse_pos": (mouse_x, mouse_y),
                    "relative_pos": (in_window_mouse_pos[0], in_window_mouse_pos[1])
                }
        time.sleep(0.01)


def handle_result_result(future : concurrent.futures.Future)-> None:
    result = future.result()
    if result['hwnd'] != clicker_target.target_hwnd:
       return
    dpg.set_value("x_coordinate",result["relative_pos"][0])
    dpg.set_value("y_coordinate",result["relative_pos"][1])

def bring_target_window_to_front(hwnd:int)-> None:
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

def get_mouse_in_window()-> None:
    if clicker_target.target_hwnd == 0:
        return
    bring_target_window_to_front(clicker_target.target_hwnd)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future_result = executor.submit(capture_click)
    future_result.add_done_callback(handle_result_result)