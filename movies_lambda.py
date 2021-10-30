import json
import pandas as pd
import numpy as np
import boto3
from io import StringIO

def lambda_handler(event, context):
   
   print("A new file is uploaded to s3 bucket!")
   print(event['Records'][0]['s3']['object']['key'])
   return

#print body

client = boto3.client('s3')
csv_obj = client.get_object(Bucket='rawmoviescsv', Key='movies.csv')
csv_obj_body = csv_obj['Body']

csv_string = csv_obj_body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))


# to read the file and write comedy movies to processedmovies bucket
df_comedy = df[df.Genre=='comedy']
csv_buf = StringIO()
df_comedy.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
client.put_object(Bucket='processedmoviescsv', Body=csv_buf.getvalue(), Key='movies_comedy.csv') 


# count movies by genre and write result to stats bucket

df_genre  = df.groupby(["Genre"]).size().to_frame(name='count').reset_index()
		
csv_buf = StringIO()
df_genre.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
client.put_object(Bucket='statsmoviescsv', Body=csv_buf.getvalue(), Key='movie_genre.csv') 
