from vectree.domain.entities import Document, Folder, Workspace
from vectree.domain.ports import TagRepository


def attach_tag(document: Document, repo: TagRepository, name: str) -> None:
    document.add_tag(repo.get_or_create(name))


def main() -> None:
    ws = Workspace(1, "HOME")
    f1 = Folder(1, "New Direct")
    f2 = Folder(1, "New Direct_sub")
    f3 = Folder(1, "1234")
    f4 = Folder(1, "qwert")
    f5 = Folder(1, "q023da")
    f6 = Folder(1, "1010soso401!")
    f7 = Folder(1, "PSDFJPP")
    ws.add_folder(f1)
    f1.add_subfolder(f2)
    f2.add_subfolder(f3)
    f3.add_subfolder(f4)
    f3.add_subfolder(f5)
    f5.add_subfolder(f6)

    d1 = Document(1, "test")
    d2 = Document(1, "1234")
    f2.add_document(d1)
    f5.add_document(d2)
    f5.add_document(d1)

    print(ws.count_documents())

    try:
        f6.add_subfolder(f7)
    except ValueError as ex:
        print(ex)

    print(ws.name)
    print(ws.folders[0].name)


if __name__ == "__main__":
    main()
