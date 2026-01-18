@echo off
pip uninstall printrgb -y
set "ver=1.1.1"
py -m build
pip install .\dist\printrgb-%ver%-py3-none-any.whl