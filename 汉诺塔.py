#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def move_A_C(n,a,b,c):#在x柱子上有n层圆盘，求解移动到y柱子上的步骤
	if n == 1:
		print ('%s --> %s' %(a,c))
	else:
		move_A_C(n-1,a,c,b)
		print ('%s --> %s' %(a,c))
		move_A_C(n-1,b,a,c)
move_A_C(10,'A','B','C')