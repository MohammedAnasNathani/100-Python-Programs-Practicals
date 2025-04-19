import os

def os_module_demo():
    # Get current working directory
    print("Current working directory:", os.getcwd())

    # List files and directories in the current directory
    print("Files and directories:", os.listdir('.'))

    # Create a new directory
    os.mkdir('new_directory')
    print("Created new directory: new_directory")

    # Rename a file/directory
    os.rename('new_directory', 'renamed_directory')
    print("Renamed directory to: renamed_directory")

    # Remove a directory
    os.rmdir('renamed_directory')
    print("Removed directory: renamed_directory")

os_module_demo()
