import boto3
import csv

l1=[]
client = boto3.client('s3')
response = client.list_buckets()
for i in response['Buckets']:
    l1.append(i['Name'])
print(l1)
with open('s3_detail.csv','w',newline='') as f: 
    fieldnames=['Name','Type','Path','Size','LastModified'] 
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for j in range(len(l1)):
        res=client.list_objects(Bucket=l1[j])
        print(res)
        print(res['ResponseMetadata']['RequestId'])
        last_modified= res['Contents'][0]['LastModified']
        last_modified=str(last_modified)
        last_modified = last_modified.replace(" ", "/")
        last_modified = last_modified.replace(",/", "_")
        for k in res['Contents']:
            obj_name = k['Key']
            obj_name = obj_name.replace("/", " ")
            obj_name = obj_name.split()[-1]
            print('Name=',obj_name,'|','Path=',k['Key'],'|',"Size=",k['Size'],"|",'Last Modified=',last_modified,'|','StorageClass=',k['StorageClass'])
            writer.writerow({
                'Name': obj_name,
                'Path': k['Key'],
                'Type': res['ResponseMetadata']['HTTPHeaders']['content-type'],
                'LastModified': last_modified,
                'Size': k['Size'],
            })


