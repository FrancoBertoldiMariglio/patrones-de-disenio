from BaseHandler import BaseHandler
from typing import Any, Optional


class Firefighter(BaseHandler):

    def handle(self, request: str) -> Optional[str]:
        if request == "Fuego":
            return f"El bombero apaga el {request}"
        else:
            return super().handle(request)