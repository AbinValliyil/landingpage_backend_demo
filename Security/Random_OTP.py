import math, random 

def OTPgenerator() :
	digits_in_otp = "0123456789"
	OTP = ""

# for a 4 digit OTP we are using 4 in range
	for i in range(6) : 
		OTP += digits_in_otp [math.floor(random.random() * 10)] 

	return OTP

