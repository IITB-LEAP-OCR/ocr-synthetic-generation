import argparse
import os
import re
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont

fontof={}
fontof['hindi']='fonts/Mangal.ttf'
fontof['gurumukhi']='fonts/Raavi.ttf'
fontof['tamil']='fonts/Latha.ttf'
fontof['telgu']='fonts/FontsFree-Net-32193833-3233-4b83-ae48-85d38c19c5fd.ttf'
fontof['urdu']='fonts/Jameel Noori Nastaleeq Regular.ttf'
fontof['odia']='fonts/Kalinga Regular.ttf'
fontof['malayalam']='fonts/Dyuthi-Regular.ttf'
fontof['kannada']='fonts/Tunga Regular.ttf'
fontof['gujarati']='fonts/Shruti Font.ttf'
fontof['bengali']='fonts/vrinda.ttf'
fontof['manipuri']='fonts/vrinda.ttf'
fontof['assamese']='fonts/vrinda.ttf'
fontof['sanskrit']='fonts/Mangal.ttf'
fontof['marathi']='fonts/Mangal.ttf'
fontof['nepali']='fonts/Mangal.ttf'
fontof['konkani']='fonts/Mangal.ttf'
fontof['dogri']='fonts/NotoSerifDogra-Regular.ttf'
fontof['maithili']='fonts/NotoSansTirhuta-Regular.ttf'
fontof['sindhi']='fonts/Lateef-Regular.ttf'
fontof['santali']='fonts/NotoSansOlChiki-VariableFont_wght.ttf'
fontof['bodo']='fonts/Bodo Amat.ttf'


# Function For Generating Synthetic Data White
def synthetic_data_white(xli,font,tename,word,output_path):
    fnt = ImageFont.truetype(font, 200)
    size_width, size_height = fnt.getsize(word)

    img1 = Image.new('RGB', (size_width, size_height), color = (255, 255, 255))
    img_h=290
    img_w=int(img_h/size_height*size_width)
    d1 = ImageDraw.Draw(img1)
    d1.text((0,0), word, font=fnt, fill=(0, 0, 0))
    img1=img1.resize((img_w,img_h))
    img1.save(os.path.join(output_path,f"{os.path.basename(tename).split('.')[0]}_word_{xli}.png"))

# Function For Refining Text Lines
def refine_text_line(line):
    regex = re.compile('[%*+-/<=>^|~#°]')
    if (regex.search(line) == None):
        return True
    else:
        return False


def main(args):

    font=fontof[args.language]
    file=args.input_file
    output_path=args.output

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    print('Starting')
    
    with open(file, 'r' , encoding="utf8") as f:
        tename = file.split(".")[0]
        all_words = []
        for xli,words in enumerate(f):
            all_words.append(words)
        
    all_words = list(map(lambda x:x.strip(),all_words)) #removes /n
    print('all words',all_words)
    wh_i=0
    for word in tqdm(all_words):
        wh_i+=1
        synthetic_data_white(wh_i,font,tename,word,output_path)
    print('Done')

def parse_args():
    parser = argparse.ArgumentParser(description="OCR Printed Data generator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input_file", type=str, default=None, help="path to the input file")
    parser.add_argument("-l", "--language", type=str, default=None, help="Name of the Language")
    parser.add_argument("-o", "--output", type=str, default='output', help="path to the output")
    
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
