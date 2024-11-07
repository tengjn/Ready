thre = 0.3
def iou():
    return

def nms(items):
    result = []
    sort(items, items.score)
    while(len(items) > 0):
        cmp = items.pop(0)
        result.append(cmp)
        for i in range(len(items)):
            if iou(items[i], cmp) > thre:
                items.pop(0)
    return result
