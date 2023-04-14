from setuptools import setup

APP = ['main.py']
DATA_FILES =[('', ['helpers.py'])]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'img/icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}
setup(
    app=APP,
    name='Ølsalg',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)