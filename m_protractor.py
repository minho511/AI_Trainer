from math import acos
import math
pi = 3.141592
# point = [(x1,y1), (x2,y2), (x3,y3)] 각 점은 p1, p2, p3
# protractor_point3는 세점이 이루는 각도 <p1,p2,p3 를 반환한다.
# 반환값은 (도) 단위
def protractor_point3(point):
    x1,x2,x3 = point[0][0],point[1][0],point[2][0]
    y1,y2,y3 = point[0][1],point[1][1],point[2][1]
    vector1 = (x1-x2, y1-y2)
    vector2 = (x3-x2, y3-y2)
    dist1 = (vector1[0]**2+vector1[1]**2)**0.5
    dist2 = (vector2[0]**2+vector2[1]**2)**0.5
    dot = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    angle = acos(dot/dist1/dist2)
    return angle*180//pi

def distance_point2(point):
    x1, x2 = point[0][0], point[1][0]
    y1, y2 = point[0][1], point[1][1]
    return ((x2-x1)**2+(y2-y1)**2)*0.5