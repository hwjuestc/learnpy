#!/usr/bin/env python3
# coding=utf-8

from enum import Enum

Month = Enum('Month',('Jan','Feb'))

for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
