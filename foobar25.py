# def solution(sw):
# 	"""
# 	takes a list of numbers and funds the maximum product possible for them.
# 	:param sw: list of numbers.
# 	:returns: the product as a string.
# 	"""
# 	product = 1
# 	last_negative_number = 0
# 	smallest_negative_number = 0
# 	for number in sw:
# 		if number > 0:
# 			product *= number
# 		elif number < 0:
# 			if last_negative_number != 0:
# 				product *= last_negative_number * number
# 				temp = max(number, last_negative_number, smallest_negative_number)
# 				if temp != 0:
# 					smallest_negative_number = temp
# 				else:
# 					smallest_negative_number = max(number, last_negative_number)
# 				last_negative_number = 0
# 			else:
# 				last_negative_number = number
# 	if last_negative_number != 0 and last_negative_number < smallest_negative_number:
# 		product /= smallest_negative_number
# 		product *= last_negative_number
# 	return str(product)
#
#
#
	

#
#
# def solution(sw):
# 	"""
# 	takes a list of numbers and funds the maximum product possible for them.
# 	:param sw: list of numbers.
# 	:returns: the product as a string.
# 	"""
# 	# product = 1 if sw.count(0) < 5 else 5
# 	product = 1
# 	temp_product = 1
# 	negative_numbers = []
# 	for i, number in enumerate(sw):
# 		if number == 0:
# 			sw.pop(i)
# 	for number in sw:
# 		if number > 1:
# 			product *= number
# 		elif number < 0:
# 			negative_numbers.append(number)
# 	if len(negative_numbers) %2 != 0:
# 		negative_numbers.sort()
# 		negative_numbers.pop()
# 	while temp_product <= 1 and len(negative_numbers) >= 2:
# 		for number in negative_numbers:
# 			temp_product *= number
# 		if temp_product <= 1:
# 			negative_numbers = negative_numbers[2:]
# 			temp_product = 1
# 	product *= temp_product
# 	return str(product)


def solution(sw):
	"""
	takes a list of numbers and funds the maximum product possible for them.
	:param sw: list of numbers.
	:returns: the product as a string.
	"""
	largest_product = sw[0]
	largest_abs_product = sw[0]
	closest_to_minus_one = sw[0] if sw[0] != 0 else 1
	for number in sw[1:]:
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


# def solution(sw):
# 	largest_product = sw[0]
# 	largest_abs_product = sw[0]
# 	closest_to_minus_one = 1/sw[0] if sw[0] != 0 else sw[0]
# 	for number in sw[1:]:
# 		in_abs_prod = False
# 		curr_prod = max(number * largest_product, number * largest_abs_product)
# 		if curr_prod > largest_product:
# 			largest_product = curr_prod
# 		if number > largest_product:
# 			largest_product = number
# 		if abs(number * largest_abs_product) > abs(largest_abs_product):
# 			largest_abs_product = number * largest_abs_product
# 			in_abs_prod = True
# 		if abs(number) > abs(largest_abs_product):
# 			largest_abs_product = number
# 			in_abs_prod = True
# 		if number < 0:
# 			if in_abs_prod:
# 				closest_to_minus_one = min(number, closest_to_minus_one)
# 			else:
# 				closest_to_minus_one = min(1/number, closest_to_minus_one)
# 	if 0 > closest_to_minus_one != largest_abs_product < 0:
# 		largest_product = max(largest_abs_product / closest_to_minus_one, largest_product)
# 	if int(largest_product) == largest_product:
# 		largest_product = int(largest_product)
# 	return str(largest_product)



assert solution([0, 0, -0.45]) == '0'