# pyqt-top-menu-bottom-widget
PyQt inner widget consists of menu bar and bottom widget(whatever the widget is) naturally.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-top-menu-bottom-widget.git --upgrade```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_top_menu_bottom_widget.topMenuBottomWidget import TopMenuBottomWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    slider = TopMenuBottomWidget()
    slider.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/148882447-83df7ecb-9a35-4d6b-8c66-a625d9ae60ef.png)
