import signal
import sys
from menu import menu
from banner import banner_color


def signal_handler(sig, frame):
    print("\nPhantomKey is closing")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


print(banner_color)


if __name__ == "__main__":
    try:
        menu.main_menu()
    except KeyboardInterrupt:
        print("\nPhantomKey is closing")
        sys.exit(0)
