from BaseHandler import BaseHandler
from typing import Any, Optional


class Medic(BaseHandler):

    def handle(self, request: str) -> Optional[str]:
        if request == "Paciente":
            return f"El medico atiende al {request}"
        else:
            return super().handle(request)