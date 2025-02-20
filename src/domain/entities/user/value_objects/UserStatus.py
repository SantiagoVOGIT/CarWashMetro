from enum import Enum


class UserStatus(Enum):

    ACTIVE = "ACTIVO"
    INACTIVE = "INACTIVO"
    SUSPENDED = "SUSPENDIDO"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
