from pydantic.dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class SomePydanticDataClass:
    a: int
    b: str


class SomePydanticModelClass(BaseModel):
    c: int
    something: float


if __name__ == '__main__':
    some_data_class = SomePydanticDataClass(
        a=1,
        b='a',
    )
    some_model_class = SomePydanticModelClass(
        c=1,
        something=0.3,
    )

