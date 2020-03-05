#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys

from invoke import task


@task
def styles(c):
    """Transpile less -> css"""
    c.run('lesscpy ./asciinema-theme-nord.less ./asciinema-theme-nord.css')


