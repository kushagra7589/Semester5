from sklearn import metrics

def ARI(actual, predicted):
	return metrics.adjusted_rand_score(actual, predicted)

def AMI(actual, predicted):
	return metrics.adjusted_mutual_info_score(actual, predicted)

def NMI(actual, predicted):
	return metrics.normalized_mutual_info_score(actual, predicted)