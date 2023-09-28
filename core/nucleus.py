# └─ ├─ │

class Tree:
    def __init__(self, f_list: list) -> None:
        self.f_list = f_list

    def make(self, root) -> None:
        paths = [
            file[file.find(root.split('/')[-1]):]
            for file in self.f_list
        ]


def cloud(mlist: list, root: str) -> None:
    print("\nRoot")
    hell = Tree(mlist)
    hell.make(root)
