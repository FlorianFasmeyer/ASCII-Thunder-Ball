from pynput import keyboard

controls = {
    'w':                False,  # Jump.
    'a':                False,  # Left.
    'd':                False,  # Right.
    keyboard.Key.esc:   False   # Quit game.
}


def on_press(key):
    try:
        controls[key.char] = True
    except AttributeError:
        pass  # If special char, do nothing!
    except KeyError:
        pass  # If not a move key, do nothing


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    try:
        controls[key.char] = False
    except AttributeError:
        pass  # If special char, do nothing!
    except KeyError:
        pass  # If not a move key, do nothing


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# non-blocking fashion (generates a thread).
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
