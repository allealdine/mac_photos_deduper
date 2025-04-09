import subprocess
import json


def get_photo_names():
    script = """
    tell application "Photos"
        set photoNames to {}
        repeat with i from 1 to count of media items
            set thisItem to media item i
            set end of photoNames to filename of thisItem
        end repeat
        return photoNames
    end tell
    """
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip().split(", ")


photo_names = get_photo_names()
print("Total photos found:", len(photo_names))
