from PIL import Image

if __name__ == '__main__':

    image = Image.new('1', (960, 540), 1)

    with open('DS3.txt', 'r') as f:
        for line in f:
            x, y = [int(t) for t in line.split()]
            image.putpixel((x, y), 0)

    image.save('output.' + 'png')
    image.close()
