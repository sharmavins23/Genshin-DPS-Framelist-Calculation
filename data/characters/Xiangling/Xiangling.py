import pandas
from ..CharacterAbstract import Character


class Xiangling(Character):

    def __init__(self, levelTuple=(1, 20), constellation=0, talentTuple=(1, 1, 1)):
        super().__init__(levelTuple, constellation, talentTuple)

        # Calculate base stats on the level passed in
        self._calculateBaseStatsOnLevel()

    def _calculateBaseStatsOnLevel(self):
        # Read data from CSV
        levelBaseStats = pandas.read_csv(
            "data/characters/Xiangling/levelBaseStats.csv")

        # Get the level mapping index
        levelMappingIndex, _ = super()._getLevelMappings()

        # Use the level mapping to scrape data from the csv
        self._baseHP = levelBaseStats["Base HP"][levelMappingIndex]
        self._charBaseATK = levelBaseStats["Base ATK"][levelMappingIndex]
        self._baseDEF = levelBaseStats["Base DEF"][levelMappingIndex]
        self._baseElementalMastery = levelBaseStats["Elemental Mastery"][levelMappingIndex]
        self._baseCritRate = levelBaseStats["CRIT Rate"][levelMappingIndex]
        self._baseCritDMG = levelBaseStats["CRIT DMG"][levelMappingIndex]
