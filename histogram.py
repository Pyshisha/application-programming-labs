import pandas
import matplotlib.pyplot as plt


def create_and_show_histogram(column: pandas.Series, xlabel_name: str, title_name: str) -> None:
    """
        Создает и выводит гистограмму.

        :param title_name:
        :param xlabel_name:
        :param df: DataFrame в формате pandas.DataFrame.
    """
    column.plot(kind='hist', bins=60, ylabel='Количесвто изображений', xlabel=xlabel_name,
                title=title_name)
    plt.show()
