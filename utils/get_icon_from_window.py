import win32gui
import win32con
import win32ui
import win32api
from pywintypes import error as p_error
import numpy as np



def get_window_icon(hwnd: int) ->np.ndarray | None:
    hicon = win32gui.SendMessage(hwnd, win32con.WM_GETICON, win32con.ICON_BIG, 0)
    if hicon == 0:
        hicon = win32gui.SendMessage(hwnd, win32con.WM_GETICON, win32con.ICON_SMALL, 0)
    if hicon == 0:
        hicon = win32gui.GetClassLong(hwnd, win32con.GCL_HICON)
    if hicon != 0:
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(hwnd))
        width, height = win32api.GetSystemMetrics(win32con.SM_CXICON), win32api.GetSystemMetrics(win32con.SM_CYICON)
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, width, height)
        mem_dc = hdc.CreateCompatibleDC()
        mem_dc.SelectObject(hbmp)
        win32gui.DrawIconEx(mem_dc.GetSafeHdc(), 0, 0, hicon, width, height, 0, None, win32con.DI_NORMAL)
        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)
        img_bgra = np.frombuffer(bmpstr, dtype='uint8').reshape((bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4))
        img_rgba = img_bgra[:, :, [2, 1, 0, 3]]
        img_normalized_rgba = img_rgba / 255.0
        img_normalized_rgba = img_normalized_rgba.flatten()
        try:
            win32gui.DestroyIcon(hicon)
            mem_dc.DeleteDC()
            hdc.DeleteDC()
        except(p_error):
            pass
        return img_normalized_rgba
    else:
        return None 

def get_default_texture()->list:
    texture_data = []
    for i in range(32*32):
        texture_data.append(0/255)
        texture_data.append(0/255)
        texture_data.append(0/255)
        texture_data.append(0/255)
    return texture_data

