#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError
    elif a + b < c or a + c < b or b + c < a:
        raise TriangleError
        
    if a == b and a == c and b == c: # first check if all sides are equal
        return 'equilateral'
    elif  a == b or a == c or b == c: # then check if any two sides are equal
        return 'isosceles'
    else:
        return 'scalene' # then we can conclude none is equal
    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
