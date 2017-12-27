import math

# Given coordinates of the first antennas:
x1, y1 = 10, 5

counter = 0

while counter >= 0:

	# Get the distance between each pair antenna from the user and parse the string input to float:
	distBt2Antennas = float(raw_input("Enter the distance between each pair antenna in meter: "))

	x2 = x1
	y2 = y1 + distBt2Antennas
	x3 = x1
	y3 = y2 + distBt2Antennas

	# Get the coordinate of the receiver from user:
	Rx, Ry = raw_input("Enter the coordinate of the receiver separated by space: ").split()

	# Get desired frequency from the user input:
	f = float(raw_input("Enter the radio frequency in Hz: "))

	# math.atan(x) -- (the inverse of the tan function) Return the arc tangent of x, in radians.
	# math.sin(x) -- Return the sine of x radians.
	# math.cos(x) -- Return the cosine of x radians.
	# math.tan(x) -- Return the tangent of x radians.
	# Sine, Cosine and Tangent:
	# sin = Opposite / Hypotenuse
	# cos = Adjacent / Hypotenuse
	# tan = Opposite / Adjacent

	def calculate_theta(x, y, distBt2Antennas):
	    r = math.sqrt((float(Rx) - x) * (float(Rx) - x) + (float(Ry) - y) * (float(Ry) - y))
	    theta = math.atan(r / distBt2Antennas)
	    return theta

	#  Speed of Radio Wave = 3 * pow(10,8)
	#  Phase Angle (radian) = 2 * pi * Frequency * Change of Time
	def beamforming(x, y, f, distBt2Antennas):
	    distance = distBt2Antennas * math.cos(calculate_theta(x, y, distBt2Antennas))
	    delay = distance / (3 * pow(10, 8))
	    phase = 2 * 3.1416 * f * delay
	    return delay, phase

	print "|+-------------------------------------+|"
	output1 = beamforming(x1, y1, f, distBt2Antennas)	  
	print "The delay of the first signal is", output1[0], "seconds."
	print "The phase shift of the first signal is", output1[1], "rad.\n"

	output2 = beamforming(x2, y2, f, distBt2Antennas)
	print "The delay of the second signal is", output2[0], "seconds."
	print "The phase shift of the second signal is", output2[1], "rad.\n"

	output3 = beamforming(x3, y3, f, distBt2Antennas)
	print "The delay of the third signal is", output3[0], "seconds."
	print "The phase shift of the third signal is", output3[1], "rad."
	print "|+-------------------------------------+|"

	counter += 1

	restart = raw_input("Would you like to restart the program? [Y/N]")	
	if restart in ("N", "n"):
		print "Exit the program. Goodbye~ \n"
		break
	elif restart not in ("Y", "y"):
		print "Invalid input. Program terminated. \n"
		break
	print "Restart the calculation: \n"




