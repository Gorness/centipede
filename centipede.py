import os

for media, directories, files in os.walk(os.getcwd()):
    if os.path.basename(media) == 'Media':
        photos_moved = 0
        for photo_folder in directories:
            photo_folder_path = os.path.join(media, photo_folder)

            # 1. each photo folder contains a full photo and some thumbnail images
            # photo_list lists all these files, usually 4 per photo_folder
            photo_list = os.listdir(photo_folder_path)

            # 2. large photos have names that match the photo_folder
            large_photos_list = [photo for photo in photo_list if photo_folder in photo]

            # Some "Media" folders don't actually contain any subfolders with photos
            # their output is an empty list. So our list must not be empty
            if large_photos_list:
                photo = large_photos_list[0]
                photo_old_path = os.path.join(photo_folder_path, photo)
                photo_new_path = os.path.join(media, photo)
                os.rename(photo_old_path, photo_new_path)
                photos_moved += 1

        if photos_moved > 0:
            print(media)
            print(f"Moved {photos_moved} photos to the Media folder")