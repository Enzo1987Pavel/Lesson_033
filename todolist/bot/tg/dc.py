from __future__ import annotations

# from dataclasses import field
# from typing import List, ClassVar, Type, Optional
#
# from marshmallow_dataclass import dataclass
# from marshmallow import Schema, EXCLUDE


from dataclasses import field
from typing import ClassVar, Type, List

from marshmallow_dataclass import dataclass
from marshmallow import Schema, EXCLUDE


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None
    username: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class MessageChat:
    id: int
    first_name: str | None
    username: str | None
    last_name: str | None
    type: str
    title: str | None

    class Meta:
        unknown = EXCLUDE


# @dataclass
# class MessageEntities:
#     offset: int | None
#     length: int
#     type_: str = field(metadata={'data_key': 'type'})
#
#     class Meta:
#         unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    from_: MessageFrom = field(metadata={'data_key': 'from'})
    chat: MessageChat
    date: int
    text: str | None
    # entities: list[MessageEntities]

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateOdj:
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateOdj]

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE



#
#
# @dataclass
# class Chat:
#     id: int
#     type: str
#     title: Optional[str] = None
#     username: Optional[str] = None
#     first_name: Optional[str] = None
#     last_name: Optional[str] = None
#
#     class Meta:
#         unknown = EXCLUDE
#
#
# @dataclass
# class MessageFrom:
#     id: int
#     first_name: str
#     last_name: Optional[str]
#     username: str
#
#     class Meta:
#         unknown = EXCLUDE  # Исключаем неизвестные/неуказанные поля
#
#
# @dataclass
# class Message:
#     message_id: int
#     # Нижнее подчеркивание 'from_', чтобы не путать со встроенными именами.
#     from_: MessageFrom = field(metadata={"data_key": "from"})
#     chat: Chat
#     text: Optional[str] = None
#
#     class Meta:
#         unknown = EXCLUDE
#
#
# @dataclass
# class UpdateObj:
#     update_id: int
#     message: Message
#
#     class Meta:
#         unknown = EXCLUDE
#
#
# @dataclass
# class GetUpdatesResponse:
#     ok: bool
#     result: List[UpdateObj]
#
#     Schema: ClassVar[Type[Schema]] = Schema
#
#     class Meta:
#         unknown = EXCLUDE
#
#
# @dataclass
# class SendMessageResponse:
#     ok: bool
#     result: Message
#
#     Schema: ClassVar[Type[Schema]] = Schema
#
#     class Meta:
#         unknown = EXCLUDE
