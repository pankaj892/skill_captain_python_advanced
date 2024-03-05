import os
import shutil

def organize_files(source_dir, dest_dir):
    try:
        # Create destination folders if they don't exist
        categories = ['images', 'documents', 'music', 'videos']
        for category in categories:
            folder_path = os.path.join(dest_dir, category)
            os.makedirs(folder_path, exist_ok=True)

        # Scan the source directory
        files = os.listdir(source_dir)

        for file in files:
            file_path = os.path.join(source_dir, file)
            if os.path.isfile(file_path):
                # Categorize files based on their extensions
                file_extension = os.path.splitext(file)[-1].lower()
                if file_extension in ('.jpg', '.png', '.gif'):
                    category = 'images'
                elif file_extension in ('.doc', '.pdf', '.txt'):
                    category = 'documents'
                elif file_extension in ('.mp3', '.wav', '.flac'):
                    category = 'music'
                elif file_extension in ('.mp4', '.avi', '.mkv'):
                    category = 'videos'
                else:
                    category = 'others'

                # Move files to their respective destination folders
                dest_folder = os.path.join(dest_dir, category)
                shutil.move(file_path, dest_folder)

        print('File organization complete.')
    except FileNotFoundError:
        print('Source or destination directory does not exist.')
    except PermissionError:
        print('Permission denied. Unable to access files or create folders.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Example usage:
source_directory = 'C:/Users/Username/Desktop/'
destination_directory = 'C:/Users/Username/Documents/'

organize_files(source_directory, destination_directory)
