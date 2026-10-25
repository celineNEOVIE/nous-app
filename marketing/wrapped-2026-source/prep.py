from PIL import Image, ImageDraw, ImageFilter, ImageChops
import sys
IMG='../../images/'
def cutout(src, out, thr=232, outline=18):
    _o=Image.open(IMG+src).convert('RGBA'); im=Image.new('RGBA',_o.size,(255,255,255,255)); im.alpha_composite(_o); im=im.convert('RGB')
    w,h=im.size
    # mask of near-white
    px=im.load()
    nw=Image.new('L',(w,h),0); m=nw.load()
    for y in range(h):
        for x in range(w):
            r,g,b=px[x,y]
            if (r+g+b)/3>thr: m[x,y]=255
    # flood from borders: use ImageDraw.floodfill on a copy
    ff=nw.copy()
    for x in range(0,w,4):
        for y in (0,h-1):
            if ff.getpixel((x,y))==255: ImageDraw.floodfill(ff,(x,y),128)
    for y in range(0,h,4):
        for x in (0,w-1):
            if ff.getpixel((x,y))==255: ImageDraw.floodfill(ff,(x,y),128)
    bg=ff.point(lambda v:255 if v==128 else 0)
    alpha=ImageChops.invert(bg).filter(ImageFilter.MinFilter(11)).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(0.8))
    rgba=im.convert('RGBA'); rgba.putalpha(alpha)
    bbox=alpha.getbbox(); rgba=rgba.crop(bbox); alpha=alpha.crop(bbox)
    pad=outline+6
    W,H=rgba.size[0]+2*pad, rgba.size[1]+2*pad
    a2=Image.new('L',(W,H),0); a2.paste(alpha,(pad,pad))
    dil=a2.filter(ImageFilter.MaxFilter(outline*2+1 if outline*2+1<=61 else 61)).filter(ImageFilter.GaussianBlur(1.2))
    res=Image.new('RGBA',(W,H),(255,253,248,0))
    white=Image.new('RGBA',(W,H),(255,253,248,255)); white.putalpha(dil)
    res=Image.alpha_composite(res,white)
    layer=Image.new('RGBA',(W,H),(0,0,0,0)); layer.paste(rgba,(pad,pad),rgba)
    res=Image.alpha_composite(res,layer)
    res.save('assets/'+out); print(out,res.size)
#cutout('1.jpg','mascot.png',thr=175,outline=16)
#cutout('5.webp','mascot_tax.png',thr=232,outline=20)
# Laurence portrait crop
p=Image.open(IMG+'3.jpg').convert('RGB')
p.crop((130,38,590,478)).resize((700,700),Image.LANCZOS).save('assets/laurence.jpg',quality=93)
cutout('6.webp','mascot_zen.png',thr=225,outline=18)
cutout('7.webp','mascot_france.png',thr=225,outline=18)
cutout('8.webp','mascot_money.png',thr=225,outline=18)
cutout('9.webp','mascot_summer.png',thr=225,outline=18)
cutout('10.png','mascot_phone.png',thr=225,outline=18)
