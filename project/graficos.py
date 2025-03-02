import polars as pl
import matplotlib.pyplot as plt

from data.constants import (
    databases,
    columns
)

class Graficos():

    def __init__(self):
        df = pl.read_csv(databases.CSV)

        self.years = columns.COLUMNS_YEARS

        self.df_brazil = (
            df.filter(pl.col("País") == "Brasil")
            .unpivot(
                index=[],
                on=self.years,
                variable_name="Ano",
                value_name="Imigrantes"
            )
        )

    def view_date(self):
        self.df_brazil
        return print(self.df_brazil)


    def __first_graphic(self):
        plt.plot(self.df_brazil['Ano'], self.df_brazil['Imigrantes'])
        plt.xticks([str(x) for x in range(1980, 2014, 5)])
        plt.yticks([int(y) for y in range(500, 3500, 500)])
        plt.show()


    def _graphic(self):
        self.__first_graphic()


if __name__ == '__main__':

    gf = Graficos()
    gf._graphic()
