import numpy as np


def non_max_suppression(boxes, max_bbox_overlap, scores=None):
    """
    Suppress overlapping detections.
    Parameters
    ----------
    boxes : ndarray
        Array of ROIs (x, y, width, height).
    max_bbox_overlap : float
        ROIs that overlap more than this values are suppressed.
    scores : Optional[array_like]
        Detector confidence score.

    Returns
    -------
    List[int]
        Returns indices of detections that have survived non-maxima suppression.

    """
    if len(boxes) == 0:
        return []

    boxes = boxes.astype(np.float)
    pick = []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2] + boxes[:, 0]
    y2 = boxes[:, 3] + boxes[:, 1]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    if scores is not None:
        id_xs = np.argsort(scores)
    else:
        id_xs = np.argsort(y2)

    while len(id_xs) > 0:
        last = len(id_xs) - 1
        i = id_xs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[id_xs[:last]])
        yy1 = np.maximum(y1[i], y1[id_xs[:last]])
        xx2 = np.minimum(x2[i], x2[id_xs[:last]])
        yy2 = np.minimum(y2[i], y2[id_xs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[id_xs[:last]]

        id_xs = np.delete(
            id_xs, np.concatenate(
                ([last], np.where(overlap > max_bbox_overlap)[0])))

    return pick
