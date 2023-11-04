from BaseHandler import BaseHandler
from typing import Any, Optional


class Policeman(BaseHandler):

    def handle(self, request: str) -> Optional[str]:
        if request == "Ladron":
            return f"El policia persigue al {request}"
        else:
            return super().handle(request)