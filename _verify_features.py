# -*- coding: utf-8 -*-
"""离屏功能验证：源选择持久化 + 源名称翻译 + 深色模式。运行: venv/Scripts/python _verify_features.py"""
import os
import sys
import json
import tempfile

os.environ["QT_QPA_PLATFORM"] = "offscreen"

PROJ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ)

# 在临时目录运行，验证配置文件写入与加载，避免污染项目目录
workdir = tempfile.mkdtemp(prefix="mdtest_")
os.chdir(workdir)

import importlib.util

spec = importlib.util.spec_from_file_location("musicdownload", os.path.join(PROJ, "musicdownload.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

from PySide6.QtWidgets import QApplication
from musicdl.modules.utils.data import SongInfo

app = QApplication(sys.argv)

# ---- 实例 1：无配置文件，应为默认状态（浅色） ----
w1 = mod.MusicDownloader()
n_sources = len(w1.source_checkboxes)
labels = [cb.text() for cb in w1.source_checkboxes]
print(f"[1] 源勾选框数量: {n_sources}")
print(f"[1] 前 8 个标签: {labels[:8]}")
print(f"[1] 默认选中: {w1.get_selected_sources()}")
assert n_sources >= 50, f"源数量异常: {n_sources}"
assert w1.get_selected_sources() == ["KuwoMusicClient", "KugouMusicClient"]
assert w1.dark_mode is False
assert mod.CURRENT_THEME is mod.LIGHT_THEME

# ---- 翻译功能 ----
cases = {
    "普通源": (SongInfo(source="KuwoMusicClient"), "酷我音乐"),
    "聚合源+上游": (SongInfo(source="TuneHubMusicClient", root_source="netease"), "TuneHub(网易云)"),
    "未知源回退": (SongInfo(source="FooMusicClient"), "Foo"),
    "有声书源": (SongInfo(source="XimalayaMusicClient"), "喜马拉雅"),
    "GD聚合源": (SongInfo(source="GDStudioMusicClient", root_source="kugou"), "GD音乐台(酷狗)"),
}
for name, (info, expect) in cases.items():
    got = w1.translate_source(info)
    print(f"[2] 翻译[{name}]: {got} (期望 {expect})")
    assert got == expect, f"{name}: got {got}"

# ---- 修改设置 + 切换深色模式 ----
for cb in w1.source_checkboxes:
    cb.setChecked(cb.text() == "Spotify" or cb.text() == "酷狗音乐")
w1.spin_limit.setValue(33)
w1.check_auto_download.setChecked(True)
w1.on_toggle_theme()
assert w1.dark_mode is True
assert mod.CURRENT_THEME is mod.DARK_THEME
assert w1.btn_theme.text() == "☀️ 浅色模式"
w1.grab().save(os.path.join(PROJ, "_ui_dark.png"))

cfg_path = os.path.join(workdir, "musicdownload_config.json")
cfg = json.loads(open(cfg_path, encoding="utf-8").read())
print(f"[3] 配置文件内容: {json.dumps(cfg, ensure_ascii=False)}")
assert set(cfg["selected_sources"]) == {"SpotifyMusicClient", "KugouMusicClient"}
assert cfg["search_size_per_source"] == 33
assert cfg["auto_download_after_search"] is True
assert cfg["dark_mode"] is True

w1.deleteLater()

# ---- 实例 2：应恢复上次保存的选择（含深色模式） ----
w2 = mod.MusicDownloader()
print(f"[4] 实例2 恢复的选中源: {w2.get_selected_sources()}")
print(f"[4] 实例2 恢复的数量/自动下载/深色: {w2.spin_limit.value()} / {w2.auto_download_after_search} / {w2.dark_mode}")
assert set(w2.get_selected_sources()) == {"SpotifyMusicClient", "KugouMusicClient"}
assert w2.spin_limit.value() == 33
assert w2.auto_download_after_search is True
assert w2.dark_mode is True
assert mod.CURRENT_THEME is mod.DARK_THEME

# 切回浅色再截图
w2.on_toggle_theme()
assert w2.dark_mode is False
w2.grab().save(os.path.join(PROJ, "_ui_light.png"))

# 切回深色验证再次持久化
w2.on_toggle_theme()
cfg = json.loads(open(cfg_path, encoding="utf-8").read())
assert cfg["dark_mode"] is True

print("\n全部验证通过 ✅  配置文件位置:", cfg_path)
