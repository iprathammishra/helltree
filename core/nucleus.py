
class Tree:
    def __init__(self, f_list: list) -> None:
        self.f_list = f_list

    def __display__(self, name):
        print()
        for file in self.f_list:
            print(file[file.find(name.split('/')[-1]):])


def cloud(mlist: list, root: str) -> None:
    hell = Tree(mlist)
    hell.__display__(root)
