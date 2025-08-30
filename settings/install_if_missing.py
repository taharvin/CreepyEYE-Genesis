# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import importlib, subprocess, sys
from settings.translations import settings_details, warnings, menu_details

def check_and_install(module_name, language="en"):
    try:
        importlib.import_module(module_name)
    except ImportError:
        ans = input(settings_details[language]["module_not_found"].format(module_name=module_name)).strip().lower()
        if ans == 'y':
            subprocess.call([sys.executable, "-m", "pip", "install", module_name])
        else:
            print(warnings[language]["missing_module"].format(module_name=module_name))
            print(menu_details[language]["exit_message"])
            sys.exit()