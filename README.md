# dynamic-parser

設定(ファイル)からプロパティ名や型情報を取得して、CSVやJSONなどの半構造化データを解析するアイデアです。
Pythonの勉強用でもあるので、しばらくはWIPで個人学習用に遊んでいます。

## Python Version

```
brew update
brew install pyenv

pyenv install 3.9.2
pyenv local 3.9.2
```

## Pythonの仮想環境

FYI
- [pip の constraints の正しい用途](https://qiita.com/methane/items/11219ceedb44c0ebcc75)
- [きたない requirements.txt から Pipenv への移行](https://www.kabuku.co.jp/developers/python-pipenv-graph)
    - Pipenvはpython製のOSSであり、最新のpythonのバージョン互換性がない場合があるのでお見送り

```
# first, create venv
python3 -m venv .venv
# second, always exec command!
source .venv/bin/activate
# first, always upgrade pip!
pip install -U pip
```

```
pip install -r requirements.lock
pip freeze | tee requirements.lock
```

```
deactivate
```


## Jupyter Notebook

[【初心者向け】Jupyter Notebookの使い方！インストール方法から解説](https://udemy.benesse.co.jp/development/python-work/jupyter-notebook.html)

```
jupyter notebook
```

## テスト方法

- unittestとpytestがある

```
cd test
python3 -m unittest
```

## TODO

- 便利ツールを導入する https://www.slideshare.net/aodag/python-172432039

> PEP 8では1行当たりに79文字という規約が設定されていますが、Djangoのコーディングスタイルには「1行あたり119文字」まで許容すると書いてあります。