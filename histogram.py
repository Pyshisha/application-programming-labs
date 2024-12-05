import numpy as np
import matplotlib.pyplot as plt


def create_and_show_histogram(img: np.ndarray) -> None:
    """
        Создает и выводит гистограмму.

        :param img: Изображение в формате numpy.ndarray.

    """
    colors = ('blue', 'green', 'red')
    shape = img.shape
    plt.figure(figsize=(10, 7))
    for i, color in enumerate(colors):
        lst = []
        for x in range(shape[0]):
            for y in range(shape[1]):
                lst.append(img[x, y, i])
        plt.subplot(3, 1, i + 1)
        plt.hist(lst, bins=128, color=color)
        plt.title(f'Гистограмма {color} канала')
        plt.xlabel('Интенсивность')
        plt.ylabel('Количество пикселей')
    plt.subplots_adjust(hspace=0.5)
    plt.show()
