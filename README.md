Для того что бы запустить скрипт сначала установите зависимости

`pip install -r requirements.txt`

после, скомпилируйте скрипт в .exe командой:

`pyinstaller --onefile text.py`
сам .exe файл будет лежать папкке `./dist`

перед тем как запустить ехешник надо проверить лежит ли с ним файл `config.yaml`
пример:`example-config.yaml`