import re

url = '/v1/collections/co.PgvF8SGWSvaNkggr5ZVxmA:sync'
p = re.compile('/v1/collections/[a-zA-Z0-9._-]+:sync$')

print(p.match(url))