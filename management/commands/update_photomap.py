from photomap import settings
from photomap.models import ImageSpot
from django.core.management import BaseCommand
import json
import urllib
import sys
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# Show this when the user types help
	help = "My test command"

	def add_arguments(self, parser):
		parser.add_argument('--web_or_file', nargs='?',type=str, default="link")
		parser.add_argument('--workplace', type=str)
		parser.add_argument('--layer', type=str)
		parser.add_argument('--est', type=str)

 	def handle(self, *args, **options):
		web_or_file = options['web_or_file']
		layer = options['layer']
 		workplace = options['workplace']
		est = options['est']

		print(web_or_file)
		if web_or_file == "link":
			feature_link= "http://192.168.19.80/geoserver/" + workplace + "/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=" + workplace + ":" + layer + "&maxFeatures=50&outputFormat=application%2Fjson"
			response = urllib.urlopen(feature_link)

			try:
				layerlist = json.loads(response.read())
			except ValueError:
				print("Error occured: Link cannot be found! Please check supplied workplace and layer")
				sys.exit()
			with open('output.json', 'w') as outfile:
   				json.dump(layerlist, outfile)
		else:
			try:
				layerlist = json.load(open(web_or_file))
			except:
				print("File cannot be found. Try Again")
				sys.exit()

		for feature in layerlist["features"]:
			spot = ImageSpot()
			spot.establishment_type = est
			spot.name = feature["properties"]["NAME"]
			spot.geom = feature["geometry"]
			spot.save()