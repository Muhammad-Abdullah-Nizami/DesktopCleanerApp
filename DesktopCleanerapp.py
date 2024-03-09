
import os
import shutil
def clean_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    for file_name in os.listdir(desktop_path):
        if os.path.isdir(os.path.join(desktop_path, file_name)):
            continue

        _, file_ext = os.path.splitext(file_name)

        folder_path = os.path.join(desktop_path, file_ext[1:].upper() + "_Files")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(os.path.join(desktop_path, file_name), folder_path)

if __name__ == "__main__":

    clean_desktop()
    print("Desktop cleaned and all files moved to folders!")
