# personal_color_analysis/color_extract.py

import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from skimage import io
from itertools import compress

class DominantColors:
    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RGB to BGR
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS, n_init=1)
        kmeans.fit(self.IMAGE)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

        print("Dominant Colors (BGR):", self.COLORS)
        print("Cluster Labels:", self.LABELS)

        # Convert BGR to RGB for better visualization
        self.COLORS_RGB = self.COLORS[:, ::-1]
        print("Dominant Colors (RGB):", self.COLORS_RGB)

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    # 가장 자주 나타난 색상 순서대로 목록 반환
    def getHistogram(self):
        numLabels = np.arange(0, self.CLUSTERS + 1)
        # 빈도수 테이블 생성
        (hist, _) = np.histogram(self.LABELS, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        colors = self.COLORS
        # 빈도수에 따라 내림차순 정렬
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        for i in range(self.CLUSTERS):
            colors[i] = colors[i].astype(int)
        # 파란색 마스크 제거
        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        return colors, hist

    def plotHistogram(self):
        colors, hist = self.getHistogram()
        # creating empty chart
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0
    
        # creating color rectangles
        for i in range(len(colors)):
            end = start + hist[i] * 500
            r, g, b = colors[i]
            # using cv2.rectangle to plot colors
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (int(r), int(g), int(b)), -1)
            start = end
    
        # display chart
        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors
