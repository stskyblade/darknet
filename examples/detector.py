# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

from __future__ import print_function

from optparse import OptionParser

import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python/'))

import darknet as dn
import pdb
import numpy as np
import cv2


IMG_PATH = '/home/demlution/data/extend/dataset/gt_marked_valid/d1ab13599be510f5c160d40555269461.jpg'


def imshow(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_img(img, title='title'):
    imshow(title, img)


def test(img_path=IMG_PATH):
    img = cv2.imread(img_path)

    dn.set_gpu(0)
    net = dn.load_net(
        b"gt_v2/gt.cfg", b'/home/demlution/data/extend/dataset/gt_v2_backup_v1/gt.backup', 0)
    meta = dn.load_meta(b"gt_v2/gt.data")
    r = dn.detect(
        net, meta, img_path.encode())

    for name, confidence, box in r:
        center_x, center_y, width, height = box
        top_left = (int(center_x - width / 2), int(center_y - width / 2))
        bottom_right = (int(center_x + width / 2), int(center_y + width / 2))

        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

    show_img(img)


def main(options):
    valid_file_path = '/home/demlution/github/darknet_v2/gt_v2/valid.txt'
    with open(valid_file_path, 'r') as f:
        text = f.read()

    img_path_list = text.split('\n')

    for path in img_path_list:
        test(path)
    return


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--dir", action="store", dest="dir", type='str')

    options, args = parser.parse_args()
    print('options', options)
    main(options)
