from dataclasses import dataclass


@dataclass(frozen=True)
class Tag:
    name: str


class TagRegistry:
    def __init__(self) -> None:
        self._by_name: dict[str, Tag] = {}

    def get_or_create(self, name: str) -> Tag:
        if name in self._by_name:
            return self._by_name[name]
        self._by_name[name] = Tag(name)

        return self._by_name[name]


class Document:
    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title
        self._tags: set[Tag] = set()

    @property
    def tags(self) -> set[Tag]:
        return set(self._tags)

    def add_tag(self, tag: Tag) -> None:
        if tag in self._tags:
            raise ValueError("Такой тэг уже закреплен!")
        self._tags.add(tag)


class Folder:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self._documents: list[Document] = []

    @property
    def documents(self) -> list[Document]:
        return list(self._documents)

    def add_document(self, document: Document) -> None:
        if any(existing.title == document.title for existing in self._documents):
            raise ValueError("Такой файл уже есть!")
        self._documents.append(document)


class Workspace:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self._folders: list[Folder] = []

    @property
    def folders(self) -> list[Folder]:
        return list(self._folders)

    def rename(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("name is empty")
        self.name = new_name

    def add_folder(self, folder: Folder) -> None:
        if any(existing.name == folder.name for existing in self._folders):
            raise ValueError("Такая папка уже есть!")
        self._folders.append(folder)

    def count_documents(self) -> int:
        return sum(len(folder.documents) for folder in self._folders)
