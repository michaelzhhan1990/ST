# -*- coding: utf-8 -*-
'''
n 》 0 或小于0 或=0 或 1
pow(x,n)=pow(x,n/2)* pow(x,n/2) * pow(x,n- n/2 *2)


'''
def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    isNegative = False
    if n < 0:
        isNegative = True
        n *= -1
    k = n / 2
    l = n - k * 2
    t1 = self.myPow(x, k)
    t2 = self.myPow(x, l)
    if isNegative == True:
        return 1 / (t1 * t1 * t2)
    else:
        return t1 * t1 * t2
