from pynput.keyboard import Key

pynput_to_win32_keycodes = {
    Key.esc: 0x1B,
    Key.enter: 0x0D,
    Key.tab: 0x09,
    Key.space: 0x20,
    Key.backspace: 0x08,
    Key.shift: 0x10,
    Key.shift_r: 0xA1,
    Key.ctrl: 0x11,
    Key.ctrl_r: 0xA3,
    Key.alt: 0x12,
    Key.alt_r: 0xA5,
    Key.caps_lock: 0x14,
    Key.delete: 0x2E,
    Key.insert: 0x2D,
    Key.home: 0x24,
    Key.end: 0x23,
    Key.page_up: 0x21,
    Key.page_down: 0x22,
    Key.up: 0x26,
    Key.down: 0x28,
    Key.left: 0x25,
    Key.right: 0x27,
    Key.f1: 0x70,
    Key.f2: 0x71,
    Key.f3: 0x72,
    Key.f4: 0x73,
    Key.f5: 0x74,
    Key.f6: 0x75,
    Key.f7: 0x76,
    Key.f8: 0x77,
    Key.f9: 0x78,
    Key.f10: 0x79,
    Key.f11: 0x7A,
    Key.f12: 0x7B,
    Key.media_volume_up: 0xAF,
    Key.media_volume_down: 0xAE,
    Key.media_next: 0xB0,
    Key.media_previous: 0xB1,
    Key.media_play_pause: 0xB3,
    Key.num_lock: 0x90,
}

for i in range(26):
    pynput_to_win32_keycodes[chr(97 + i)] = 0x41 + i  # a-z -> VK_A bis VK_Z

for i in range(10):
    pynput_to_win32_keycodes[str(i)] = 0x30 + i  # 0-9 -> VK_0 bis VK_9



def convert_from_string_to_vk_keycode(key):
    return pynput_to_win32_keycodes.get(key)



