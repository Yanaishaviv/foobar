FIRST_INDEX = 0


def solution(number_list):
	"""
	takes a list of numbers and funds the maximum product possible for them.
	:param number_list: list of numbers.
	:returns: the product as a string.
	"""
	largest_product = number_list[FIRST_INDEX]
	largest_abs_product = number_list[FIRST_INDEX]
	closest_to_minus_one = number_list[FIRST_INDEX] if number_list[FIRST_INDEX] != 0 else 1
	for number in number_list[1:]:
		in_abs_prod = False
		curr_prod = max(number * largest_product, number * largest_abs_product)
		if curr_prod > largest_product:
			largest_product = curr_prod
		if number > largest_product:
			largest_product = number
		if abs(number * largest_abs_product) > abs(largest_abs_product):
			largest_abs_product = number * largest_abs_product
			in_abs_prod = True
		if abs(number) > abs(largest_abs_product):
			largest_abs_product = number
			in_abs_prod = True
		if number < 0:
			if in_abs_prod:
				closest_to_minus_one = min(number, closest_to_minus_one)
			else:
				closest_to_minus_one = min(1/number, closest_to_minus_one)
	if 0 > closest_to_minus_one != largest_abs_product < 0:
		largest_product = max(largest_abs_product / closest_to_minus_one, largest_product)
	if int(largest_product) == largest_product:
		largest_product = int(largest_product)
	return str(largest_product)
