import os

def rename_images(directory_path):
    if not os.path.exists(directory_path):
        print(f"The specified directory '{directory_path}' does not exist.")
        return

    files = os.listdir(directory_path)

    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if not image_files:
        print(f"No image files found in '{directory_path}'.")
        return
    

    for i, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{i}{extension}"
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        os.rename(old_path, new_path)

if __name__ == "__main__":
    image_directory = "images"

    rename_images(image_directory)
