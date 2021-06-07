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


## 疑問点

- dataclassとnamedtupleの使い分けは？
  - [Python3.7の新機能 Data Classes](https://qiita.com/massa142/items/6dbfeb88092dea4f95d8)
- 抽象型メンバーはなさそう
- mypyは1nestしか解析できないっぽい
  - [mypy: Correct way of type-annotating list of multiple types
](https://stackoverflow.com/questions/52544118/mypy-correct-way-of-type-annotating-list-of-multiple-types)
- 三項演算子: 条件式が真のときに評価される式 if 条件式 else 条件式が偽のときに評価される式
