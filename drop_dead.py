import sys
import time
import os

# ANSI color codes for aesthetic VS Code terminal look
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    PINK = "\033[38;2;255;105;180m"
    PURPLE = "\033[38;2;186;85;211m"
    CYAN = "\033[38;2;0;255;255m"
    BLUE = "\033[38;2;100;149;237m"
    YELLOW = "\033[38;2;255;215;0m"
    GRAY = "\033[38;2;128;128;128m"

# Enable ANSI colors on Windows terminal if needed
if os.name == 'nt':
    os.system('')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, char_delay=0.065, color=Colors.PINK):
    """Prints text character-by-character with typewriter effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write(Colors.RESET + "\n")

def main():
    clear_screen()
    print(f"{Colors.PURPLE}{Colors.BOLD}┌{'─'*52}┐{Colors.RESET}")
    print(f"{Colors.PURPLE}{Colors.BOLD}│      🎧 Now Playing: Olivia Rodrigo - Drop Dead     │{Colors.RESET}")
    print(f"{Colors.PURPLE}{Colors.BOLD}└{'─'*52}┘{Colors.RESET}\n")
    time.sleep(1.2)

    # List of (Lyric, character typing speed, pause after line, text color)
    lyrics = [
        ("Oh, one night I was bored in bed", 0.075, 0.45, Colors.PINK),
        ("And stalked you on the internet", 0.070, 0.55, Colors.PINK),
        ("It's feminine intuition", 0.080, 0.60, Colors.CYAN),
        ("'Cause I always had a vision of us standing like this", 0.055, 0.70, Colors.PURPLE),
        ("All pressed up in the bathroom line", 0.070, 0.50, Colors.BLUE),
        ("You're lookin' like an angel on the walls of Versailles", 0.058, 0.65, Colors.YELLOW),
        ("The most alive I've ever been", 0.075, 0.85, Colors.CYAN),
        ("But kiss me and I might...", 0.090, 0.60, Colors.PINK),
        ("...DROP DEAD 🖤✨", 0.110, 2.00, Colors.PINK + Colors.BOLD),
    ]

    for line, char_delay, line_pause, color in lyrics:
        type_text(line, char_delay, color)
        time.sleep(line_pause)

    print(f"\n{Colors.GRAY}─── [End of Preview] ───{Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.GRAY}Program dihentikan.{Colors.RESET}")

