#RposimMachRep1.R

source("Rposim.R")

#global variables
UpRate = 1/1.0 # reciprocal of mean up time
RepairRate = 1/0.5 # reciprocal of mean repair time
NextID = 0 # next available ID number for MachineClass objects
TotalUpTime = 0.0 # total up time for all machines

MachineClass <- setRefClass("MachineClass",
fields = list(StartUpTime="numeric",ID="numeric"),
contains = "Process",
methods = list(
initialize = function()
{
    .self$StartUpTime <<- 0.0
    .self$ID <<- NextID
    NextID <<- NextID + 1
},
Run = function()
{
		while(1)
    {  
        # record current time, now(), so can see how long machine is up
        .self$StartUpTime <- now()
        # hold for exponentially distributed up time
        UpTime <- rexp(1,UpRate)
        yield_hold(.self, UpTime) # simulate UpTime
        TotalUpTime <<- TotalUpTime + now() - .self$StartUpTime
        RepairTime <- rexp(1,RepairRate)
        # hold for exponentially distributed repair time
        yield_hold(.self, RepairTime)
        #print MachineClass.TotalUpTime
    }
}))
main <- function()
{
	  initialize()
    # set up the two machine threads
    for(i in 1:2)
    {
        # create a MachineClass object
        M <- MachineClass()
        activate(M,M$Run()) # required
    }
    # run until simulated time 10000
    MaxSimtime = 10000.0
    simulate(MaxSimtime) # required
		
    paste("the percentage of up time was ", TotalUpTime/(2*MaxSimtime))
 }
 
 main()
