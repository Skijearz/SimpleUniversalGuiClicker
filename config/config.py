import tomlkit
hotkeys = {}
def read_hotkeys_from_config()->None:
    with open("config.toml",mode="rt") as f_open:
        config = tomlkit.load(f_open)
        for hotkey in config['Hotkeys']:
            hotkeys[hotkey] = config["Hotkeys"][hotkey]
                
    
def save_hotkeys_to_config()-> None:
    with open("config.toml",mode="w+") as f_open:
        config = tomlkit.load(f_open)
        config["Hotkeys"] = hotkeys
        tomlkit.dump(config,f_open)