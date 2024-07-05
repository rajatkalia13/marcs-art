import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

def upload_to_s3(file_name, star-finder-solutions, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: star-finder-solutions
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    try:
        s3.upload_file(file_name, star-finder-solutions, object_name)
        print(f"File '{file_name}' uploaded successfully.")
        return True
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False

def upload_images_from_folder(C:\Users\rohit\Downloads\img\img, star-finder-solutions):
    """
    Upload all images from a folder to an S3 bucket

    :param folder_path: Folder containing the images
    :param bucket: Bucket to upload to
    """
    for root, dirs, files in os.walk(C:\Users\rohit\Downloads\img\img):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                object_name = os.path.relpath(file_path, folder_path)
                upload_to_s3(file_path, bucket, object_name)

if __name__ == "__main__":
    # Folder containing images
    folder_path = 'path/to/starfind_solutions'
    # Bucket name
    bucket_name = 'star-finder-solutions'
    
    # Upload the images
    upload_images_from_folder(C:\Users\rohit\Downloads\img\img, star-finder-solutions)
