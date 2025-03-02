import polars as pl
import matplotlib.pyplot as plt
from data.constants import databases, columns

class Graficos:
    def __init__(self):
        df = pl.read_csv(databases.CSV)
        self.years = columns.COLUMNS_YEARS
        
        self.df_brazil = (
            df.filter(pl.col("País") == "Brasil")
            .unpivot(
                index=["País"],
                on=self.years,
                variable_name="Ano",
                value_name="Imigrantes"
            )
        )
        
        self.df_comp = (
            df.filter(pl.col("País").is_in(["Brasil", "Argentina"]))
            .unpivot(
                index=["País"],
                on=self.years,
                variable_name="Ano",
                value_name="Imigrantes"
            )
            .pivot(
                index="Ano",
                on="País",
                values="Imigrantes"
            )
            .sort("Ano")
        )


    def _base_config(self):
        """Configurações comuns para todos os gráficos"""
        plt.figure(figsize=(12, 6))
        plt.xlabel("Ano", fontsize=12)
        plt.ylabel("Número de Imigrantes", fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)


    def show_brazil(self):
        self._base_config()
        plt.title("Imigração do Brasil para o Canadá (1980-2013)", fontsize=14)
        plt.plot(
            self.df_brazil["Ano"],
            self.df_brazil["Imigrantes"],
            marker='o',
            linestyle='-',
            color='green'
        )
        plt.xticks(self.df_brazil["Ano"][::5])
        plt.tight_layout()
        plt.show()


    def show_comparison(self):
        self._base_config()
        plt.title("Comparação Brasil vs Argentina (1980-2013)", fontsize=14)
        
        plt.plot(
            self.df_comp["Ano"],
            self.df_comp["Brasil"],
            label="Brasil",
            marker='o',
            linestyle='-',
            color='blue'
        )
        
        plt.plot(
            self.df_comp["Ano"],
            self.df_comp["Argentina"],
            label="Argentina",
            marker='o',
            linestyle='-',
            color='orange'
        )
        
        plt.legend()
        plt.xticks(self.df_comp["Ano"][::5])
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":

    gf = Graficos()

    # gf.show_brazil()
    gf.show_comparison()
