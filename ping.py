import config
import requests
import time
from datetime import datetime
import csv

statusfile = './status.txt'

def main():
	while True:
		statuses = []
		for page, content in config.urls.items():
			start = time.time()
			status = ""
			try:
				response = requests.get(page)
				if not content or content in response.text:
					status = 'OK'
				else:
					status = 'WORNING'	
			except requests.exceptions.RequestException as e: 
				status = 'DOWN'
			end = time.time()
			statuses.append([page, datetime.now(), end - start, status ])

		with open(config.logfile, 'a') as csvfile:
			csvwriter = csv.writer(csvfile)
			for logline in statuses:
				csvwriter.writerow(logline)

		with open(statusfile, 'w') as file:
			csvwriter = csv.writer(file)
			for logline in statuses:
				csvwriter.writerow(logline)

		time.sleep(config.wait)			

if __name__ == "__main__":
	main()