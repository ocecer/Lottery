# Import
import random
from numpy import random, sort
from pandas import DataFrame

# Games
"""
sayilal loto 6/49
Super loto 6/60
cilgin sayisal loto 8/90
on numara 20/80
"""


class Lottery:
    # Number generator for Lottery
    def getNumbers(self, _numbers, _outOf, _coupon_df, _numberOfColumns=1):
        self.numbers = _numbers
        self.outOf = _outOf
        self.coupon_df = _coupon_df
        self.numberOfColumns = _numberOfColumns

        # Create Lottery coupon
        # for iter in range(1, self.numberOfColumns + 1):
        for iter in range(self.numberOfColumns):
            selectedNumbers = sort(random.default_rng().choice(
                self.outOf, size=self.numbers, replace=False)+1).reshape(1, len(self.coupon_df.columns))

            if self.coupon_df.empty:
                # If df is empty, selected number is writing into df
                self.coupon_df.loc[iter] = selectedNumbers[0]
            else:
                # Eleminate possible duplicate entries
                for numbers in self.coupon_df.values.tolist()[:]:
                    if selectedNumbers.tolist()[0] != numbers:
                        self.coupon_df.loc[iter] = selectedNumbers[0]
                    else:
                        print(f"Duplicate")
                        continue

        # Return the Lottery coupon
        return self.coupon_df

    def six49(self, _numberOfColumns=1):
        self.numberOfColumns = _numberOfColumns

        six49_df = DataFrame(
            columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Num6"])
        six49_df.empty

        six49_df = self.getNumbers(6, 49, six49_df, self.numberOfColumns)

        return six49_df

    def six60(self, _numberOfColumns=1):
        self.numberOfColumns = _numberOfColumns

        six60_df = DataFrame(
            columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Num6"])
        six60_df.empty

        six60_df = self.getNumbers(6, 60, six60_df, self.numberOfColumns)

        return six60_df

    def eight90(self, _numberOfColumns=1):
        self.numberOfColumns = _numberOfColumns

        eight90_df = DataFrame(
            columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Num6", "Num7", "Num8"])
        eight90_df.empty

        eight90_df = self.getNumbers(8, 90, eight90_df, self.numberOfColumns)

        return eight90_df

    def twenty80(self, _numberOfColumns=1):
        self.numberOfColumns = _numberOfColumns

        twenty80_df = DataFrame(columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Num6", "Num7", "Num8", "Num9",
                                "Num10", "Num11", "Num12", "Num13", "Num14", "Num15", "Num16", "Num17", "Num18", "Num19", "Num20"])
        twenty80_df.empty

        twenty80_df = self.getNumbers(
            20, 80, twenty80_df, self.numberOfColumns)

        return twenty80_df

    # def custom(self, _numbers, _outOf, _numberOfColumns=1):
    #     self.numbers = _numbers
    #     self.outOf = _outOf
    #     self.numberOfColumns = _numberOfColumns

    #     self.getNumbers(self.numbers, self.outOf, self.numberOfColumns)


# # Lottery.getNumbers
# # lot1 = Lottery().six49(200)
# lot2 = Lottery().six60(1000)
# # lot3 = Lottery().eight90(2)
# # lot4 = Lottery().twenty80(2)

# # print(lot1)
# print(lot2)
# # print(lot3)
# # print(lot4)
