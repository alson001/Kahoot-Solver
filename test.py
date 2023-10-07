import keyboard
import pyautogui
import pytesseract


"""
Use this snippet to get the coordinates of the mouse cursor to help you get the coordinates for your screenshots.
pyautogui.moveTo(0, 0)
while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")
"""
# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\alson\\OneDrive\\Documents\\Script\\tesseract.exe"  # Path to tesseract.exe example path: r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def test_screenshots_of_buttons():
    # Coordinates for each button
    button_coords = {
        0: {"top_left": (200, 100), "bottom_right": (1800, 260)},
        1: {"top_left": (30, 800), "bottom_right": (940, 930)},
        2: {"top_left": (970, 800), "bottom_right": (1900, 930)},
        3: {"top_left": (30, 940), "bottom_right": (940, 1070)},
        4: {"top_left": (970, 940), "bottom_right": (1900, 1070)},
    }

    for button in button_coords:
        coords = button_coords[button]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        # Calculate width and height
        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_path = f"screenshot_button_{button}.png"
        screenshot.save(screenshot_path)
        # Open the screenshot
        # os.system(
        #   f"start {screenshot_path}"
        # )  # Use "xdg-open" on Linux, "start" on Windows


def ocr_test():
    # Coordinates for each button
    button_coords = {
        0: {"top_left": (200, 100), "bottom_right": (1800, 200)},
        1: {"top_left": (30, 800), "bottom_right": (940, 930)},
        2: {"top_left": (970, 800), "bottom_right": (1900, 930)},
        3: {"top_left": (30, 940), "bottom_right": (940, 1070)},
        4: {"top_left": (970, 940), "bottom_right": (1900, 1070)},
    }

    for button in button_coords:
        coords = button_coords[button]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        # Calculate width and height
        width = x2 - x1
        height = y2 - y1

        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_text = pytesseract.image_to_string(screenshot)
        if screenshot_text.strip() == "a\\":
            print("No text detected.")
            continue
        if not screenshot_text.strip():
            print("No text detected.")
            continue
        print(f"Text for button {button}: {screenshot_text}")


# Bind the function to a hotkey (e.g., Ctrl+Alt+T)
keyboard.add_hotkey("ctrl+alt+t", ocr_test)
# Keep the program running
keyboard.wait()
