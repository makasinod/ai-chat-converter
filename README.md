#chat-gpt-converter
chat-gpt-converter is a utility for converting ChatGPT/OpenAI chat JSON files into .docx and .txt formats. It supports both single-file and batch folder processing.

##Features
- Supports ChatGPT Export and OpenAI API JSON formats.
- Converts to DOCX and TXT with clear role separation (User/Assistant).
- Automatically creates output folders and safe file names.
- Batch processing of all JSON files in a selected folder.

##Installation
Clone the repository:
bash
```
git clone <YOUR_REPOSITORY_URL>
cd chat-gpt-converter
```

Install dependencies using uv:
bash
```
uv sync
```

##Usage
1. Convert a single file
    - Place your JSON file in the inputs/ folder.

      Run the script:

      bash
      ```
      uv run main.py
      ```
    - Then enter the file name (without extension) when prompted.

2. Batch convert all files in a folder
    bash
    ```
    uv run main.py --all true --folder_name inputs/your_folder
    `inputs/your_folder — path to the folder with JSON files`

3. Output files
    All results are saved in the outputs/ folder, with unique names for each chat.

##Project Structure

    chat-gpt-converter/
    ├── inputs/           # Input JSON files
    ├── outputs/          # Output DOCX and TXT files
    ├── main.py           # Main script
    ├── chat_to_files.py  # Conversion logic
    ├── pyproject.toml    # Project dependencies
    └── README.md         # Project description


##Supported JSON Formats
OpenAI API:
json
```
{
  "messages": [
    {"role": "user", "content": "Hi!"},
    {"role": "assistant", "content": "Hello!"}
  ]
}
```
ChatGPT Export:
json
```
{
  "mapping": {
    "id1": {
      "message": {
        "author": {"role": "user"},
        "content": {"parts": ["Hi!"]}
      }
    },
    ...
  }
}
```

##Requirements
    - Python >= 3.12
    - python-docx
    - uv (for dependency management and running)

##Known Issues
1. The file must be located in the inputs/ folder or its subfolders.
2. Only the formats described above are supported.
