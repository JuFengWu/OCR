
import pyttsx3

# 初始化
engine = pyttsx3.init()

engine.say('hello world')
engine.say('老師沒聲音，今天不想說話了(錯誤)')
# 朗讀一次
engine.runAndWait()

