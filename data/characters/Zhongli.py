from CharacterAbstract import Character  # Abstract parent class


class Zhongli(Character):

    def __init__(self, levelTuple=(1, 20), constellation=0, talentTuple=(1, 1, 1)):

        super.__init__(levelTuple, constellation, talentTuple)

        # Calculate base stats on the level passed in
        self._calculateBaseStatsOnLevel()

    def _calculateBaseStatsOnLevel(self):

        if self.currentLevel == 1 and self.maxLevel == 20:
            # Level is 1/20
            pass
        elif 1 <= self.currentLevel <= 20 and self.maxLevel == 20:
            # Anywhere from 1 to 20-, smooth to 20-
            pass
        elif self.currentLevel == 20 and self.maxLevel == 40:
            # Level is 20/40, or 20+
            pass
        elif 20 < self.currentLevel <= 40 and self.maxLevel == 40:
            # Anywhere from 20 to 40-, smooth to 40-
            pass
        elif self.currentLevel == 40 and self.maxLevel == 50:
            # Level is 40/50, or 40+
            pass
        elif 40 < self.currentLevel <= 50 and self.maxLevel == 50:
            # Anywhere from 40 to 50-, smooth to 50-
            pass
        elif self.currentLevel == 50 and self.maxLevel == 60:
            # Level is 50/60, or 50+
            pass
        elif 50 < self.currentLevel <= 60 and self.maxLevel == 60:
            # Anywhere from 50 to 60-, smooth to 60-
            pass
        elif self.currentLevel == 60 and self.maxLevel == 70:
            # Level is 60/70, or 60+
            pass
        elif 60 < self.currentLevel <= 70 and self.maxLevel = 70:
            # Anywhere from 60 to 70-, smooth to 70-
            pass
        elif self.currentLevel == 70 and self.maxLevel == 80:
            # Level is 70/80, or 70+
            pass
        elif 70 < self.currentLevel <= 80 and self.maxLevel == 80:
            # Anywhere from 70 to 80-, smooth to 80-
            pass
        elif self.currentLevel == 80 and self.maxLevel == 90:
            # Level is 80/90, or 90+
            pass
        elif 80 < self.currentLevel <= 90 and self.maxLevel == 90:
            # Anywhere from 80 to 90, smooth to 90
            pass
