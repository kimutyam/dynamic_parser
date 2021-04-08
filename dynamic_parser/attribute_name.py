from dataclasses import dataclass


@dataclass(frozen=True)
class AttributeName:
    value: str

    # AttributeNameを評価できていないため、type hint定義不能??
    def add_prefix(self, prefix):
        return AttributeName(f"{prefix}{self.value}")
