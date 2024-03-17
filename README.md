# 1. 動作環境
以下を前提にしています。
- macOS(同じ準備をすれば、windowsでも動作はしました。)
- python3（verは11で確認しましたが、多少古くても動くと思います。）
- VScode
- OCRエンジンがある

# 2. 事前準備

## VScodeのインストール
公式サイトからインストールできます。
https://code.visualstudio.com/download

## OCRエンジンのインストール
macの場合はbrewがあれば、以下コマンドでインストールできます。
```
brew install tesseract
```

公式サイトからもインストール可能です。
windowsではこちらを使ってインストールし、動作しました。
https://gammasoft.jp/blog/tesseract-ocr-install-on-windows/

# 3. 利用手順
VScodeでこのリポジトリをクローンします。
（VScodeアイコンを右クリックして、New Windowを選択し、Clone RepositoryでこのリポジトリのURLを入力します。）
![img](readme_source/image.png 'clone_repository')

以下コマンドで必要ライブラリをインストールします。
```
pip install -r requirements.txt
```

prameta.pyを編集します。

以下コマンドでプログラムを起動します。
```
python3 keyword_detect.py
```


ターミナルにスクリーンショットを撮った中で、キーワードを含む画面のパスが表示されるので、確認しに行きます。
![Alt text](image.png)