import cv2
import pandas


def fill_image_data(df: pandas.DataFrame) -> None:
    """
        Заполняет столбцы в шириной, высотой и глубиной изображений.

        :param df: DataFrame в формате pandas.DataFrame
    """
    width = []
    height = []
    depth = []
    for img_path in df['Absolute path']:
        try:
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            shape = img.shape
            width.append(int(shape[1]))
            height.append(int(shape[0]))
            depth.append(int(shape[2]) if len(shape) > 2 else 1)
        except:
            width.append(None)
            height.append(None)
            depth.append(None)

    df['Width'] = width
    df['Height'] = height
    df['Depth'] = depth


def fill_image_area(df: pandas.DataFrame) -> None:
    """
        Создает и заполняет столбец с площадью изображений.

        :param df: DataFrame в формате pandas.DataFrame
    """
    df['Area'] = df['Width'] * df['Height']

def filter_by_size(df: pandas.DataFrame, max_w: int, max_h: int) -> pandas.DataFrame:
    """
        Фильтрует изображения по заданной ширине и высоте.

        :param df: DataFrame в формате pandas.DataFrame
        :param max_w: Максимальная ширина в формате int
        :param max_h: Максимальная высота в формате int
        :return: Отфильтрованный DataFrame в формате pandas.DataFrame

    """
    return df[(df['Width'] <= max_w) & (df['Height'] <= max_h)]
