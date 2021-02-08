from abc import ABC, abstractmethod


class Character(ABC):

    # Base stat calculation and initialization
    def __init__(self, levelTuple=(1, 20), constellation=0, talentTuple=(1, 1, 1)):

        # TODO: Input bounds checking and validation

        # Pass in (current, max) level values
        self.currentLevel, self.maxLevel = levelTuple

        self._baseHP = 0
        self.CurrentHP = 0
        self.MaxHP = 0

        self._charBaseATK = 0  # Just the base ATK stat of the character
        self._baseATK = 0  # ATK stat + weapon base ATK stat
        self.ATK = 0

        self._baseDEF = 0
        self.DEF = 0

        self._baseElementalMastery = 0
        self.ElementalMastery = 0

        self.MaxStamina = 240

        self._baseCritRate = 0.05
        self.CRITRate = 0
        self._baseCritDMG = 0.5
        self.CRITDMG = 0

        self._baseHealingBonus = 0
        self.HealingBonus = 0
        self._baseIncomingHealingBonus = 0
        self.IncomingHealingBonus = 0

        self._baseEnergyRecharge = 1
        self.EnergyRecharge = 0

        self._baseCDReduction = 0
        self.CDReduction = 0

        self._basePyroDMGBonus = 0
        self.PyroDMGBonus
        self._baseHydroDMGBonus = 0
        self.HydroDMGBonus
        self._baseDendroDMGBonus = 0
        self.DendroDMGBonus
        self._baseElectroDMGBonus = 0
        self.ElectroDMGBonus = 0
        self._baseAnemoDMGBonus = 0
        self.AnemoDMGBonus = 0
        self._baseCryoDMGBonus = 0
        self.CryoDMGBonus = 0
        self._baseGeoDMGBonus = 0
        self.GeoDMGBonus = 0
        self._basePhysicalDMGBonus = 0
        self.PhysicalDMGBonus

        self.Constellation = constellation
        self.TalentLevels = talentTuple

    @abstractmethod  # Have to extend with character-specific stat scaling
    def _calculateBaseStatsOnLevel(self):
        # TEMPLATE for creating other characters
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
