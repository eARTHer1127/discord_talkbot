# 必要なこと
- python環境の構築
- 必要なパッケージのインストール
- discord_bot用アカウントの登録
- bot用アカウントのbot用トークンの準備
- tokenをdiscord_play.pyへの反映

# オプション
- 特定ワード検出時に特定のmp3ファイル（効果音など）をプログラムが読み込めるようフォルダに準備
- sampleプログラムには「sample1.mp3」「sample2.mp3」「sample3.mp3」を読み込むように指定しているので用意していないとエラー出ると思います。

# 実行環境
```
$ python3 -V
Python 3.9.0
$ pip3 -V
pip 20.2.4 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
$ pip3 list show | grep gTTS
gTTS              2.2.2
$ pip3 list show | grep discord
discord.py        1.7.2
```

# インストールと実行
```
$ git clone https://github.com/eARTHer1127/discord_talkbot.git
$ cd discord_talkbot
$ python3 discord_play.py
```
