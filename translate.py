import codecs

# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = open("source.txt","r").read()

# The target language
target = 'zh-CN'
#target = 'ar'

# Translates some text
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))

out = codecs.open('output.txt','w', encoding='utf-8')
out.write(u'Translation: {}'.format(translation['translatedText']))
out.close()
