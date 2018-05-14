import json
from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# 打印1949年的国家人口
for pop_dict in pop_data:
	if pop_dict['Year'] == '1949':
		country_name = pop_dict['Country Name']
		population = int(  # 将一个浮点数的小数丢掉，返回整数
			float(pop_dict['Value'])
		)
		code = get_country_code(country_name)
		if code:
			print(code + ': ' + str(population))
		else:
			print("ERROR -" + country_name)
