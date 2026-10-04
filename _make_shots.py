# -*- coding: utf-8 -*-
"""生成 README 用界面截图（真实字体）：images/4.png 浅色、images/5.png 深色"""
import os
import sys

if "QT_QPA_PLATFORM" in os.environ:
    del os.environ["QT_QPA_PLATFORM"]

PROJ = os.path.dirname(os.path.abspath(__file__))
workdir = tempfile_dir = os.path.join(os.environ.get("TEMP", "/tmp"), "mdshot_readme")
os.makedirs(workdir, exist_ok=True)
os.chdir(workdir)

import importlib.util

spec = importlib.util.spec_from_file_location("musicdownload", os.path.join(PROJ, "musicdownload.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

w = mod.MusicDownloader()
w.resize(1200, 800)
# 截图里展示一个干净简洁的保存路径
w.save_dir_edit.setText(r"C:\Music")
w.grab().save(os.path.join(PROJ, "images", "4.png"))

w.dark_mode = True
w.apply_theme()
w.grab().save(os.path.join(PROJ, "images", "5.png"))

print("截图完成:", os.path.join(PROJ, "images", "4.png"), "和 5.png")
