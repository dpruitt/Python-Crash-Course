class BowlingGame:

    def __init__(self):
        self.points = 0
        self.rolls = []
        self.frames = []
        self.current_frame = Frame()

    def roll(self, pins):
        self.points += pins
        if len(self.frames) and self.frames[-1].is_spare:
            self.points += pins

        self.current_frame.rolls.append(pins)
        self.rolls.append(pins)
        if len(self.rolls) % 2 == 0:
            frame_total = self.rolls[-1] + self.rolls[-2]
            if frame_total == 10:
                self.current_frame.is_spare = True
            self.frames.append(self.current_frame)
            self.current_frame = Frame()


    def score(self):
        return self.points


class Frame:

    def __init__(self):
        self.number = 1
        self.is_spare = False
        self.rolls = []