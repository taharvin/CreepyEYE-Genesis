# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages
from settings.api.api import WHOIS_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.whois")

def whois(domain, language="en"):
    logger.info("\n" + check_messages[language]["whois_check"].format(query=domain))

    if not validate_api_key(WHOIS_API_KEY, "WhoIs", language=language):
        return
    
    try:
        url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService"
        params = {"apiKey": WHOIS_API_KEY, "domainName": domain, "outputFormat": "JSON"}
        data = make_request("GET", url, params=params, language=language)

        if data and isinstance(data, dict):
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))

            whois_record = data.get("WhoisRecord")
            if whois_record:
                domain_name = whois_record.get('domainName', 'N/A')
                organization = whois_record.get('registrant', {}).get('organization', 'N/A')
                country = whois_record.get('registrant', {}).get('country', 'N/A')

                print(colored(info_details[language]["domain_checked"], "green"), domain_name)
                print(colored(info_details[language]["organization"], "green"), organization)
                print(colored(info_details[language]["country"], "green"), country)
            else:
                log_warning_yellow(status_messages[language]["no_results"])
        else:
            log_warning_yellow(error_details[language]["empty_response"])
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))