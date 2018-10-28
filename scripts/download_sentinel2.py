# This script downloads data by tile and can take a list of tiles to download
# Input parameters are username [2] and password [3] for ESA hub  and path to folder in which to store downloaded
# images [1]
# The tile properties are currently hardcoded in the script --> adapt this to enable flexible selection of search criteria

from collections import OrderedDict
from sentinelsat import SentinelAPI
from sys import argv


def download_products(targetfolder, user, password):


	# Create query and download files #

	# password is retrieved from command line argument, user name is currently hardcoded
	api = SentinelAPI(user, password)

	# can be a list of tile ids
	tiles = ['34PHV']


	# create dictionary with core keywords
	query_kwargs = {
			'platformname': 'Sentinel-2',
			'producttype': 'S2MSI1C',
			'relativeorbitnumber': '064',
			'date': ('20180301', '20180310')}

	print('Query arguments are:')
	for i in query_kwargs:
		print(i, ': ', query_kwargs[i])

	# create empty ordered dictionary in which to insert query result for each tile
	products = OrderedDict()

	# for each tile in 'tiles', copy the dictionary of core keywords from above (without tiles), insert the corresponding
	# tile id (or filename for data before Apr 2017),
	# then apply query using the modified dictionary, and finally update 'products' (appending query result)
	for tile in tiles:
		kw = query_kwargs.copy()
		# print(kw)
		kw['tileid'] = tile  # only works for products after 2017-03-31
		# kw['filename'] = '*_{}_*'.format(tile)  # products after 2016-12-01
		pp = api.query(**kw)
		products.update(pp)

	# download selected products
	print('Found', len(products), 'product(s).')
	api.download_all(products, directory_path = targetfolder)

	print("Downloaded " + str(len(products)) + " product(s).")


if __name__ == "__main__":
	download_products(argv[1], argv[2], argv[3])
