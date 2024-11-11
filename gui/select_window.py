import dearpygui.dearpygui as dpg
import logic.windows as windows
import logic.clicker as clicker
def open_process_popup()-> None:
    all_window_handles = windows.get_visible_windows()
    pop_up_window_width = int(dpg.get_item_width("main_window")*0.95)
    pop_up_window_heigth = int(dpg.get_item_height("main_window")*0.86)

    with dpg.window(tag="popup_window",label="Select Window",no_resize=True,pos=[4,50],width=pop_up_window_width,height=pop_up_window_heigth,on_close=lambda: dpg.delete_item("popup_window"),no_title_bar=True,no_move=True):
        listbox_width = int(dpg.get_item_width("popup_window")*0.95)
        dpg.add_listbox(all_window_handles,tag="hwnd_listbox",num_items=18,width=listbox_width)
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=int(listbox_width/2)-50)
            dpg.add_button(label="Confirm",callback=clicker.change_clicker_target)
            dpg.add_button(label="Cancel" ,callback=lambda: dpg.delete_item("popup_window"))
