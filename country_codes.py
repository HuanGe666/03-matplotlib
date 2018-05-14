from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
	"""根据国家名字查找国家代码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	# 没找到，返回None
	return None
