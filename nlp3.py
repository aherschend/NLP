from pathlib import Path
import imageio
from wordcloud import WordCloud


text = Path('RomeoAndJuliet.txt').read_text()

mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap='prism', mask = mask_image, background_color='white')

#generate is how everything happens
wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

#can use stop words on the homework assignment

print("done")

