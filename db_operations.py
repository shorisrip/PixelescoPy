from models import *
import datetime

not_viewed = "not_viewed"
viewed = "viewed"

def is_table_empty():
    picture_list_query = Image.select()
    return not(picture_list_query.exists())


def populate_db_with_paths(files_matched):
    for file in files_matched:
        populate_db(file, "not_viewed")


def list_viewed():
    pass


def list_not_viewed():
    pictures_not_viewed = list(Image.select().where(Image.status==not_viewed).execute())
    file_paths = []
    for item in pictures_not_viewed:
        file_path = item.filepath
        file_paths.append(file_path)
    return file_paths


def mark_as_viewed(filepath):
    image_record = Image.get(Image.filepath==filepath)
    image_record.status = viewed
    image_record.save()
    image_record.viewed_date = datetime.datetime.now()
    image_record.save()


def mark_as_skipped():
    pass


def mark_as_not_viewed():
    pass


def populate_db(file_path, status):
    picture_entry = Image(filepath=file_path, status=status, viewed_date=None)
    picture_entry.save()


def is_not_viewed(filepath):
    # Optimization needed here
    image_record_query = Image.select().where(Image.filepath == filepath)
    if image_record_query.exists():
        image_status = Image.get(Image.filepath == filepath).status
        if image_status==not_viewed:
            return True
        else:
            return False
    else :
        status = not_viewed
        image_entry = Image(filepath=filepath, status=status,
                              viewed_date=None)
        image_entry.save()
        return True