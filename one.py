
#!/opt/my-envs/training-melvin/bin/python3.6
import tk
import boto3
import sys
class DevNull:
    def write(self, msg):
        pass
sys.stderr = DevNull()
client = boto3.client('s3')
bucket_name = ('saikrish1')
#print('my_key_name', 'my_path_name', 'last_modified', 'content_type', 'content_length', sep=' ')
step = client.list_objects(Bucket= str(bucket_name))['Contents']
step = client.list_objects(Bucket= str(bucket_name))
for my_path in step:
    my_path_name = my_path['Key']
    print(my_path_name)
    my_key_name_string = my_path_name.split('/')
    my_key_name = my_key_name_string[0] + my_key_name_string[-1]
    response = client.get_object(
     Bucket = str(bucket_name),
     Key = str(my_path)
     )
    last_modified = response['ResponseMetadata']['HTTPHeaders']['LastModified']
    last_modified = last_modified.replace(" ", "/")
    last_modified = last_modified.replace(",/", "_")
    content_encoding = response['ResponseMetadata']['HTTPHeaders']['content-encoding']
    print(my_path,last_modified,content_encoding)
    