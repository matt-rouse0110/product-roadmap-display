# -*- mode: python ; coding: utf-8 -*-
import sys # added line
from os import path # added line
site_packages = next(p for p in sys.path if 'site-packages' in p) # added line

block_cipher = None


a = Analysis(['dataParser.py'],
             pathex=['C:\\Users\\Desktop'],
             binaries=[],
             datas=[(path.join(site_packages,"pptx","templates"), "pptx/templates")],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='roadmap_presentation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
