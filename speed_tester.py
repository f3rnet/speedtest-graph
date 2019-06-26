import speedtest
from time import sleep

speed = speedtest.Speedtest()


def speed_test(down_speed, up_speed):
	str(int(down_speed))[:3]
	str(int(up_speed))[:3]
	with open('down_speed_results.txt', 'a') as file:
		file.write(str(int(down_speed)))
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
	sleep(60)

