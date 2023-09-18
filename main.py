from core.nucleus import Tree
import os

root_directory = "/workspaces/helltree"
directories_list = []
files_list = []

for root, directories, files in os.walk(root_directory):
    for directory in directories:
        directories_list.append(os.path.join(root, directory))
    for file in files:
        files_list.append(os.path.join(root, file))

if __name__ == "__main__":
    initialize = Tree(directories_list, files_list)
