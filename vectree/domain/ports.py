from typing import Protocol

from vectree.domain.entities import Tag


class TagRepository(Protocol):
    def get_or_create(self, name: str) -> Tag: ...
