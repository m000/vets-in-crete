#!/usr/bin/env python
'''Geocodes data from excel and dumps json.
'''

import argparse
from openpyxl import load_workbook

try:
	from apikeys import geocode_api_key
except ImportError:
	geocode_api_key = None

DEFAULTS = {
	'sheet': 'Crete',
	'outdir': 'json',
	'addrcols': 'B,C,D',
	'apikey': geocode_api_key,
}

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Geocode data from excel and dump json.')
	parser.add_argument('workbook', help='Excel workbook to process.')
	parser.add_argument('--sheet', default=DEFAULTS['sheet'], help='Sheet to process.')
	parser.add_argument('--address-columns', dest='addrcols', metavar='C1,C2...', default=DEFAULTS['addrcols'], help='Columns to concatenate and use as address for geocode lookups.')
	parser.add_argument('--api-key', dest='apikey', default=DEFAULTS['apikey'], help='API key to use for geocode lookups.')
	args = parser.parse_args()

	wb = load_workbook(args.workbook)
	sheet = wb.get_sheet_by_name(args.sheet)
	addrcols = args.addrcols.split(',')

	if args.apikey is None:
		raise Exception('No API key specified. Aborting.')

	print(sheet)
	print(addrcols)
	print(args.apikey)

