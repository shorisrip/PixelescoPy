from models import *
import datetime

not_viewed = "not_viewed"
viewed = "viewed"


def is_table_empty():
    """ Checks if table is empty"""
    picture_list_query = Image.select()
    return not(picture_list_query.exists())


def populate_db_with_paths(files_matched):
    """
    Adds initial entries for all paths and marks as not viewed
    :param files_matched: List of file paths you want to populate in db
    :return: None
    """
    for file in files_matched:
        populate_db(file, "not_viewed")


def list_viewed():
    pass


def list_not_viewed():
    """ List file paths not viewed"""
    pictures_not_viewed = list(Image.select().where(Image.status==not_viewed).execute())
    file_paths = []
    for item in pictures_not_viewed:
        file_path = item.filepath
        file_paths.append(file_path)
    return file_paths


def mark_as_viewed(file_path):
    """
    Marks image as viewed in db
    :param file_path: FIle path of image you want to mark viewed
    :return: None
    """
    image_record = Image.get(Image.filepath == file_path)
    image_record.status = viewed
    image_record.save()
    image_record.viewed_date = datetime.datetime.now()
    image_record.save()


def mark_as_skipped():
    pass


def mark_as_not_viewed():
    pass


def populate_db(file_path, status):
    """
    Adds entry or an image in db with desired status
    :param file_path: String File path of image you  want to add to db
    :param status: String status you want image to have
    :return: None
    """
    picture_entry = Image(filepath=file_path, status=status, viewed_date=None)
    picture_entry.save()


def is_not_viewed(file_path):
    """
    Checks if image is not viewed. Also, if image doesn't exist in db adds it
    :param file_path: String file path of image
    :return: Boolean
    """
    # Optimization needed here
    image_record_query = Image.select().where(Image.filepath == file_path)
    if image_record_query.exists():
        image_status = Image.get(Image.filepath == file_path).status
        if image_status == not_viewed:
            return True
        else:
            return False
    else:
        status = not_viewed
        populate_db(file_path, status)
        return True
