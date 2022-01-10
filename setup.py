from setuptools import setup, find_packages

setup(
    name='pyqt-top-menu-bottom-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt inner widget consists of menu bar and bottom widget(whatever the widget is) naturally.',
    url='https://github.com/yjg30737/pyqt-top-menu-bottom-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)