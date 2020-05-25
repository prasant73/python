# def jpeg_res(filename):
#    """"This function prints the resolution of the jpeg image file passed into it"""

#    # open image for reading in binary mode
#    with open(filename,'rb') as img_file:

#        # height of image (in 2 bytes) is at 164th position
#        img_file.seek(163)

#        # read the 2 bytes
#        a = img_file.read(2)

#        # calculate height
#        height = (a[0] << 8) + a[1]

#        # next 2 bytes is width
#        a = img_file.read(2)

#        # calculate width
#        width = (a[0] << 8) + a[1]

#    print("The resolution of the image is",width,"x",height)

# jpeg_res("img.jpg")



from PIL import Image
import base64
import json
 # My image is a 200x374 jpeg that is 102kb large
def print_img_details(img, res1, res2):
    d = {}
    foo = Image.open("img.jpg")
    foo = foo.resize((res1,res2),Image.ANTIALIAS)
    # foo.save("img2.jpg",quality=95)
    foo.save(img,optimize=True,quality=95)
    with open(img, "rb") as imageFile:
        st = base64.b64encode(imageFile.read())
        # print (st)
    d['image64'] = st
    d['size'] = foo.size
    d['resolution'] = '160 x 300'
    # print(d)
    s = str(d)
    json_d = json.dumps(s)
    loaded_r = json.loads(json_d)
    return loaded_r

print(print_img_details("img.jpg",320,568))