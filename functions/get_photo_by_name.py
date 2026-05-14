from aiogram.types import FSInputFile
import os

def get_photo(folder_path: str, filename: str) -> FSInputFile:
    full_path = os.path.join(folder_path, filename)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f'Файл {filename} не найден в {folder_path}')

    return FSInputFile(full_path)

