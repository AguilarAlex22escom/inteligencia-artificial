import random
import os, shutil

def save_files(ctr):
    format = ".png"
    route = "shapes/triangle/"
    new_route = "shapes/dataset/"
    for file in range(260):
        circle_file = str(random.randint(0,3719)) + format
        saved_file = os.path.join(route,circle_file)
        print(circle_file)
        if os.path.isfile(saved_file) and not os.path.isfile(os.path.join(new_route, "triangle_" + circle_file)) and not os.path.isfile(os.path.join(new_route,circle_file)):
            shutil.copy(saved_file, new_route)
            new_file ="triangle_" + circle_file
            os.rename(new_route + circle_file, new_route + new_file)
            ctr += 1
    print(ctr)
save_files(0)
'''
circle files: 3720 ~= 24.85%
square files: 3765 ~= 25.15%
triangle files: 3720
star files: 365
'''
