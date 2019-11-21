import os

for dire, direct, file in os.walk(os.getcwd()):
    if os.path.basename(dire) == 'Media':
        for photo_folder in direct:
            photo_where = os.path.join(dire, photo_folder)
            photo_list = os.listdir(photo_where)
            photo = list(filter(lambda x: photo_folder in x, photo_list))[0]
            photo_old_path = os.path.join(photo_where, photo)
            photo_new_path = os.path.join(dire, photo)
            os.rename(photo_old_path, photo_new_path)

print('succ')







#
