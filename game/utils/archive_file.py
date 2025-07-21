import os
from datetime import datetime


def archive_file(file_path: str, history_path: str) -> None:
    """
    Archive a file by moving it to a history directory with a timestamp.
    Create the history directory if it doesn't exist.
    """
    if os.path.exists(file_path):
        os.makedirs(history_path, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Extract filename and extension safely
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        new_file_name = f"{name}_{timestamp}{ext}"
        os.rename(file_path, os.path.join(history_path, new_file_name))