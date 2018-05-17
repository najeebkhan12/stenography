import cv2

def convert_to_binary(text):
    binary = []
    binary.append(''.join(format(ord(x), 'b') for x in text))
    return binary

def encode_image(image, st):
    global len_msg
    count = 0
   
    for row in range(0, 23):
        for col in range(0, 23):
            binary = '{0:08b}'.format(image[row][col])   #formater for converting int to binary
            binary = list(binary)
            binary[7] = st[count]   
            image[row][col] = int(''.join(binary), 2)    #converts binary to decimal 
            count = count + 1
            if (count == len_msg):
                return image
           
def decode_img(image):
    message = []
    count = 0
    global len_msg
    for row in range(0, 23):
        for col in range(0, 23):
            binary = '{0:08b}'.format(image[row][col])
            binary = list(binary)
            message.append(binary[7])
            count = count + 1
            if (count == len_msg):                
                return message

def decode_binary_string(s):
    return ''.join(chr(int(s[i*7:i*7+7],2)) for i in range(len(s)//7))

image = cv2.imread('grayscale.jpg', 0)
image = cv2.resize(image, (24, 24), interpolation = cv2.INTER_AREA)
st = 'HelloWorld'
print 'Encoding message...'
msg = convert_to_binary(st)
msg = ''.join(str(e) for e in msg)
len_msg = len(msg)
encode_image(image, msg)
print 'Message Encoded in Image, File name is \'Encode.png\''
cv2.imwrite('encode.png', encode_image(image, msg))
print 'Decoding Image'
encode = cv2.imread('encode.png', 0)
msg = decode_img(encode)
msg = ''.join(msg)
print decode_binary_string(msg)
