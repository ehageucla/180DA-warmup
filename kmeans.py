# CREDIT: OPENCV kmeans.py on GITHUB
# found at https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py
# !/usr/bin/env python

'''
K-means clusterization sample.
Usage:
   kmeans.py
Keyboard shortcuts:
   ESC   - exit
   space - generate new distribution
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

#CREDIT: OPENCV gaussian_mix file
#function definition placed here, can be found at
#https://github.com/opencv/opencv/blob/master/samples/python/gaussian_mix.py
from numpy import random


def make_gaussians(cluster_n, img_size):
    points = []
    ref_distrs = []
    for _i in xrange(cluster_n):
        mean = (0.1 + 0.8 * random.rand(2)) * img_size
        a = (random.rand(2, 2) - 0.5) * img_size * 0.1
        cov = np.dot(a.T, a) + img_size * 0.05 * np.eye(2)
        n = 100 + random.randint(900)
        pts = random.multivariate_normal(mean, cov, n)
        points.append(pts)
        ref_distrs.append((mean, cov))
    points = np.float32(np.vstack(points))
    return points, ref_distrs


def main():
    cluster_n = 5
    img_size = 512

    # generating bright palette
    colors = np.zeros((1, cluster_n, 3), np.uint8)
    colors[0, :] = 255
    colors[0, :, 0] = np.arange(0, 180, 180.0 / cluster_n)
    colors = cv.cvtColor(colors, cv.COLOR_HSV2BGR)[0]

    while True:
        print('sampling distributions...')
        points, _ = make_gaussians(cluster_n, img_size)

        term_crit = (cv.TERM_CRITERIA_EPS, 30, 0.1)
        _ret, labels, _centers = cv.kmeans(points, cluster_n, None, term_crit, 10, 0)

        img = np.zeros((img_size, img_size, 3), np.uint8)
        for (x, y), label in zip(np.int32(points), labels.ravel()):
            c = list(map(int, colors[label]))

            cv.circle(img, (x, y), 1, c, -1)

        cv.imshow('kmeans', img)
        ch = cv.waitKey(0)
        if ch == 27:
            break

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
