from .base import Accessory


class RGBLight(Accessory):
    def set_state(self, state):
        return 1

    def get_status(self):
        return 0

    def set_brightness(self, brightness: float) -> None:
        pass

    def get_brightness(self) -> float:
        pass

    def set_hue(self, hue: float) -> None:
        pass

    def get_hue(self) -> float:
        pass

    def set_saturation(self, float) -> None:
        pass

    def get_saturation(self) -> float:
        pass
