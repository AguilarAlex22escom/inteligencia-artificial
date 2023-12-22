import cv2 as cv
import numpy as np, pandas as pd
import random, os, math
from matplotlib import pyplot as plt

# Second code
def create_dataset(path):
    shapes = ["circle", "triangle", "square", "star"]
    patterns = []
    images = os.listdir(path)
    for image_file in images:
        # for index in range(5):
            # random_shape = str(random.randint(0,3764))
            # shape_file = os.path.join(path,shape + random_shape + ".png")
        if image_file[-4:] == ".png":
    # First code
                # image = cv.imread(shape_file, cv.IMREAD_GRAYSCALE)
            image = cv.imread(os.path.join(path, image_file))
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            ret, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
            contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            cnt = contours[0] # cnt is from the first obtained contour.
            wrapper = cv.convexHull(cnt,returnPoints = False)
            deffects = cv.convexityDefects(cnt,wrapper)
            moments = cv.moments(cnt)
            hu_moments = cv.HuMoments(moments).flatten()
            '''
            x1, y1 = cnt[0,0]
            cv.drawContours(image,[cnt],-1, (44, 120, 200), 3)
            print("Hu-Moments of first contour:\n", hu_moments)
                cv.putText(image, 'Figure', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 0.6, (200, 120, 60), 2)
                cv.imshow("Hu-Moments", image)
                cv.waitKey(0)
                cv.destroyAllWindows()
            '''
            for shape in shapes:
                if shape in image_file:
                    patterns.append({
                                    "class_name" : shape,
                                    "h0" : hu_moments[0],
                                    "h1" : hu_moments[1],
                                    "h2" : hu_moments[2],
                                    "h3" : hu_moments[3],
                                    "h4" : hu_moments[4],
                                    "h5" : hu_moments[5],
                                    "h6" : hu_moments[6]})
    dataset = pd.DataFrame(patterns)
    print(dataset)
    return data
create_dataset("shapes/dataset/")