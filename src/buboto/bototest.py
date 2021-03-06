import boto3
import boto3.session
from boto3.dynamodb.conditions import Key


# # Create your own session
# my_session = boto3.session.Session()

# s3 = my_session.resource('s3')

# buckets = list(s3.buckets.all())
# print(buckets)


client = boto3.client('dynamodb')

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1985
    print(f"Movies from {query_year}")
    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title'])
