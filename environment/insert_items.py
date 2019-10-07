import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('kids_activity')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:
	batch.put_item(Item={
    	"category": "Cognitive",
    	"title": "Playgroud with bumba",
    	"partner": "Halu",
    	"detail":
        	[
            	{
                	"location": "Jakarta",
                	"comment": "Good for kids"
            	}
        	]
	})
	batch.put_item(Item={
    	"category": "Motoric",
    	"title": "Race with Crash Bandicot",
    	"partner": "Bunga Kembang",
    	"detail":
        	[
            	{
                	"location": "Tangerang",
                	"comment": "Tabrak - tabrakan"
            	}
        	]
	})
	batch.put_item(Item={
    	"category": "School",
    	"title": "Drawing with buba",
    	"partner": "CandyGuys",
    	"detail":
        	[
            	{
                	"location": "Jakarta Selatan",
                	"comment": "Gambarin aku dong kakak"
            	}
        	]
	})
	batch.put_item(Item={
    	"category": "Sensoric",
    	"title": "Swimming with Dolphin",
    	"partner": "Sea World",
    	"detail":
        	[
            	{
                	"location": "Bogor",
                	"comment": "lumba-lumba cuy!"
            	}
        	]
	})
