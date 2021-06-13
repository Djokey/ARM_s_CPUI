import configparser as cp
import os


def get_option(option, path="config.ini", section="Settings"):
    if not os.path.exists(path):
        create_new_config(path)
    else:
        config = cp.ConfigParser()
        config.read(path, encoding="cp1251")
        if config.has_option(section, option):
            ret = config.get(section, option)
        else:
            ret = 'None'
        return ret


def set_option(option, setting, path="config.ini", section="Settings"):
    if not os.path.exists(path):
        create_new_config(path)
    else:
        config = cp.ConfigParser()
        config.read(path, encoding="cp1251")
        if config.has_section(section):
            config.set(section, option, setting)
        else:
            _add_section(path, section)
            config = cp.ConfigParser()
            config.read(path, encoding="cp1251")
            config.set(section, option, setting)
        with open(path, "w") as config_file:
            config.write(config_file)


def _add_section(path="config.ini", section="Settings"):
    if os.path.exists(path):
        config = cp.ConfigParser()
        config.read(path, encoding="cp1251")
        if config.has_section(section):
            ret = "0"
        else:
            config.add_section(section)
            with open(path, "w") as config_file:
                config.write(config_file)
                config_file.close()
            ret = "1"
    else:
        ret = '2'
        create_new_config(path)
    return ret


def create_new_config(path="config.ini"):
    disk_dir = os.getenv("SystemDrive")
    user = os.environ.get("USERNAME")
    config = cp.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "account", r"None")
    config.set("Settings", "password", r"None")
    config.set("Settings", "mail", r"imap.mail.ru")
    config.set("Settings", "sender", r"None")
    config.set("Settings", "path_for_save_letters", f"{disk_dir}:\\Users\\{user}\\Desktop\\Почта\\")
    config.set("Settings", "time_sleep", "600")
    config.set("Settings", "letters", r"0")
    with open(path, "w") as config_file:
        config.write(config_file)


def remove_option(option, path="config.ini", section="Settings"):
    config = cp.ConfigParser()
    config.read(path, encoding="cp1251")
    config.remove_option(section, option)
    with open(path, "w") as config_file:
        config.write(config_file)
