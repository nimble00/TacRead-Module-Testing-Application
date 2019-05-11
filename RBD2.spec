# -*- mode: python -*-

block_cipher = None


a = Analysis(['RBD2.py'],
             pathex=['C:\\Users\\DELL\\Desktop\\RBD_dir\\Module_repo\\module_testing'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RBD2',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='rbd.ico')
