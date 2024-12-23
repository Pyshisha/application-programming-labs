import os
import csv


class ImagePathIterator:
    def __init__(self, annotation_file: str) -> None:
        self.annotation_file = annotation_file
        self.image_paths = self.__load_image_paths()
        self.limit = len(self.image_paths)
        self.counter = 0

    def __load_image_paths(self) -> list[str]:
        image_paths = []
        with open(self.annotation_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                abs_path = row[1].strip()
                image_paths.append(abs_path)
        return image_paths

    def __iter__(self) -> 'ImagePathIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            image_path = self.image_paths[self.counter]
            self.counter += 1
            if not os.path.exists(image_path):
                raise FileNotFoundError
            return image_path
        else:
            raise StopIteration
