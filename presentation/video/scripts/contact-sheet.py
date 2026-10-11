from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
p=Path(__file__).resolve().parents[1]
kind=sys.argv[1] if len(sys.argv)>1 else 'stills'
files=sorted((p/'out/review').glob(kind+'-*.png'))
w=640;h=360;cols=3
font=ImageFont.truetype(str(p/'fonts/SourceSans3-Regular.otf'),22)
im=Image.new('RGB',(cols*w,((len(files)+cols-1)//cols)*(h+40)),'#F4F5F7');d=ImageDraw.Draw(im)
for n,f in enumerate(files):
 x=n%cols*w;y=n//cols*(h+40);a=Image.open(f).convert('RGB');a.thumbnail((w,h));im.paste(a,(x,y));frame=int(f.stem.split('-')[-1]);d.text((x+16,y+h+7),f'{frame//30//60:02}:{frame//30%60:02}.{frame%30:02}  /  frame {frame}',font=font,fill='#0D2D44')
im.save(p/('out/contact-sheet.png' if kind=='beats' else 'out/static-compositions.png'))
