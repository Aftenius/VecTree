from vectree.domain.entities import Document, Folder


def move_document(source: Folder, target: Folder, document: Document) -> None:
    target.add_document(document)
    source.remove_document(document)
