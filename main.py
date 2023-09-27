from core.nucleus import Tree, cloud
from core.ignore import ignor
import os
import sys


def is_there(root: str, ignore: list) -> bool:
    for item in ignore:
        if root.replace('\\', '/').__contains__(item) == True:
            return True
    return False


def main(path) -> list:
    files_list = []
    for root, _, files in os.walk(path):
        for file in files:
            if is_there(root, ignor) == False:
                files_list.append(os.path.join(root, file).replace('\\', '/'))
    return files_list


if __name__ == "__main__":
    argv_list = ['--h', '.', '--cwd', '--e', '::path']

    if len(sys.argv) > 2 or len(sys.argv) <= 1:
        print("Usage: python main.py --h ")
        sys.exit(1)

    if sys.argv[1] == '--h':
        print(
            """
Welcome to Helltree! 💀

Command: python main.py <action>

<Action>      <Abbreviation>        <Description>
--h           help                  Display this help message.
--cwd         current directory     Display the current working directory.
.             period                Generate a tree structure of the current directory.
--e           exit                  Exit the program.
::path/       path of the folder    Generate a personalized tree for the specified folder path.
                                    Example: python main.py ::path/to/folder
        """
        )

    elif sys.argv[1] == '--cwd':
        print(os.getcwd())

    elif sys.argv[1].split('/')[0] not in argv_list:
        print("Usage: python main.py --h ")
        sys.exit(1)

    elif sys.argv[1] == '--e':
        sys.exit(1)

    elif sys.argv[1] == '.':
        cloud(main(os.getcwd()), os.getcwd().replace('\\', '/'))

    else:
        path = "".join(sys.argv[1][7:])
        if os.path.exists(path):
            print("\n'✅ os.path.exists passed.'\n")
            cloud(main(path), path)
        else:
            print("\n'❌ Path doesn't exist.'\n")
