# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import requests
import logging
from settings.proxy.tor import get_smart_session
from settings.translations import error_details
from settings.helpers import log_error_red
logger = logging.getLogger("settings.make_request")

def make_request(method, url, params=None, api_key=None, data=None, files=None, timeout=10, language="en"):
    session = get_smart_session(language)
    if api_key is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CreepyEYE Genesis)",
        }
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CreepyEYE Genesis)",
            "Authorization": f"Bearer {api_key}"
        }

    try:
        if method == "GET":
            res = session.get(url, params=params, headers=headers, timeout=timeout)
        elif method == "POST":
            res = session.post(url, data=data, files=files, headers=headers, timeout=timeout)
        else:
            raise ValueError(error_details[language]["unsupported_request_method"])

        res.raise_for_status()

        try:
            return res.json()
        except Exception:
            return res.text
        
    except requests.exceptions.Timeout:
        log_error_red(error_details[language]["request_timeout"].format(url=url))
    except requests.exceptions.RequestException as e:
        log_error_red(error_details[language]["request_error"].format(url=url, e=e))
    return None

