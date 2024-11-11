import dearpygui.dearpygui as dpg
from utils.get_icon_from_window import get_default_texture
from utils.convert_from_int_to_vk import vk_code_to_key_name
import gui.gui_callbacks as gc
import gui.select_window as sw
import logic.clicker as clicker
import logic.windows as windows
import config.config as config
import logic.hotkey as hotkey

def init_window():
    dpg.create_context()
    dpg.create_viewport(title="~", width=500, height=450,decorated=False)
    with dpg.handler_registry():
        dpg.add_mouse_drag_handler(button=0, threshold=0, callback=gc.mouse_drag_callback)
        dpg.add_mouse_click_handler(button=0, callback=gc.mouse_click_callback)
    create_dynamic_textures()
    create_fonts()
    create_theme()
    create_main_window()
    dpg.setup_dearpygui()
    dpg.set_primary_window("main_window",True)
    dpg.show_viewport()
    dpg.start_dearpygui()

def create_dynamic_textures():
    dpg.add_texture_registry(tag="texture_container")
    dpg.add_dynamic_texture(32, 32, get_default_texture(),parent="texture_container", tag="dynamic_texture_icon")

def create_fonts():
    with dpg.font_registry():
        comic_font = dpg.add_font("assets/Roboto-Black.ttf", 14)
        dpg.bind_font(comic_font)

def create_theme():
    with dpg.theme() as cel_shaded_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 2, category=dpg.mvThemeCat_Core)
            dpg.bind_theme(cel_shaded_theme)

def create_main_window():
    with dpg.window(tag="main_window",label="Clicker",width=380,height=350):
        with dpg.menu_bar():
            window_width = dpg.get_viewport_width()
            dpg.add_spacer(width=window_width-85)
            dpg.add_button(label="_",callback= lambda: dpg.minimize_viewport())
            dpg.add_button(label="Close",callback=gc.close_app)
        with dpg.group(horizontal=True):
            with dpg.child_window(width=405,height=70):
                with dpg.group(horizontal=True):
                    dpg.add_text("No selected Window",tag="selected_window")
                with dpg.group(horizontal=True):
                    dpg.add_spacer(width=175)
                    dpg.add_button(label="Select Window",width=150,tag="pop_up_process",callback=sw.open_process_popup,height=30)
            with dpg.child_window(width=70,height=70,no_scrollbar=True,tag="image_window"):
                w = dpg.get_item_width("image_window")
                h = dpg.get_item_height("image_window")
                w = w/2 - 16
                h = h/2 - 16
                dpg.add_image("dynamic_texture_icon",width=32,height=32,pos=[w,h])
        dpg.add_spacer(height=10)
        with dpg.group():
            with dpg.child_window(height=75):
                dpg.add_spacer(height=15)
                with dpg.group(horizontal=True):
                    dpg.add_text("Clicks per second:")
                    dpg.add_slider_int(tag="cpsSlider",min_value=1.0,max_value=1000.0,callback=clicker.change_clicker_speed,default_value=1)
            dpg.add_spacer(height=10)
            with dpg.group():
                with dpg.child_window(height=75):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Mouse Position:")
                        dpg.add_spacer(width=90)
                        dpg.add_text("X:")
                        dpg.add_text("0", tag="x_coordinate")
                        dpg.add_spacer(width=20)
                        dpg.add_text("Y:")
                        dpg.add_text("0", tag="y_coordinate")
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=175)
                        dpg.add_button(label= "Set Clicker Position",width=150,callback=windows.get_mouse_in_window, height=30)
            dpg.add_spacer(height=10)
            with dpg.group(horizontal=True):
                with dpg.child_window(width=300):
                    dpg.add_spacer(height=10)
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=65)
                        with dpg.group():
                            dpg.add_button(label="Start Clicker",width=150,height=30,callback=clicker.start_clicker)
                            dpg.add_button(label="Stop Clicker" ,width=150,height=30,callback=clicker.stop_clicker)
                    dpg.add_spacer(height=5)
                    dpg.add_separator()
                    dpg.add_spacer(height=5)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Hotkeys:")
                        dpg.add_text("Start:")
                        dpg.add_button(label=vk_code_to_key_name(config.hotkeys["hotkey_button_start"]) if config.hotkeys["hotkey_button_start"] != 0 else "Not Set",tag="hotkey_button_start",callback=hotkey.set_hotkey,width=60,height=20)
                        dpg.add_text("Stop:")
                        dpg.add_button(label=vk_code_to_key_name(config.hotkeys["hotkey_button_stop"]) if config.hotkeys["hotkey_button_stop"] != 0 else "Not Set",tag="hotkey_button_stop",callback=hotkey.set_hotkey,width=60,height=20)

                with dpg.child_window(autosize_x=True):
                    with dpg.group(horizontal=True):
                        dpg.add_spacer(width=30)
                        dpg.add_text("Clicker Status")
                    dpg.add_separator()
                    with dpg.group(horizontal=True):
                        dpg.add_text("Running?")
                        dpg.add_text("False", tag="clicker_running_status",color=(255,0,0))
    
                    
    




