import sys
yy = int(sys.stdin.readline())
ifleap = lambda x: 1 if yy%4==0 and yy%100!=0 or yy%400==0 else 0
print(ifleap(yy))