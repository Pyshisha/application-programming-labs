import argparse

from image_characteristics import filter_by_size, fill_image_data, fill_image_area
from histogram import create_and_show_histogram
from reader import read_csv


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Считать пути к изображениям из файла.")
    parser.add_argument('csv_path', type=str, help="Путь к аннотации.")
    args = parser.parse_args()
    return args.csv_path


def main() -> None:
    """
        Главная функция программы. Обрабатывает аргументы командной строки и выводит результаты.
    """
    try:
        df = read_csv(parse_args())

        del df['Image name']
        df['Width'] = 0
        df['Height'] = 0
        df['Depth'] = 0

        fill_image_data(df)
        print(df.head())
        df = df.dropna(subset=['Width', 'Height', 'Depth'])
        new_df = filter_by_size(df, 1000, 700)
        print("Отфильтрованный DataFrame")
        print(new_df)

        fill_image_area(df)
        df = df.sort_values(["Area"], ascending=True)
        print("Отcортированный по площади DataFrame")
        print(df)

        create_and_show_histogram(df["Area"], "Площадь", "Распределение площадей изображений")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
