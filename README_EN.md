<h1 align="center">MusicDownload</h1>

<p align="center">
  🇺🇸 <a href="./README_EN.md">English</a> | 🇨🇳 <a href="./README.md">简体中文</a>
</p>

<p align="center">
<a href="https://peps.python.org/pep-0719"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/musicdl">
</a>
 <a href="https://pypi.org/project/musicdl"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/musicdl">
</a>
 <a href="https://github.com/yss161/musicDownload/releases"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/yss161/musicDownload"></a>
 <a><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/yss161/musicDownload?style=flat"></a>
 <a><img alt="GitHub forks" src="https://img.shields.io/github/forks/yss161/musicDownload?style=flat"></a>
 <a><img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/yss161/musicDownload/total"></a>
 <a><img alt="GitHub watchers" src="https://img.shields.io/github/watchers/yss161/musicDownload?style=flat"></a>

</p>

The Ultimate Music Downloader: Supports lossless audio downloads, batch downloading, one-click downloads, and playlist downloads.

Aggregates **57 music sources** for search and download: major Chinese platforms (Kuwo, Kugou, QQ Music, NetEase Cloud Music, Migu), international platforms (Spotify, TIDAL, YouTube Music, Deezer), aggregator mirror sites such as GD Music Station, and audiobook sources like Ximalaya.

## ✨ What's New in This Version

- **More music sources**: selectable sources expanded from 17 to 57. The source list is read dynamically from the installed musicdl package — new sources from future musicdl upgrades require no code changes
- **Source name translation**: all sources are shown with Chinese names; results from aggregator sources (GD Music Station, TuneHub, etc.) are additionally labeled with the real upstream platform, e.g. `TuneHub(NetEase)`
- **Dark mode**: one-click toggle 🌙/☀️ at the top right; the window, dialogs and context menus are all themed, and your preference is remembered
- **Settings persistence**: selected sources, results-per-source limit, save directory, auto-download toggle, search mode and theme are all saved automatically to `musicdownload_config.json` and restored on the next launch
- **Bug fixes**: fixed the "🚀 Auto-download all after search" toggle not working on newer PySide6 versions; fixed invisible labels when the system is in dark mode

### Screenshots:

<table align="center" border="0" cellpadding="10">

  <tr>
    <td align="center">
      <img src="images/4.png" width="600"><br>
      <b>New UI (Light) — 57 selectable music sources</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="images/5.png" width="600"><br>
      <b>Dark Mode</b>
    </td>
  </tr>
</table>

### Settings Auto-Save:

All settings (selected sources, results-per-source limit, save directory, auto-download toggle, search mode, dark mode) are saved automatically to `musicdownload_config.json` next to the program and restored on the next launch.

### Run Example：

```bash
# Python 3.13+ required (verified on 3.14)
git clone https://github.com/yss161/musicDownload.git
cd musicDownload
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python musicdownload.py 
```

### Run Release Example：

```
# Python 3.13+ required (verified on 3.14)
git clone https://github.com/yss161/musicDownload.git
cd musicDownload
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# If You Is Windows , Run make_release.bat
.\make_release.bat

# If You Is Linux、MacOS , Run make_release.sh
bash make_release.sh
```

## 📌 Original Projects & Acknowledgements

This project is derived from the following open-source projects. Many thanks to the original authors:

- **GUI base**: [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) (extended with source selection persistence, source name translation, dark mode, etc.)
- **Core search/download library**: [CharlesPikachu/musicdl](https://github.com/CharlesPikachu/musicdl) (the original GUI was based on [musicdlgui.py](https://github.com/CharlesPikachu/musicdl/blob/master/examples/musicdlgui/musicdlgui.py))
