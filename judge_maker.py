def make_judge(grade,points):
    if min(points) <= 10 or points.count(30) >= 3:
        judgement = 3
    elif grade == 'D':
        judgement = 2
    else:
        judgement = 1
    return judgement