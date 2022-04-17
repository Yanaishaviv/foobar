def solution(number_list):
	"""
	takes a list of numbers and funds the maximum product possible for them.
	the algorithm works as the following:
	each iteration i take the next number, and check whether it fits into one of the three -
	largest product (biggest one, signed)
	largest absolute product - the biggest one in it's absolute value
	or the closest to minus one - the negative number closest to minus one, or if it's not used, it's inverse.
	after i passed through all the numbers, I compare the largest absolute product divided the number closest
	to minus one with the largest overall product, and the larger one between them is the biggest product.
	:param number_list: list of numbers.
	:returns: the product as a string.
	"""
	largest_product = number_list[0]
	largest_abs_product = number_list[0]
	closest_to_minus_one = number_list[0] if number_list[0] != 0 else 1
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
	if closest_to_minus_one < 0\
		and closest_to_minus_one != largest_abs_product \
		and largest_abs_product < 0:

		largest_product = max(largest_abs_product / closest_to_minus_one, largest_product)
	# since we return this as a string, if it's a whole number it needs to be returned without the floating point.
	if int(largest_product) == largest_product:
		largest_product = int(largest_product)
	return str(largest_product)
