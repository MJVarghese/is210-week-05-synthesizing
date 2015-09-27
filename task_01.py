#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Task 1 File."""


import datetime


CURDATE = None


def get_current_date():
    """ This is to return the current day as a date object."""
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
