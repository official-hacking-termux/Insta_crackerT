import time
import sys
import os

# ---- Demo settings ----
DEMO_USERNAME = "admin"            # demo local user (you can change)
DEMO_PASSWORD = "Passw0rd!"        # correct demo password (local only)
TRY_DELAY = 0.15                   # seconds between tries (for visible progress)

# ---- Colors ----
RED    = "\033[91m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
MAGENTA= "\033[95m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

# ---- Banner ----
def print_banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(RED + "="*65 + RESET)
    print(GREEN + BOLD + r"""

 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

 ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝
    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """ + RESET)
    print(CYAN + BOLD + "             HACKING TERMUX (VERSION)" + RESET)
    print(MAGENTA + "             Tool created by Anonymous Teach" + RESET)
    print(RED + "="*65 + RESET + "\n")

# ---- Helpers ----
def readable_path(p):
    try:
        return os.path.abspath(os.path.expanduser(p))
    except Exception:
        return p

def simulate_try(username, candidate):
    # purely cosmetic: show attempt in red, success in green
    print(RED + f"Trying username='{username}' password='{candidate}'" + RESET,
          end="\r", flush=True)

# ---- Main ----
def main():
    print_banner()
    print(CYAN + "NOTE: This Tool is only for educational purpose.\n" + RESET)

    username = input(GREEN + "Enter username to target: " + RESET).strip()
    wl_path = input(GREEN + "Enter path to wordlist file: " + RESET).strip()
    wl_path = readable_path(wl_path)

    if not os.path.isfile(wl_path):
        print(RED + f"\nError: Wordlist file not found at: {wl_path}" + RESET)
        sys.exit(1)

    try:
        with open(wl_path, "r", encoding="utf-8", errors="ignore") as f:
            total = sum(1 for _ in f)
    except Exception as e:
        print(RED + "Could not read wordlist file: " + str(e) + RESET)
        sys.exit(1)

    print(CYAN + f"\nSimulating wordlist attack on user '{username}'" + RESET)
    print(MAGENTA + f"Wordlist: {wl_path}  —  {total} candidates\n" + RESET)
    time.sleep(0.6)

    found = False
    tried = 0
    with open(wl_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            candidate = line.rstrip("\n").strip()
            if candidate == "":
                continue
            tried += 1
            simulate_try(username, candidate)
            time.sleep(TRY_DELAY)

            if username == DEMO_USERNAME and candidate == DEMO_PASSWORD:
                print(" " * 120, end="\r")
                print(GREEN + f"[{tried}/{total}] Password FOUND for user '{username}': {candidate}" + RESET)
                found = True
                break

    if not found:
        print("\n" + " " * 120, end="\r")
        print(RED + f"\nTried {tried} candidates. No match found in the wordlist." + RESET)

    print(CYAN + "\nDone. Reminder: do not misuse this tool." + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\nCancelled by user. Bye." + RESET)
