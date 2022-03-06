from time import time
import psutil
import os
from datetime import datetime

#  Implementation of Round Robin scheduling
class RoundRobin :
	#  Calculate waiting time of given process by using q time
	def find_waiting_time(self, processes, bt, wt, q, n) :
		pending_bt = [0] * n
		#  Loop controlling variable
		i = 0
		while (i < n) :
			pending_bt[i] = bt[i]
			i += 1
		
		#  Current time 
		process_time = 0
		#  work process indicator
		work = True
		#  Execute round robin process 
		while (work == True) :
			#  Set that initial no work at this time
			work = False
			#  Execute process one by one repeatedly
			i = 0
			while (i < n) :
				if (pending_bt[i] > 0) :
					work = True
					if (pending_bt[i] > q) :
						process_time += q
						pending_bt[i] -= q
					else :
						process_time = process_time + pending_bt[i]
						wt[i] = process_time - bt[i]
						pending_bt[i] = 0
					
				
				i += 1
			
		
	
	# This is calculating the average time by using given processes id,burst time and q  
	def find_avg_time(self, processes, burst_time, q, n) :
		#  Auxiliary space to store waiting time and turnaround time
		turnaround_time = [0] * n
		waiting_time = [0] * n
		# Resultant variable
		total_waiting_time = 0
		total_turnaround_time = 0
		# Loop control variable
		i = 0
		self.find_waiting_time(processes, burst_time, waiting_time, q, n)
		#  Calculate turnaround time 
		while (i < n) :
			#  Get turn around time for ith processes
			turnaround_time[i] = burst_time[i] + waiting_time[i]
			i += 1
		
		print(" (Process) (Burst Time) (Waiting Time) (Turn Around Time)", end = "")
		#  Display process ,burst time, waiting time, turn around time  
		#  And calculate the average waiting time and average turn around time
		i = 0
		while (i < n) :
			#  Calculate waiting time
			total_waiting_time += waiting_time[i]
			#  Calculate turnaround time 
			total_turnaround_time += turnaround_time[i]
			print("\n p", processes[i] ," \t\t", burst_time[i] ," \t\t", waiting_time[i] ," \t\t", turnaround_time[i], end = "")
			i += 1
		
		# Display Result 
		print("\n Average Waiting Time : ", (total_waiting_time / n))
		print(" Average Turn Around Time : ", (total_turnaround_time / n) )
		e_cpu_Util = psutil.cpu_times()
		e_Disk_Util = psutil.disk_usage('/')
		p1 = psutil.Process()
		e_Memory_Util = p1.memory_full_info()

def robin_main(data,n):
	
	p1 = os.getpid()
	print("process ID for Round Robin ",p1,datetime.now())
	obj = RoundRobin()
	# n = input("Number of processors: ")
	# n = int(n)
	# Process set
	processes = data[0]
	# Burst time of process set  
	burst_time = data[1]
	#  Assume that size of process and burst time is equal
	#  Get size
	n = len(processes)
	q = 2
	obj.find_avg_time(processes, burst_time, q, n)

if __name__ == "__main__":robin_main()