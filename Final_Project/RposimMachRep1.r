#RposimMachRep1.R

source("Rposim.R")


#global variables
#UpRate = 1/1.0 # reciprocal of mean up time
#RepairRate = 1/0.5 # reciprocal of mean repair time
#NextID = 0 # next available ID number for MachineClass objects
#TotalUpTime = 0.0 # total up time for all machines

globals <- NULL

MachineClass <- setRefClass("MachineClass",
fields = list(StartUpTime="numeric",ID="numeric"),
contains = "Process",
methods = list(
initialize = function()
{
    .self$StartUpTime <<- 0.0
    .self$ID <<- globals[1,3]
    globals[1,3] <<- globals[1,3] + 1
    callSuper()
},
Run = function()
{
		while(1)
    {  
    #print("top of machine loop")
        # record current time, now(), so can see how long machine is up
        .self$StartUpTime <- now()
        # hold for exponentially distributed up time
        UpTime <- rexp(1,globals[1,1])
        yield_hold(.self, UpTime) # simulate UpTime
        globals[1,4] <<- globals[1,4] + now() - .self$StartUpTime
        RepairTime <- rexp(1,globals[1,2])
        # hold for exponentially distributed repair time
        yield_hold(.self, RepairTime)
        ##print MachineClass.TotalUpTime
        #print("bottom of machine loop")
    }
}))
main <- function()
{
#print("top of main")
	  initialize(c(1/1.0, 1/0.5, 0, 0.0))
    # set up the two machine threads
    for(i in 1:2)
    {
        # create a MachineClass object
        M <- MachineClass()
        activate(M) # required
    }
    # run until simulated time 10000
    MaxSimtime = 100.0
    simulate(MaxSimtime) # required
		
    print(paste("the percentage of up time was ", globals[1,4]/(2*MaxSimtime)))
 }
 
 main()
