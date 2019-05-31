import boto3
from boto3.s3.transfer import TransferConfig
import os
bucket_name = 'ec2-snapshot-interview'
s3 = boto3.client('s3')

def upload_to_s3(filename, path):
    print("size of the file is " ,os.path.getsize(path))
    if(os.path.getsize(path) < 1024 * 1024 * 5):
        s3.upload_file(path, bucket_name, filename)
        return "size is too small for multipart upload"
    multipart_upload = s3.create_multipart_upload(Bucket=bucket_name,Key=filename)
    print(multipart_upload)
    parts = upload_parts(multipart_upload["UploadId"], path, filename)
    result = complete(multipart_upload["UploadId"], parts, filename)
    print(result)
    return " none"


def upload_parts(mpu_id, path, filename):
    parts = []
    uploaded_bytes = 0

    with open(path, "rb") as f:

        i = 1
        while True:
            data = f.read(1024 * 1024 * 5)
            if not len(data):
                break
            part = s3.upload_part(
                    Body=data, Bucket=bucket_name, Key=filename, UploadId=mpu_id, PartNumber=i)
            parts.append({"PartNumber": i, "ETag": part["ETag"]})
            uploaded_bytes += len(data)
            print("{0} of {1} uploaded ({2:.3f}%)".format(
                uploaded_bytes, os.path.getsize(path),
                as_percent(uploaded_bytes, os.path.getsize(path))))
            i += 1
    return parts

def as_percent(num, denom):
  return float(num) / float(denom) * 100.0

def complete(mpu_id, parts, filename):
    result = s3.complete_multipart_upload(
        Bucket=bucket_name,
        Key=filename,
        UploadId=mpu_id,
        MultipartUpload={"Parts": parts})
    return result


def download(filename):
    s3.download_file(bucket_name, filename, "/Users/madya/Documents/GitHub/aws_interview_flask/flask_project/download_simulation/"+filename)
