# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


check_messages = {
    "uk": {
        "abuseipdb_check": "\n[🚨] AbuseIPDB для IP: {query}",
        "emailrep_check" : "\n[🔍] EmailRep перевірка: {query}",
        "greynoise_check": "\n[🚨] GreyNoice перевірка: {query}",
        "ipinfo_check": "\n[🌐] Перевірка IP: {query}",
        "numverify_check": "\n[📞] Перевірка номера телефону: {query}",
        "hunter_check": "\n[📧] Перевірка email через Hunter.io: {query}",
        "username_search": "\n[🔍] Пошук по ніку: {query}",
        "shodan_check": "\n[🔍] Shodan перевірка: {query}",
        "virustotal_check" : "\n[🔍] VirusTotal перевірка: {query}",
        "spiderfoot_check": "\n[🕷️] SpiderFoot перевірка: {query}",
        "whois_check": "\n[🔍] Whois перевірка: {query}",
    },
    "en": {
        "abuseipdb_check": "\n[🚨] AbuseIPDB for IP: {query}",
        "emailrep_check" : "\n[🔍] EmailRep check: {query}",
        "greynoise_check": "\n[🚨] GreyNoice check: {query}",
        "ipinfo_check": "\n[🌐] Checking IP: {query}",
        "numverify_check": "\n[📞] Checking phone number: {query}",
        "hunter_check": "\n[📧] Checking email via Hunter.io: {query}",
        "username_search": "\n[🔍] Searching by username: {query}",
        "shodan_check": "\n[🔍] Shodan check: {query}",
        "virustotal_check": "[🔍] VirusTotal check: {query}",
        "spiderfoot_check": "\n[🕷️] SpiderFoot check: {query}",
        "whois_check": "\n[🔍] Whois check: {query}",
    }
}

status_messages = {
    "uk": {
        "processing": "[~] Обробка запиту: {query}",
        "results_found": "[+] Знайдено:",
        "no_results": "[-] Нічого не знайдено.",
        "tor_status_active": "[+] Tor увімкнено — з'єднання зашифровано"
    },
    "en": {
        "processing": "[~] Processing query: {query}",
        "results_found": "[+] Found:",
        "no_results": "[-] No results found.",
        "tor_status_active": "[+] Tor routing enabled – connection anonymized"
    }
}

error_details = {
    "uk": {
        "key_error" : "[!] Ключ {e} не знайдено у словнику",
        "api_error": "[!] Помилка API: {e}",
        "error": "[!] Сталася помилка {e}",
        "json_error": "[!] Помилка декодування JSON відповіді: {e}",
        "empty_response": "[!] Сервер повернув порожню відповідь.",
        "request_timeout": "[!] Тайм-аут при запиті до {url}",
        "request_error": "[!] Помилка при запиті до {url}: {e}",
        "found_and_status": "[!] Ресурс {name} знайдено за URL {url} — статус: {res}",
        "unsupported_request_method": "[!] Непідтримуваний метод запиту",
        "dependency_check_failed": "[!] Перевірка залежностей провалена! Будь ласка, встановіть відсутні модулі або додайте файл sf.py.",
        "env_errors": "[!] Не вдалося відкрити файл .env: {e}",
        "invalid_email": "[!] Неправильний формат email.",
        "invalid_ip": "[!] Невірна IP-адреса.",
        "invalid_domain": "[!] Невірне доменне ім’я.",
        "invalid_phone": "[!] Невірний номер телефону."
    },
    "en": {
        "key_error" : "[!] Key {e} not found in dictionary",
        "api_error": "[!] API error: {e}",
        "error": "[!] An error occurred: {e}",
        "json_error": "[!] JSON response decoding error: {e}",
        "empty_response": "[!] Server returned empty response.",
        "request_timeout": "[!] Request to {url} timed out",
        "request_error": "[!] Error while requesting {url}: {e}",
        "found_and_status": "[!] Resource {name} found at {url} — status: {res}",
        "unsupported_request_method": "[!] Unsupported request method",
        "dependency_check_failed": "[!] Dependency check failed! Please install the missing modules or add sf.py.",
        "env_errors": "[!] Failed to open .env file: {e}",
        "invalid_email": "[!] Invalid email format.",
        "invalid_ip": "[!] Invalid IP address.",
        "invalid_domain": "[!] Invalid domain name.",
        "invalid_phone": "[!] Invalid phone number."
    }
}

warnings = {
    "uk": {
        "ethical_use_warning" : (
            "[!] УВАГА - цей інструмент був створений тільки для етичних цілей. \n",
            "-> Розробники не несуть відповідальності за ваші дії."
        ),
        "missing_module" : "[!] Увага - Без '{module_name}' деякі функції не працюватимуть.",
        "missing_dependency": "[!] Модуль {module} відсутній!",
        "ascii_warning": "[!] Неможливо відобразити результати з не-ASCII символами. Використовується ASCII-only режим.",
        "tor_inactive_warning": "[!] Помилка підключення Tor — використовується стандартна мережа",

    },
    "en": {
        "ethical_use_warning" : (
            "[!] WARNING - this tool was created for ethical purposes only. \n",
            "-> Developers are not responsible for your actions."
        ),
        "missing_module" : "[!] Warning - Without '{module_name}' some functions will not work.",
        "missing_dependency": "[!] Module {module} is missing!",
        "ascii_warning": "[!] Unable to display results with non-ASCII characters. ASCII-only mode is being used.",
        "tor_inactive_warning": "[!] Tor connection error — standard network is being used"
    }
}

menu_details = {
    "uk": {
        "press_any_key": "Натисніть любу клавішу для продовження...",
        "exit_message" : "Вихід із CreepyEYE. Бувай!",
        "incorrect_option": "[!] Невірна опція. Спробуйте ще раз.",
        "menu": "--- ГОЛОВНЕ МЕНЮ ---",
        "choose_option": ">>> Оберіть опцію: ",
        "input_username": "Введіть псевдонім: ",
        "input_email": "Введіть email: ",
        "input_ip": "Введіть IP: ",
        "input_domain": "Введіть домен: ",
        "input_phone": "Введіть номер телефону  (в міжнародному форматі, наприклад, +380XXXXXXXXX або +1XXXXXXXXXX): ",
        "input_telegram_username": "Введіть Telegram псевдонім (без @): ",
        "tor_enabled": "[+] Tor увімкнено!",
        "tor_ip": "[+] IP через Tor: {ip}",
        "tor_not_running": "[-] Tor не запущений. Запусти Tor (наприклад, через Tor Browser або tor.exe)"

    },
    "en": {
        "press_any_key": "Press any key to continue...",
        "exit_message": "Exiting CreepyEYE. Goodbye!",
        "incorrect_option": "[!] Incorrect option. Please try again.",
        "menu": "--- MAIN MENU ---",
        "choose_option": ">>> Choose an option: ",
        "input_username": "Enter username: ",
        "input_email": "Enter email: ",
        "input_ip": "Enter IP: ",
        "input_domain": "Enter domain: ",
        "input_phone": "Enter phone number (in international format, e.g., +380XXXXXXXXX or +1XXXXXXXXXX): ",
        "input_telegram_username": "Enter Telegram username (without @): ",
        "tor_enabled": "[+] Tor is enabled!",
        "tor_ip": "[+] IP via Tor: {ip}",  
        "tor_not_running": "[-] Tor is not running. Start Tor (e.g., via Tor Browser or tor.exe)"

    }
}

info_details = {
    "uk": {
        "abuse_score": "[+] Рівень зловживань:",
        "last_report": "[+] Останнє повідомлення:",
        "reputation": "[+] Репутація:",
        "suspicious": "[+] Підозрілий:",
        "blacklist": "[+] На чорному списку:",
        "leaked_passwords": "[+] Злиті паролі:",
        "activity": "[+] Активність:",
        "domain_checked": "[+] Домен перевірено:",
        "classification": "[+] Класифікація:",
        "name": "[+] Назва:",
        "emails_found": "[+] Знайдені емейли на домені {domain}:",
        "ip_info": "[+] Інформація про IP:",
        "country": "[+] Країна:",
        "location": "[+] Локація:",
        "carrier": "[+] Оператор:",
        "provider": "[+] Провайдер:",
        "organization": "[+] Організація:",
        "os": "[+] ОС:",
        "detections": "[+] Виявлення:",
    },
    "en": {
        "abuse_score": "[+] Abuse Score:",
        "last_report": "[+] Last Report:",
        "reputation": "[+] Reputation:",
        "suspicious": "[+] Suspicious:",
        "blacklist": "[+] Blacklisted:",
        "leaked_passwords": "[+] Leaked Passwords:",
        "activity": "[+] Activity:",
        "domain_checked": "[+] Domain Checked:",
        "classification": "[+] Classification:",
        "name": "[+] Name:",
        "emails_found": "[+] Emails found on domain {domain}:",
        "ip_info": "[+] IP Information:",
        "country": "[+] Country:",
        "location": "[+] Location:",
        "carrier": "[+] Carrier:",
        "provider": "[+] Provider:",
        "organization": "[+] Organization:",
        "os": "[+] OS:",
        "detections": "[+] Detections:",
    }
}


menu = {
    "uk": [
        "Виберіть опцію:",
        "1. Пошук по псевдоніму/ім'ям 🔍",
        "2. Пошук по email 📧",
        "3. Перевірка IP 🌐",
        "4. Перевірка домену 🕵️",
        "5. Перевірка номера телефону 📱",
        "6. Налаштування API 🔧",
        "7. Запустити TOR 🔧",
        "8. Поміняти мову 🔄",
        "0. Вихід ❌"
    ],
    "en": [
        "Select an option:",
        "1. Search by username/name 🔍",
        "2. Search by email 📧",
        "3. Check IP 🌐",
        "4. Check domain 🕵️",
        "5. Check phone number 📱",
        "6. API settings 🔧",
        "7. Start TOR 🔧",
        "8. Change language 🔄",
        "0. Exit ❌"
    ]
}

settings_details = {
    "uk": {
        "module_not_found": "[!] Модуль '{module_name}' не знайдено. Встановити? (y/n): ",
        "some_modules_missing": "[!] Деякі модулі не знайдені. Бажаєте їх встановити автоматично? (y/n): ",
        "install_requirements": "Будь ласка, встановіть модулі за допомогою 'pip install -r requirements.txt', а потім повторно запустіть скрипт.",
        "invalid_option": "[!] Невірний ввід. Будь ласка, введіть 'y' або 'n'.",
        "missing_api_key": "[!] Змінна середовища '{name}' не знайдена в .env файлі!",
        "found_and_status": "[-] {name}: {url} - статус: {res}",
        "connection_error": "[-] {name}: Не вдалося підключитися до {url}",
        "env_file_created": "[+] Файл {env_path} створено!",
        "env_file_exists": "ℹ️ Файл {env_path} вже існує.",
        "api_key_not_found": "[!] {api_name} не знайдено в api_keys.env файлі!",
        "invalid_api_key": "[!] Невірний API ключ для {api_name} !",
        "too_many_attempts": "[!] Забагато невірних спроб. Вихід."
    },
    "en": {
        "module_not_found": "[!] Module '{module_name}' not found. Install? (y/n): ",
        "some_modules_missing": "[!] Some modules are missing. Do you want to install them automatically? (y/n): ",
        "install_requirements": "Please install the modules using 'pip install -r requirements.txt' and then rerun the script.",
        "invalid_option": "[!] Invalid input. Please enter 'y' or 'n'.",
        "missing_api_key": "[!] Environment variable '{name}' not found in .env file!",
        "found_and_status": "[-] {name}: {url} - status: {res}",
        "connection_error": "[-] {name}: Failed to connect to {url}",
        "env_file_created": "[+] File {env_path} created!",
        "env_file_exists": "ℹ️ File {env_path} already exists.",
        "api_key_not_found": "[!] {api_name} not found in api_keys.env file!",
        "invalid_api_key": "[!] Invalid API key for {api_name} !",
        "too_many_attempts": "[!] Too many invalid attempts. Exiting."

    }
}

spiderfoot_details = {
    "uk": {
        "start": "[🕷️] Запуск SpiderFoot...",
        "start_error": "[!] Помилка при запуску SpiderFoot: {e}",
        "stop": "[!] SpiderFoot зупинено",
        "stop_error": "[!] Помилка при зупинці SpiderFoot: {e}",
        "not_running": "[!] SpiderFoot неактивний",
        "already_running": "[!] SpiderFoot вже запущений",
        "timeout_error": "[!] Час вийшов при запиті до SpiderFoot",
        "status": "[~] Статус SpiderFoot: {status}",
        "request_error": "[!] Помилка при запиті до SpiderFoot: {e}",
        "error": "[!] Помилка SpiderFoot: {error}",
        "process_not_found": "[!] Процес SpiderFoot не знайдено або вже зупинено",
        "missing_sf_script": "[!] Файл sf.py не знайдено! Перевір, чи Spiderfoot встановлено правильно.",
        "start_error": "[!] Помилка запуску Spiderfoot: {e}",
        "sf_script_found": "[+] Знайдено sf.py",
        "spiderfoot_check": "[~] Виконується запит до Spiderfoot: {query}"
    },
    "en": {
        "start": "[🕷️] Starting SpiderFoot...",
        "start_error": "[!] Error starting SpiderFoot: {e}",
        "stop": "[!] SpiderFoot stopped",
        "stop_error": "[!] Error stopping SpiderFoot: {e}",
        "not_running": "[!] SpiderFoot is not running",
        "already_running": "[!] SpiderFoot is already running",
        "timeout_error": "[!] Timeout while making request to SpiderFoot",
        "status": "[~] SpiderFoot Status: {status}",
        "request_error": "[!] Error making request to SpiderFoot: {e}",
        "error": "[!] SpiderFoot Error: {error}",
        "process_not_found": "[!] SpiderFoot process not found or already stopped",
        "missing_sf_script": "[!] sf.py file not found! Check if Spiderfoot is installed correctly.",
        "start_error": "[!] Error starting Spiderfoot: {e}",
        "sf_script_found": "[+] sf.py found",
        "spiderfoot_check": "[~] Making request to Spiderfoot: {query}"
    }
}