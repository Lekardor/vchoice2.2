# -*- mode: python -*-
import sys
sys.setrecursionlimit(5000)
block_cipher = None


a = Analysis(['test.py'],
             pathex=['D:\\软件工程\\UI\\vchoice2.2_source'],
             binaries=[],
             datas=[('stopwords','wordcloud')],
             hiddenimports=['sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils'],
             hookspath=[],
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
          name='test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='D:\\软件工程\\UI\\vchoice2.2_source\\image\\flash.ico')
