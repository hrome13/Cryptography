import os

def save_secret_key(path, sk)
    # Set the path to the USB drive
    # usb_drive_path = '/media/usb'

    # Set the filename for the text file on the USB drive
    filename = 'secret_key.txt'

    # Set the full path to the text file on the USB drive
    file_path = os.path.join(path, filename)

    # Save the string to the text file on the USB drive
    with open(file_path, 'w') as f:
        f.write(sk)