library(bigmemory)
library(methods)

#globals
pQ <- c()
fQ <- c()
data <- big.matrix(1,3,init=0.0)
numProcs <- 0

setRefClass("Process",
fields=list(pid="numeric"),
methods = list(
initialize = function()
{
    .self$pid = 0
}))

setRefClass("Resource",
fields=list(n="numeric"))

# Initialize
initialize <- function(g=c())
{
#print("top of init")
    #double the number of rows in data
    data <<- as.big.matrix(rbind(as.matrix(data),matrix(0,nrow=dim(data)[1],ncol=3)))
    dput(describe(data),file="memPtr")
    
    if(length(g) > 100 || length(g) == 0)
    {
    }else
    {
        globals <<- as.big.matrix(matrix(g,nrow=1,ncol=length(g)))
        dput(describe(globals),file="globals")
    }
    #print("end of init")
}

# Used to indicate how much time to allocate to a thread
yield_hold <- function(p, holdTime)
{
    #print("in yield")
    if(p$pid == 0) {p$pid <- numProcs + 1}
    if(p$pid > dim(data)[1]) { initialize() }
    data[p$pid,2] <<- 1
    data[p$pid,3] <<- data[1,2] + holdTime
    data[p$pid,1] <<- 1
    
    while(data[p$pid,1] == 1) {data <- attach.big.matrix(dget('memPtr'))}
    
    #print("end of yield")
}

# Cause a thread to join a queue for a given resource and use if no other threads in queue
yield_request <- function(resource)
{

    rQ = c(rQ,p$pid)
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
activate <- function(p)
{
    #print("in activate")
    #print(p$pid)
    numProcs <<- numProcs + 1
    if(p$pid == 0) {p$pid <- numProcs + 1}
    if(p$pid > dim(data)[1])
    {
        initialize()
    }
    pQ <- c(pQ, p)
    save.image("env.RData")
    save(p,file="saveP.RData")
    
    fileConn<-file("scr.R")
    writeLines(c("load('env.RData')","load('saveP.RData')","library(methods)","library(bigmemory)","data <- attach.big.matrix(dget('memPtr'))","globals <- attach.big.matrix(dget('globals'))","p$Run()"), fileConn)
    close(fileConn)
    
    system("R CMD BATCH scr.R out.txt &")
    
    #print("after activate")
}

# Awakens a previously-passivated thread.
reactivate <- function()
{

}

# Cancels all the events associated with a previously-passivated thread.
cancel <- function()
{
	
}

now <- function()
{
    #print("start of now")
    data[1,2]  #current time
}

# Do the simulation
simulate <- function(until)
{
#print("in simulate")
    while(data[1,2] < until)
    {
        m <- as.matrix(data)
        minP <- which.min(subset(m, m[,1] == 1)[,3]) #get waiting proc with min time
        
        
        
        if(length(minP) != 0)
        {
        
            minP <- minP + 2
            data[1,2] <- data[minP,3]  #update total time
            
            #print(data)
            
            #print("minp")
            #print(minP)
            
            #print(data[minP,])
            if(data[minP,2] == 1)
            {
                data[minP,1] <- 0
            } else if(data[minP,2] == 2)
            {
                #handle yield_request
            } else if(data[minP,2] == 3)
            {
                #handle yield_release
            } else if(data[minP,2] == 4)
            {
                #handle yield_passivate
            } else if(data[minP,2] == 5)
            {
                #handle reactivate???
            }
        }
        #print("bottom of sim loop")
    }
    #print("end of simulate")
}
