import argparse
import os

from chat_to_files import ChatConverter

# === Перетворити всі файли в папці ===
parser = argparse.ArgumentParser(description="Convert ChatGPT JSON to DOCX and TXT")
parser.add_argument(
    "--all",
    required=False,
    help="Назва JSON-файлу, який треба обробити (наприклад: chat.json.)",
)
parser.add_argument(
    "--folder_name",
    required=False,
    help="Назва папки з JSON-файлами для обробки (наприклад: chats)"
)
args = parser.parse_args()

def ask_filename():
    """Запитує у користувача назву JSON-файлу без розширення."""
    file_base = input(
        "Введіть назву JSON-файлу для обробки без розширення (наприклад: chat).\n"
        "Увага: файл має бути у папці inputs!!!\n"
        "Якщо ви бажаєте конвертувати всі файли, додайте '--all true --folder-name ...'"
        "ПРИКЛАД: 'uv run main.py --all true --folder_name inputs/some' у скрипт.\n"
        "Для продовження введіть назву файлу або натисніть 'Ctrl + C': "
    ).strip()
    return find_file(file_base)

def find_file(file_name: str) -> str:
    """
    Шукає JSON-файл у папці 'inputs' і всіх підпапках.
    Повертає повний шлях до файлу або піднімає помилку, якщо файл не знайдено.
    """
    search_root = "inputs"
    target = f"{file_name}.json" if not file_name.endswith(".json") else file_name

    for root, _, files in os.walk(search_root):
        if target in files:
            return os.path.join(root, target)

    raise FileNotFoundError(f"❌ Файл '{target}' не знайдено у '{search_root}' або його підпапках.")


if __name__ == "__main__":
    converter = ChatConverter()

    if args.all and args.folder_name:
        folder_path = args.folder_name
        print(f"Files in folder: {os.listdir(folder_path)}")
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"❌ Папка '{folder_path}' не знайдена!")

        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                # input_file = os.path.join(folder_path, filename)
                print(f"Обробка файлу: {filename}")
                converter.convert(find_file(filename))
    else:
        converter.convert(ask_filename())
