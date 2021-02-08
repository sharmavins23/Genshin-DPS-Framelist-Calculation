from CharacterAbstract import Character  # Abstract parent class


class Zhongli(Character):

    def __init__(self, levelTuple=(1, 20), constellation=0, talentTuple=(1, 1, 1)):

        super.__init__(levelTuple, constellation, talentTuple)

        # Calculate base stats on the level passed in
        self._calculateBaseStatsOnLevel()

    def _calculateBaseStatsOnLevel(self):

        if self.currentLevel == 1 and self.maxLevel == 20:
            # Level is 1/20
            self._baseHP = 1144
            self._charBaseATK = 20
            self._baseDEF = 57
            self._baseGeoDMGBonus = 0
        elif 1 < self.currentLevel <= 20 and self.maxLevel == 20:
            # Anywhere from 1 to 20-, smooth to 20-
            self._baseHP = 2967
            self._charBaseATK = 51
            self._baseDEF = 67
            self._baseGeoDMGBonus = 0
        elif self.currentLevel == 20 and self.maxLevel == 40:
            # Level is 20/40, or 20+
            self._baseHP = 3948
            self._charBaseATK = 67
            self._baseDEF = 198
            self._baseGeoDMGBonus = 0
        elif 20 < self.currentLevel <= 40 and self.maxLevel == 40:
            # Anywhere from 20 to 40-, smooth to 40-
            self._baseHP = 5908
            self._charBaseATK = 101
            self._baseDEF = 297
            self._baseGeoDMGBonus = 0
        elif self.currentLevel == 40 and self.maxLevel == 50:
            # Level is 40/50, or 40+
            self._baseHP = 6605
            self._charBaseATK = 113
            self._baseDEF = 332
            self._baseGeoDMGBonus = 0.072
        elif 40 < self.currentLevel <= 50 and self.maxLevel == 50:
            # Anywhere from 40 to 50-, smooth to 50-
            self._baseHP = 7599
            self._charBaseATK = 130
            self._baseDEF = 382
            self._baseGeoDMGBonus = 0.072
        elif self.currentLevel == 50 and self.maxLevel == 60:
            # Level is 50/60, or 50+
            self._baseHP = 8528
            self._charBaseATK = 146
            self._baseDEF = 428
            self._baseGeoDMGBonus = 0.144
        elif 50 < self.currentLevel <= 60 and self.maxLevel == 60:
            # Anywhere from 50 to 60-, smooth to 60-
            self._baseHP = 9533
            self._charBaseATK = 163
            self._baseDEF = 479
            self._baseGeoDMGBonus = 0.144
        elif self.currentLevel == 60 and self.maxLevel == 70:
            # Level is 60/70, or 60+
            self._baseHP = 10230
            self._charBaseATK = 175
            self._baseDEF = 514
            self._baseGeoDMGBonus = 0.144
        elif 60 < self.currentLevel <= 70 and self.maxLevel = 70:
            # Anywhere from 60 to 70-, smooth to 70-
            self._baseHP = 11243
            self._charBaseATK = 192
            self._baseDEF = 564
            self._baseGeoDMGBonus = 0.144
        elif self.currentLevel == 70 and self.maxLevel == 80:
            # Level is 70/80, or 70+
            self._baseHP = 11940
            self._charBaseATK = 204
            self._baseDEF = 599
            self._baseGeoDMGBonus = 0.216
        elif 70 < self.currentLevel <= 80 and self.maxLevel == 80:
            # Anywhere from 70 to 80-, smooth to 80-
            self._baseHP = 12965
            self._charBaseATK = 222
            self._baseDEF = 651
            self._baseGeoDMGBonus = 0.216
        elif self.currentLevel == 80 and self.maxLevel == 90:
            # Level is 80/90, or 90+
            self._baseHP = 13662
            self._charBaseATK = 233
            self._baseDEF = 686
            self._baseGeoDMGBonus = 0.288
        elif 80 < self.currentLevel <= 90 and self.maxLevel == 90:
            # Anywhere from 80 to 90, smooth to 90
            self._baseHP = 14695
            self._charBaseATK = 251
            self._baseDEF = 738
            self._baseGeoDMGBonus = 0.288
