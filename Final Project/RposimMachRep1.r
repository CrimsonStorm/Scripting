#RposimMachRep1.r

library(Rposim)
import random
#global variables
	set.seed(12345)
	TotalTime = c(0.0)
#class MachineClass(SimPy.Simulation.Process):
	UpRate = c(1/1.0) # reciprocal of mean up time
	RepairRate = c(1/0.5) # reciprocal of mean repair time
	NextID = c(0) # next available ID number for MachineClass objects
	TotalUpTime = c(0.0) # total up time for all machines
	#print(TotalUpTime)
	#def __init__(self): # required constructor
		#SimPy.Simulation.Process.__init__(self) # must call parent constructor
		# instance variables
		StartUpTime = 0.0 # time the current up period started
		 # ID for this MachineClass object
		#MachineClass.NextID += 1
Run = function(): # required constructor
		while 1:
			# record current time, now(), so can see how long machine is up
			StartUpTime = now()
			# hold for exponentially distributed up time
			UpTime = rexp(1,UpRate)
			yield_hold(UpTime) # simulate UpTime
			TotalUpTime += .now() - StartUpTime
			RepairTime = rexp(1,RepairRate)
			# hold for exponentially distributed repair time
			yield_hold(RepairTime)
			#print MachineClass.TotalUpTime
def main():
	#SimPy.Simulation.initialize() # required
    # set up the two machine threads
	for I in range(2):
        # create a MachineClass object
		#M = MachineClass()
		activate(Run()) # required
        # run until simulated time 10000
		MaxSimtime = 10000.0
	simulate(MaxSimtime) # required
	#print(MachineClass.TotalUpTime)
	GTotalTime += TotalUpTime
		
	print "the percentage of up time was", \
	TotalTime/(2*MaxSimtime)
