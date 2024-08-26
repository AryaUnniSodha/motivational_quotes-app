# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\Arya U\\motivational_quotes'],
    binaries=[],
    datas=[
        ('C:\\Users\\Arya U\\motivational_quotes\\motivational_quotes', 'motivational_quotes'),  # Include your Django project directory
        ('C:\\Users\\Arya U\\motivational_quotes\\quotes', 'quotes'),  # Include your quotes app directory
        ('C:\\Users\\Arya U\\motivational_quotes\\quotes\\templates', 'quotes/templates'),  # Include your templates directory
        ('C:\\Users\\Arya U\\motivational_quotes\\manage.py', '.'),  # Include manage.py
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Arya U\\motivational_quotes\\myicon\\motivation.ico'],
)
