import speedtest
from time import sleep
import datetime

speed = speedtest.Speedtest()


def speed_test(down_speed, up_speed):
	str(int(down_speed))[:3]
	str(int(up_speed))[:3]
	timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
	with open('down_speed_results.txt', 'a') as file:
		file.write('{} | {}'.format(str(int(down_speed)), timestamp))
		file.write('\n')
	file.close()
	with open('up_speed_results.txt', 'a') as file:
		file.write(str(int(up_speed)))
		file.write('\n')
	file.close()


while True:
	down_speed = speed.download()
	up_speed = speed.upload()
	speed_test(down_speed, up_speed)
	# rest in seconds before performing next test
	# current setting at 1 min is pretty short
	# recommend changing to higher setting for longer duration
	sleep(60)

