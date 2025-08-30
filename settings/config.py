# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import os, logging

SPIDERFOOT_PORT = 5001
SHOW_JSON = True
spiderfoot_process = None
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
USE_TOR_PROXY = True  
TOR_PROXY = "socks5h://127.0.0.1:9050"


def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )