#!/usr/bin/env python3
# -*- coding: cp1252 -*-
def swap(x,y):
    temp = x
    x = y
    y = temp
    print("after x:",x,"\n","after y:",y)

x = int(input("Enter value of x"))
y = int(input("Enter value of y"))
if (x > y):
    swap(x,y)
else:
    print(x,y)


<a href="{% url 'article:comment-delete' comment.id %}" style="float:right">&#9747;</a>
