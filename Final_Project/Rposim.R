library(bigmemory)

#globals
pQ <- c()
fQ <- c()
data <- NULL

setClass("Process", slots=c(pid="numeric", data="big.matrix"),prototype=list(pid=0))

setClass("Resource", representation(n="numeric"))

# Initialize
initialize <- function()
{
    #initialize big memory object
    #data <<- as.big.matrix(d, type="double", backingfile="m.bin", descriptorfile="data.desc")
}

# Used to indicate how much time to allocate to a thread
yield_hold <- function(p, holdTime)
{
    data[p@pid][2] <- 1
	  data[p@pid][3] <- data[1][2] + holdTime
    data[p@pid][1] <- 1 
    while(data[p@pid][1] == 1)
    {
        #busy wait
    }
} 

# Cause a thread to join a queue for a given resource and use if no other threads in queue
yield_request <- function(resource)
{
    ProcessQueue = c(ProcessQueue,resource)


}

# Indicate that a thread is done using a resource allowing next thread to use the resource (Need bigmemory for this)
yield_release <- function(resource)
{

}

# Have a thread wait until awakened by some other thread.
yield_passivate <-function()
{

}

# Mark a thread runnable when first created
activate <- function(p, f)
{
    pQ <- c(pQ, p)
    fQ <- c(fQ, f)
}

# Awakens a previously-passivated thread.
reactivate <- function(X)
{

}

# Cancels all the events associated with a previously-passivated thread.
cancel <- function(X)
{
	
}

now <- function(X)
{
    data[1][2]  #current time
}

# Do the simulation
simulate(until)
{
    for (i in 1:length(pQ))
    {
        pQ[i]@pid <- i
        #add a row to big.matrix
        #data[i][1] <- 0
        #data[i][2] <- 0
        #data[i][3] <- 0
        #open a new terminal and call fQ[i]
    }
    while(data[1][2] < until)
    {
        m <- as.matrix(data)
        minP <- which.min(subset(m, m[,1] == 1)[,3]) #gets waiting proc with min time
        data[1][2] <- minp[3]  #update total time
        
        if(minP[2] == 1)
        {
            #handle yield_hold
        } else if(minP[2] == 2)
        {
            #handle yield_request
        }
        } else if(minP[2] == 3)
        {
            #handle yield_release
        }
        } else if(minP[2] == 4)
        {
            #handle yield_passivate
        } else if(minP[2] == 5)
        {
            #handle reactivate???
        }
    }
}
