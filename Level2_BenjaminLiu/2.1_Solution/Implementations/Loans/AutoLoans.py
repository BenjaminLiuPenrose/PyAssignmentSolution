

# Exercise 2.2.4
# Create a fixed AutoLoan class. This should derive-from the appropriate base class(es)

# Exercise 2.2.4
class AutoLoan(Loan):
	def __init__(self, auto):
		if isinstance(auto, Car):
			self._auto=suto;
		else :
			self._auto=Car(face); # Implementation needed 	
			logging.error('The entered home does not belong to Car');