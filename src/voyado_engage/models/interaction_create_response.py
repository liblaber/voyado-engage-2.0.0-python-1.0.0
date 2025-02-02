# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .interaction_create_response_self import InteractionCreateResponseSelf


@JsonMap({"id_": "id", "self_": "self"})
class InteractionCreateResponse(BaseModel):
    """InteractionCreateResponse

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param self_: self_, defaults to None
    :type self_: InteractionCreateResponseSelf, optional
    """

    def __init__(self, id_: str = None, self_: InteractionCreateResponseSelf = None):
        if id_ is not None:
            self.id_ = id_
        if self_ is not None:
            self.self_ = self._define_object(self_, InteractionCreateResponseSelf)
