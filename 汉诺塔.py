#!/usr/bin/env python
#coding=utf
def answer_z(x, y):#已知起始柱子与终点柱子求解空闲柱子
    all = ('A','B','C')
    for a in all :
        if a == x:
            continue
        if a == y:
            continue
        return a
def move_A_C(n,x,y):#在x柱子上有n层圆盘，求解移动到y柱子上的步骤
	z = answer_z(x,y)
	if n == 1:
		print '%s --> %s' %(x,y)
	else:
		move_A_C(n-1,x,z)
		print '%s --> %s' %(x,y)
		move_A_C(n-1,z,y)
move_A_C(10,'A','C')