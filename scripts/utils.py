#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fsize(path):
    with open(path, 'r') as file:
        n = len(file.read())
    return n
