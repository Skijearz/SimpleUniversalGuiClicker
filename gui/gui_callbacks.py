import dearpygui.dearpygui as dpg
import os
import config.config as config

is_menu_bar_clicked = False

def mouse_click_callback() -> None:
    global is_menu_bar_clicked
    is_menu_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 40 else False
def mouse_drag_callback(_, app_data)-> None:
    if is_menu_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
        dpg.set_viewport_pos([new_pos_x, new_pos_y])

def close_app():
    config.save_hotkeys_to_config()
    os._exit(1)