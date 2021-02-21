import index  # Inserts the CWD into path
import header as h
# Base script tester for datatype CSV reading

zhongliInstance = h.Zhongli(
    levelTuple=(80, 90),
    constellation=0,
    talentTuple=(1, 1, 1)
)

print(zhongliInstance._baseHP)
