# PROJECT IS GOING TO SUCK

# Global Variables
# TOTALRUNTIME = 0
# Get time in milliseconds
# FIRSTTIME = as.numeric(Sys.time())*1000 
# ThreadList = as.matrix()
# ProcessQueue = c(0)
# QueueLength = length(ProcessQueue)

# Bigmemory SharedData
# ResourceList = as.matrix()

source();


makeProcess <- (){

}

makeResource <-() {

}

## Initialize global variables to be used. (Not 100% sure if needed)
__init__ <- function(...){
# Make Threads
# Make Events

}

# Used to indicate how much time to allocate to a thread
yield_hold <- function(holdTime,X){
	TOTALRUNTIME = TOTALRUNTIME + holdTime
	nextRunTime = X[3] + holdTime
	X[3] = nextRunTime
	X[1] = 1

# Cause a thread to join a queue for a given resource and use if no other threads in queue
yield_request<- function(resource){
ProcessQueue = c(ProcessQueue,resource)


}

# Indicate that a thread is done using a resource allowing next thread to use the resource (Need bigmemory for this)
yield_release <-function(resource){

}

# Have a thread wait until awakened by some other thread.
yield_passivate <-function(){

}



# Mark a thread runnable when first created
activate <- function(X){
	X[1] = 0
}

# Awakens a previously-passivated thread.
reactivate <- function(X){
	X[1] = 0
}

# Cancels all the events associated with a previously-passivated thread.
cancel <- function(X){
	
}

# Do the simulation
simulate(untilTime){

while(TOTALRUNTIME < untilTIme){
	# Run each thread and get time
	
	for(i in threads){
		# Execute Run command in separate instances of R
		
	}
}



}