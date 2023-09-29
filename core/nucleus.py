
class Tree:
    def __init__(self, f_list: list) -> None:
        self.f_list = f_list

    def make(self, root) -> None:
        paths = [
            file[file.find(root.split('/')[-1]):]
            for file in self.f_list
        ]
        paths.reverse()
        nlist = []
        for i, path in enumerate(paths):
            split = path.split('/')
            for i, item in enumerate(split):
                nlist.append([i * ' ', '└─', item])

        for iteration, value in enumerate(nlist):
            for k in range(iteration+1, len(nlist)):
                if (nlist[k] == value):
                    nlist[k] = '0'

        for y in nlist:
            if y != '0':
                print("".join(y))


def cloud(mlist: list, root: str) -> None:
    print("\nRoot")
    hell = Tree(mlist)
    hell.make(root)
