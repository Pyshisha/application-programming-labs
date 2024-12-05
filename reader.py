import cv2
import numpy as np


def read_image(image_path: str) -> np.ndarray:
    try:
        img = cv2.imread(image_path)
        return img
    except Exception as e:
        raise Exception(f"Ошибка при загрузке изображений: {e}")
