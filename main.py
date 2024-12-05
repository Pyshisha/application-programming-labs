import argparse

import cv2

from histogram import create_and_show_histogram
from inversion_image import invert_image
from reader import read_image


def parse_args() -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="Считать изображение из файла.")
    parser.add_argument('image_path', type=str, help="Путь к изображению.")
    parser.add_argument('save_dir', type=str, help="Директория для сохранения.")
    args = parser.parse_args()
    return args.image_path, args.save_dir


def main() -> None:
    """
        Главная функция программы. Обрабатывает аргументы командной строки и выводит результаты.
    """
    (image_path, save_dir) = parse_args()
    try:
        img = read_image(image_path)
        shape = img.shape
        print(f"Ширина изображения: {shape[1]}")
        print(f"Высота изображения: {shape[0]}")

        create_and_show_histogram(img)
        inv_img = invert_image(img)

        cv2.imwrite(f'{save_dir}/inverted_image.jpg', inv_img)
        cv2.imshow('Inverted Image', inv_img)
        cv2.imshow('Original Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
