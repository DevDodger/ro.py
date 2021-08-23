from typing import Optional
from datetime import datetime
from dateutil.parser import parse

from .utilities.shared import ClientSharedObject

from .bases.baseuniverse import BaseUniverse
from .bases.baseplace import BasePlace


class Presence:
    def __init__(self, shared: ClientSharedObject, data: dict):
        self._shared: ClientSharedObject = shared
        self._data: dict = data

        self.user_presence_type: int = data["userPresenceType"]
        self.last_location: str = data["lastLocation"]

        self.place: Optional[BasePlace] = data.get("placeId") and BasePlace(
            shared=shared,
            place_id=data["placeId"]
        )

        self.root_place: Optional[BasePlace] = data.get("rootPlaceId") and BasePlace(
            shared=shared,
            place_id=data["rootPlaceId"]
        )

        self.game_id: Optional[str] = data["gameId"]

        self.universe: Optional[BaseUniverse] = data.get("universeId") and BaseUniverse(
            shared=shared,
            universe_id=data["universeId"]
        )

        self.user_id: int = data["userId"]
        self.last_online: datetime = parse(data["lastOnline"])