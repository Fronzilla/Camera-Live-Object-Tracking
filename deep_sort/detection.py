import numpy as np


class Detection:
    """
    Этот класс отвечает за обнаружение ограничивающего прямоугольника на одном изображении.
    Параметры
    ----------
    tlwh: array_like
        Ограничивающая рамка в формате `(x, y, w, h)`.
    уверенность: плавать
        Оценка достоверности детектора.
    особенность: array_like
        Вектор признаков, описывающий объект, содержащийся на этом изображении.

    Атрибуты
    ----------
    tlwh: ndarray
        Ограничивающая рамка в формате `(верхний левый x, верхний левый y, ширина, высота)`.
    уверенность: ndarray
        Оценка достоверности детектора.
    особенность: ndarray | NoneType
        Вектор признаков, описывающий объект, содержащийся на этом изображении.

    """

    def __init__(self, tlwh, confidence, cls, feature):
        self.tlwh = np.asarray(tlwh, dtype=np.float)
        self.confidence = float(confidence)
        self.cls = cls
        self.feature = np.asarray(feature, dtype=np.float32)

    def to_tlbr(self):
        """Convert bounding box to format `(min x, min y, max x, max y)`, i.e.,
        `(top left, bottom right)`.
        """
        ret = self.tlwh.copy()
        ret[2:] += ret[:2]
        return ret

    @staticmethod
    def tlbr_midpoint(box):
        """
        Finds midpoint of a box in tlbr format.
        """
        min_x, min_y, max_x, max_y = box
        midpoint = (int((min_x+max_x)/2), int((min_y+max_y)/2))
        return midpoint

    def to_xyah(self):
        """Convert bounding box to format `(center x, center y, aspect ratio,
        height)`, where the aspect ratio is `width / height`.
        """
        ret = self.tlwh.copy()
        ret[:2] += ret[2:] / 2
        ret[2] /= ret[3]
        return ret
