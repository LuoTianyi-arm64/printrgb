#!/bin/bash
ver = 1.1.2
py -m build
pip uninstall printrgb -y
pip install .\dist\printrgb-${ver}-py3-none-any.whl
