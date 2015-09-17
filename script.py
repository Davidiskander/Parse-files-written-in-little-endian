__author__ = 'davidiskander'

import struct
import datetime
import bitstring

i=0
j=0
HR = []
hrlst = []

def convert(timestamp):
	return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %I:%M:%S %p')

def binary_to_int(b):
	return struct.unpack('<i', b)[0] # read string as little endian integer

with open("999999999_hr_1441695601.skd", "rb") as f:
  buf = f.read()
bytes = map(ord, buf)
print "=========================================================\n" \
	  "Header: %s \n" \
	  "=========================================================" %bytes[0:15]

def invalid_r():
	HR[4:5] = ['Invalid']

def automatic_t():
	HR[5:6] = ['Automatic']

def manual_t():
	HR[5:6] = ['Manual']

def result_0():
	HR[6:7] = ['0 - Measurement succeeded']

def result_1():
	HR[6:7] = ['1 - Measurement was cancelled by the user']

def result_2():
	HR[6:7] = ['2 - Measurement was cancelled because no raw data was coming from the Pixart (no contact)']

def result_3():
	HR[6:7] = ['3 - Measurement was cancelled because it timed out (30s)']

def result_4():
	HR[6:7] = ['4 - Measurement was cancelled because the Pixart algorithm reported a bad state.']

def result_5():
	HR[6:7] = ['5 - Measurement was cancelled due to an initialization failure']

def result_6():
	HR[6:7] = ['6 - Measurement was cancelled by a system event (SMS message, screen turning on, etc.) ']

for HR in bytes:
	i += 1
	j += 16
	z = j + 16
	HR = bytes[j:z]

	if len(HR) != 0:
		sampledata = HR[0:4]
		binarydata = struct.pack('<BBBB', *sampledata)
		timestamp = binary_to_int(binarydata)
		time_result = convert(timestamp)

		if HR[4:5] == [0]:
			invalid_r()

		if HR[5:6] == [1] or [2]:
			automatic_t()

		elif HR[5:6] == [0]:
			manual_t()

		if HR[6:7] == [0]:
			result_0()

		if HR[6:7] == [16]:
			result_1()

		if HR[6:7] == [32]:
			result_2()

		if HR[6:7] == [48]:
			result_3()

		if HR[6:7] == [64]:
			result_4()

		if HR[6:7] == [80]:
			result_5()

		if HR[6:7] == [96]:
			result_6()

		print "(%s)\tTime:%s\tReading:%s    \tType: %s \tResult: %s" %(i, time_result, HR[4:5], HR[5:6], HR[6:7])
		hrlst.append(HR[4:5])
	else:
		break


