
import shutil
from pathlib import Path
from datetime import datetime

# File extension categories
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".html", ".css", ".js", ".cpp", ".c"]
}


def get_category(extension):

    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def get_unique_path(destination):

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):

    source_folder = Path(folder_path).expanduser()

    if not source_folder.exists() or not source_folder.is_dir():
        print("Error: Please enter a valid folder path.")
        return

    moved_count = 0
    failed_count = 0
    category_count = {}

    print("\nStarting File Organizer...")
    print("--------------------------------")

    # Read files from the selected folder
    for file in source_folder.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.suffix)

        destination_folder = source_folder / category

        try:
            # Create category folder if it doesn't exist
            destination_folder.mkdir(exist_ok=True)

            destination_file = destination_folder / file.name

            # Prevent filename collisions
            destination_file = get_unique_path(destination_file)

            # Move file
            shutil.move(str(file), str(destination_file))

            print(f"Moved: {file.name} -> {category}/")

            moved_count += 1
            category_count[category] = (
                category_count.get(category, 0) + 1
            )

        except PermissionError:
            print(f"Permission denied: {file.name}")
            failed_count += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")
            failed_count += 1

    # Display execution summary
    print("\n========== ORGANIZATION SUMMARY ==========")
    print("Total files moved:", moved_count)
    print("Failed operations:", failed_count)

    for category, count in category_count.items():
        print(f"{category}: {count} files")

    print("Completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("==========================================")


def main():

    print("\n================================")
    print("     AUTOMATED FILE ORGANIZER")
    print("================================")

    folder_path = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    if not folder_path:
        print("Folder path cannot be empty.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
