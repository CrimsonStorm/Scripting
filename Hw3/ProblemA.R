makeAscendNums <- function(vec){
	returnClass <- vec
	if(!(all(diff(returnClass )>=0))){
		stop("not nondecreasing")
	}
	if(all(diff(returnClass) >0)){
		attr(returnClass , 'strictAscend') <- TRUE
	}else{
		attr(returnClass , 'strictAscend') <- FALSE
	}
	class(returnClass) <- "ascendNums"
	returnClass 
}

"[<-.ascendNums" <- function(x,i,value){
	stop("read-only")
}

"+.ascendNums" <- function(x,x2){
	xVec <- c(x)
	x2Vec <- c(x2)
	newVector = recursiveFunc(xVec ,x2Vec )
	returnVec = makeAscendNums(newVector)
	returnVec
}

recursiveFunc <- function(b,c){
		totalVec <- c()
		if(length(b) > 0 && length(c) > 0){
			minVal <- min(b,c)
			if(!is.na(match(minVal,b))){
				b <- b[-1]
			}else{
				c <- c[-1]
			}
			totalVec <- c(totalVec,minVal)
			totalVec <- c(totalVec,recursiveFunc(b,c))
		}else if(length(b) == 0){
			totalVec <- c(totalVec,c)
		}else{
			totalVec <- c(totalVec,b)
		}
		totalVec
}