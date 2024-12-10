import pandas
import pandas as pd


def read_csv(csv_path: str) -> pandas.DataFrame:
    """
        Создает DataFrame из csv файла.

        :param csv_path путь к файлу csv в формате str
        :return:  DataFrame в формате pandas.DataFrame
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        raise Exception(f"Ошибка при загрузке данных: {e}")
