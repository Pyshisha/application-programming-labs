import numpy as np


def invert_image(img: np.ndarray) -> np.ndarray:
    """
       Инвертирует цвета изображения.

       :param img: Исходное изображение в формате numpy.ndarray.
       :return: Инвертированное изображение в формате numpy.ndarray.
    """
    shape = img.shape
    inv_img = img.copy()
    for i in range(shape[0]):
        for j in range(shape[1]):
            inv_img[i, j] = 255 - img[i, j]
    return inv_img
