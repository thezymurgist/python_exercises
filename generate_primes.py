'''This is a test project ot predict and list all prime numbers from 2 through a given limit greater than 2.
Created by The Zymurgist - Nov 2017'''

def gen_prime():
  from time import sleep
  print "Welcome to Generate Primes"
  sleep(1)
  limit = int(raw_input("Please set the upper limit for your list: "))
  if limit > 2:
    test_case = [2, 3, 5, 7]
    primes = test_case
    
    #test all the primes
    print "Calculating primes..."
    sleep(2)
    for i in range(2, limit + 1):
      if all(i % n != 0 for n in test_case):
        primes.append(i)
     
    #print the primes
    print "The prime numbers from 2 to %d are: " % (limit)
    for prime in primes:
      print prime
          
        
  else:
    print "Sorry, that limit won't work. Exiting Generate Primes..."
    return False

  
gen_prime()


#Possibly a more user friendly way to do this...
#This way the user at least sees visual output as the calculations are completed
def gen_prime():
  from time import sleep
  print "Welcome to Generate Primes"
  sleep(1)
  limit = int(raw_input("Please set the upper limit for your list: "))
  if limit > 2:
    test_case = [2, 3, 5, 7]
    
    #test and print the primes
    print "Calculating primes..."
    sleep(1)
	print "The prime numbers from 2 to %d are: " % (limit)
    for i in range(2, limit + 1):
      if all(i % n != 0 for n in test_case) or i in test_case:
        print i
     
  else:
    print "Sorry, that limit won't work. Exiting Generate Primes..."
    return False

  
gen_prime()

#Now experimenting with grabbing just the largest prime
def largest_prime():
	from time import sleep
	print "Welcome to the Largest Prime Calculator"
	sleep(1)
	limit = int(raw_input("Please set the upper limit of your range: "))
	if limit > 2:
		test_case = [2, 3, 5, 7]
	
		#find the highest prime
		print "Finding the highest prime from 2 to %d " % (limit)
		for i in reversed(range(2, limit + 1)):
			if all(i % n != 0 for n in test_case) or i in test_case:
				print "The highest prime is: %d \nExiting..." % (i)
				break
	else:
		print "Sorry, that limit won't work. Exiting Generate Primes..."
		return False

largest_prime()
