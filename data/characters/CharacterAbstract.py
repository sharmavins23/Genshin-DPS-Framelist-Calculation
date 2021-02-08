from abc import ABC, abstractmethod


class Character(ABC):

    # Base stat calculation and initialization
    def __init__(self, levelTuple=(1, 20), constellation=0, talentTuple=(1, 1, 1)):
        # Pass in (current, max) level values
        self.currentLevel, self.maxLevel = levelTuple

        self._baseHP = 0
        self.MaxHP = 0

        self._charBaseATK = 0  # Just the base ATK stat of the character
        self._baseATK = 0  # ATK stat + weapon base ATK stat
        self.ATK = 0

        self._baseDEF = 0
        self.DEF = 0

        self._baseElementalMastery = 0
        self.ElementalMastery = 0

        self._baseCritRate = 0
        self.CRITRate = 0
        self._baseCritDMG = 0
        self.CRITDMG = 0

        self._baseEnergyRecharge = 0
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
        pass
