# coding=utf-8
# ディスコード用パッケージのインポート
import discord
# リスト内の単語をランダムで呼び出す場合に使用するパッケージ
import random
# text-to-speach用パッケージ。ざっくりいうとテキストを音声に変換してくれる
from gtts import gTTS

client = discord.Client()

# ランダムで読み上げる際に必要なリストの定義。コンマで区切る
random_contents=["ひまそうなねろ","ねろねろねろ","ねろそうなひま","パワき","ぱ、パワ・・・パワーキー","パワき持ってない癖に"]
shake_list = ["ひま","ねろ","パワキ","ぱわき","ネロ"]
# 読み上げない特定ワードの定義。特定のユーザに向けたアットマークと、URLが含むhttpの文字列
ng_word = ["@", "http"]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # ディスコードの会話する場所で以下のコマンド「!join」を打つとbotがボイスチャンネルへ入る
    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")
    # botを会話する場所から追い出すときのコマンド「!leave」
    elif message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")

    # ここから特定の文字列が叩かれたときに、特定のmp3ファイルを会話場に流し込むif分の連鎖
    # あんまりif分岐が多いと（1000個くらい？）実行速度に影響が出るかもだからそこはだれか改善してクレメンス
    elif message.content == "!sample1":
        # 以下の四行は、botが会話場に入っていない時にコマンドが打たれたときにbotが会話場に入っていないことをコメントする機能
        # ぶっちゃけ邪魔なので「!aachinu」にしかいれていない
        if message.guild.voice_client is None:
#            await message.channel.send("接続していません。")
             print("None")
             return
        # 「elif」の特定文字列を打ち込んだ時に、以下のmp3を流すコマンドを打ち込む。
        message.guild.voice_client.play(discord.FFmpegPCMAudio("sample1.mp3"))

    # 1個目に並んで、2個目以降は「elif」と「mp3」を流すメッセージの繰り返し
    elif message.content == "!sample2":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("sample2.mp3"))
    elif message.content == "!sample3":
        message.guild.voice_client.play(discord.FFmpegPCMAudio("sample3.mp3"))
# 「実装したけど、消して欲しいって言われたけど機能だけ奪ってプログラムに残しておきたい」
# そういうときは、コマンドの先頭に半角シャープ「#」をつけて「コメントアウト」する（こうすれば動かなくなる）
#   elif message.content == "!sample4":
#        message.guild.voice_client.play(discord.FFmpegPCMAudio("sample4.mp3"))

# 以下、shake_list=["ひま","ねろ","パワキ","ぱわき","ネロ"]を先ほど定義した
# shake_listリストに登録されている単語がテキスト内に存在する場合、特定のワードをrandom_contents内のワードでランダムに置き換えて読む
    elif [s for s in shake_list if s in message.content]:
#        if message.guild.voice_client is None:
#            await message.channel.send("接続していません。")
#            return
        for s in shake_list:
            if s in message.content:
                message.content = message.content.replace(s, random.choice(random_contents))
        # message.content = random.choice(random_contents)
        tts = gTTS(text=message.content, lang='ja')
        tts.save('./zzz.mp3')
        message.guild.voice_client.play(discord.FFmpegPCMAudio("zzz.mp3"))

# 上の置換と同様に、NGワードを含んでいる場合は、メッセージをNGワードに置き換えて読むようにする
# 例「@jawhfoafubhoafhaowufgaow」←この場合、「アットマークジェイダブリューエイチ・・・」とめっちゃ読むので
# 「アットマーク」だけを読むように変換してくれる。httpも同様
    elif [s for s in ng_word if s in message.content]:
#       if message.guild.voice_client is None:
#            await message.channel.send("接続していません。")
#            return
        for s in ng_word:
            if s in message.content:
                message.content = s
        # message.content = random.choice(random_contents)
        tts = gTTS(text=message.content, lang='ja')
        tts.save('./zzz.mp3')
        message.guild.voice_client.play(discord.FFmpegPCMAudio("zzz.mp3"))

    # 上記の特定コマンド以外はテキストを音声に変えて、プログラムを実行しているフォルダに
    # 「zzz.mp3」を生成して保存、そのmp3ファイルをディスコードに送って再生している。
    else:
        if message.guild.voice_client is None:
#            await message.channel.send("接続していません。")
             print("接続されていません")
             return
        tts = gTTS(text=message.content, lang='ja')
        tts.save('./zzz.mp3')
        message.guild.voice_client.play(discord.FFmpegPCMAudio("zzz.mp3"))
# 一番大事なんだけど、botのトークンを以下の「""」の間にコピーして保存する。
client.run("---ここにtokenをコピーしてね---")
