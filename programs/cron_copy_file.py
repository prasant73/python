# import schedule
# import time
# from copy_file_yogitha import main

# count = 0

# while True:
# 	if count % 2 != 0:
# 		count += 1
# 		schedule.every().day.at("01:00").do(main,'It is 01:00')
# 	else:
# 		count += 1
# 		schedule.every().day.at("12:00").do(main,'It is 12:00')
# 	schedule.run_pending()
# 	time.sleep(60)


import sys
print(sys.argv)
if(sys.argv[1] == "-e"):
	sys.exit()
sys.argv.append(1)
print("-v" in sys.flags)
