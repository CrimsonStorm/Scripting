library(bigmemory)
library(methods)

#globals
pQ <- c()
fQ <- c()
rQ <- c()
data <- big.matrix(1,3,init=0.0)
numProcs <- 0

setRefClass("Process", fields=list(pid="numeric"),
methods = list(
initialize = function()
{
    
    .self$pid = 0
})

setRefClass("Resource", fields=list(n="numeric"))

# Initialize
initialize <- function()
{
    #double the number of rows in data
    print(data[,])
    data <<- as.big.matrix(rbind(as.matrix(data),matrix(0,nrow=dim(data)[1],ncol=3)))
    print(data[,])
    dput(describe(data),file="memPtr")
    print("end of init")
}

# Used to indicate how much time to allocate to a thread
yield_hold <- function(p, holdTime)
{
    print("in yield")
    if(p$pid == 0) {p$pid <- numProcs + 1}
    if(p$pid > dim(data)[1]) { initialize() }
    data[p$pid,2] <<- 1
    data[p$pid,3] <<- data[1,2] + holdTime
    data[p$pid,1] <<- 1
    
    dd <- paste("while(data[",p$pid,",1]==1){data <- attach.big.matrix(dget('memPtr'))}", collapse="")
    fileConn<-file("scr.R")
    writeLines(c("source('Rposim.R')","data <- attach.big.matrix(dget('memPtr'))",dd), fileConn)
    close(fileConn)
    
    print(data)
    #create a thread so it can wait
    #system("Rscript scr.R")
    system("R CMD BATCH scr.R out.txt &")
    #system(paste("echo \"source('Rposim.R')\ndata <- attach.big.matrix(dget('memPtr'))\nwhile(data[",p$pid,",1]==1){data <- attach.big.matrix(dget('memPtr'))}\" | R --slave", collapse=""))
    if(numProcs == 0)
    {
        activate(p,f)
    }
    print("end of yield")
}

# Cause a thread to join a queue for a given resource and use if no other threads in queue
yield_request <- function(p,resource)
{
	rQ = c(rQ,p$pid)

}

# Indicate that a thread is done using a resource allowing next thread to use the resource (Need bigmemory for this)
yield_release <- function(p, resource)
{
	rQ = c(rQ[-1],p$pid)
}

# Have a thread wait until awakened by some other thread.
yield_passivate <-function(p)
{
	data[p$pid,1] = 1
}

# Mark a thread runnable when first created
activate <- function(p)
{
print("in activate")
    numProcs <<- numProcs + 1
    if(p$pid == 0) {p$pid <- numProcs + 1}
    if(p$pid > dim(data)[1])
    {
        initialize()
    }
    data[p$pid,1] <<- 0
    data[p$pid,2] <<- 0
    data[p$pid,3] <<- 0
    pQ <- c(pQ, p)
    fQ <- c(fQ, f)
    
    dd <- paste("p <- ",p$pid, collapse="")
    fileConn<-file("scr.R")
    writeLines(c("source('Rposim.R')",deparse(p$Run),"data <- attach.big.matrix(dget('memPtr'))","p <- "), fileConn)
    close(fileConn)
    
    system("R CMD BATCH scr.R out.txt &")
    
    print("after activate")
}

# Awakens a previously-passivated thread.
reactivate <- function(p)
{
	data[p$pid, 1] <<- 1
	pQ <- c(Pq,p)
	
	dd <- paste("p <- ",p$pid, collapse="")
    fileConn<-file("scr.R")
    writeLines(c("source('Rposim.R')",deparse(p$Run),"data <- attach.big.matrix(dget('memPtr'))","p <- "), fileConn)
    close(fileConn)
    
    system("R CMD BATCH scr.R out.txt &")
	
}

# Cancels all the events associated with a previously-passivated thread.
cancel <- function(p)
{
	pos = which(pQ == p$pid)
	if(pos == 1){
		pQ = pQ[-1]
	}else{
		pQ = c(pQ[1:pos-1],pQ[pos+1:length(pQ))
	}
}

now <- function()
{
    print("start of now")
    data[1,2]  #current time
}

# Do the simulation
simulate <- function(until)
{
print("in simulate")
    while(data[1,2] < until)
    {
        m <- as.matrix(data)
        minP <- which.min(subset(m, m[,1] == 1)[,3]) #get waiting proc with min time
        data[1,2] <- data[minP,3]  #update total time
        
        if(minP[2] == 1)
        {
            data[minP,1] <- 0
        } else if(minP[2] == 2)
        {
            #handle yield_request
        } else if(minP[2] == 3)
        {
            #handle yield_release
        } else if(minP[2] == 4)
        {
            #handle yield_passivate
        } else if(minP[2] == 5)
        {
            #handle reactivate???
        }
        print("bottom of sim loop")
    }
    print("end of simulate")
}