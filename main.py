from vectree.domain.entities import Document, Folder, TagRegistry, Workspace
from vectree.domain.ports import TagRepository


def attach_tag(document: Document, repo: TagRepository, name: str) -> None:
    document.add_tag(repo.get_or_create(name))


def main() -> None:
    ws = Workspace(1, "Test")
    f1 = Folder(1, "pupupu")
    f2 = Folder(2, "tututu")
    f3 = Folder(3, "lalala")
    d1 = Document(1, "1.md")
    d2 = Document(2, "2.md")
    d3 = Document(3, "3.md")

    f1.add_document(d1)
    f2.add_document(d2)
    f3.add_document(d3)

    ws.add_folder(f1)
    ws.add_folder(f3)

    t = TagRegistry()
    attach_tag(d1, t, "RED")

    print(ws.count_documents())


if __name__ == "__main__":
    main()
