#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings')
    # 我们把上面一行替换为如下两行：，这样做的逻辑是，
    # 通过读取系统环境变量中TYPEIDEA_PROFILE来控制Django加载不同的setting文件
    # 以此达到开发环境使用develop.py这个配置、而线上环境使用product.py这个配置
    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
