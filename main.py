from vectree.domain.entities import Document, Folder
from vectree.domain.ports import TagRepository
from vectree.domain.services import move_document


def attach_tag(document: Document, repo: TagRepository, name: str) -> None:
    document.add_tag(repo.get_or_create(name))


def main() -> None:
    f1 = Folder(1, "pupupu")
    f2 = Folder(2, "tututu")
    f3 = Folder(3, "lalala")
    d1 = Document(1, "1.md")
    d2 = Document(2, "2.md")
    d3 = Document(3, "3.md")

    f1.add_document(d1)
    f2.add_document(d2)
    f3.add_document(d3)

    move_document(f1, f3, d1)
    print(len(f1.documents), len(f3.documents))


if __name__ == "__main__":
    main()
