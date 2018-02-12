import difflib
def recursive_change():
		a='hello'
		b='mellow'
		seq=difflib.SequenceMatcher(None,a,b)
		d=seq.ratio()*100
		print (d)
		return d
		
print (recursive_change())