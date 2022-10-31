class Octopus:
    def __init__(self, level: int):
        self.is_flashing: bool = False
        self.energy_level: int = level

    def increase_level(self) -> bool:
        self.energy_level += 1

        # Only want to trigger other flashes if octopus has not flashed already
        if self.energy_level > 9 and not self.is_flashing:
            self.flash()
            return True

        return False

    def flash(self):
        self.is_flashing = True

    def finish_flash(self):
        if self.is_flashing:
            self.is_flashing = False
            self.energy_level = 0
