def padding1(img):
    import sys
    from PIL import Image

    list_im = ['vr.jpg',img,'vr.jpg']
    new_im = Image.new('RGB', (444,95)) #creates a new empty image, RGB mode, and size 444 by 95

    for elem in list_im:
        for i in xrange(0,444,95):
            im=Image.open(elem)
            new_im.paste(im, (i,0))
    new_im.save('test1.jpg')
