import win32api
import ctypes

def vk_code_to_key_name(vk_code: int) -> str:
    scan_code = win32api.MapVirtualKey(vk_code, 0)
    lParam = (scan_code << 16)
    buffer = ctypes.create_unicode_buffer(32)

    ctypes.windll.user32.GetKeyNameTextW(lParam, buffer, 32)

    return buffer.value


