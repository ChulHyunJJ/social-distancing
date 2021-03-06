import json

def append_cluster(dic_jo, phase, xx, ys, kps):
    """Append the annotation based on its distance"""

    if ys[0] <= 10:
        dic_jo[phase]['clst']['10']['kps'].append(kps)
        dic_jo[phase]['clst']['10']['X'].append(xx)
        dic_jo[phase]['clst']['10']['Y'].append(ys)

    elif ys[0] <= 20:
        dic_jo[phase]['clst']['20']['kps'].append(kps)
        dic_jo[phase]['clst']['20']['X'].append(xx)
        dic_jo[phase]['clst']['20']['Y'].append(ys)

    elif ys[0] <= 30:
        dic_jo[phase]['clst']['30']['kps'].append(kps)
        dic_jo[phase]['clst']['30']['X'].append(xx)
        dic_jo[phase]['clst']['30']['Y'].append(ys)

    else:
        dic_jo[phase]['clst']['>30']['kps'].append(kps)
        dic_jo[phase]['clst']['>30']['X'].append(xx)
        dic_jo[phase]['clst']['>30']['Y'].append(ys)


def get_task_error(dd):
    """Get target error not knowing the gender, modeled through a Gaussian Mixure model"""
    mm = 0.046
    return dd * mm


def get_pixel_error(zz_gt):
    """calculate error in stereo distance due to 1 pixel mismatch (function of depth)"""

    disp = 0.54 * 721 / zz_gt
    error = abs(zz_gt - 0.54 * 721 / (disp - 1))
    return error


def open_annotations(path_ann):
    try:
        with open(path_ann, 'r') as f:
            annotations = json.load(f)
    except FileNotFoundError:
        annotations = []
    return annotations
