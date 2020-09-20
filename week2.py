def minimumInserts(baseStr, targetStr):
	# A method that counts the minimum number of insertions required to make a substring of baseStr equal to targetStr
	# This method implements a brute-force approach
	# Compares the insertions required from different starting points of baseStr
	# Longest Common Subsequence does not always give the minimum number of insertion required

	insertArr = [] # Stores number of insertions required depending on the starting point of comparison of baseStr

	if len(baseStr) <= 0:
		return len(targetStr)
	else:
		for baseIndex in range(0, len(baseStr)):
			i = baseIndex # Will be used as a starting point of comparison/matching
			matchCount = 0 # Reset
			insertCount = 0 # Reset

			for targetIndex, targetChar in enumerate(targetStr):

				# If targetStr has not been completely matched with yet
				if matchCount < len(targetStr) and i <= len(baseStr) - 1:
					if baseStr[i] == targetChar:
						i += 1
						matchCount += 1

			# Subtract matchCount from length of targetStr to get the number of insertions
			insertCount = len(targetStr) - matchCount
					
			insertArr.append(insertCount)
			
		return min(insertArr)
