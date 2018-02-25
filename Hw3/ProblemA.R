makeAscendNums <- function(vec){
  if (is.vector(vec) == FALSE){
    stop("not a vector")
  }
  diff <- vec[-1] - vec[-length(vec)]
	if(any(diff < 0)){
		stop("not nondecreasing")
	}
  attr(vec, "strictAscend") <- ifelse( all( diff > 0),TRUE,FALSE)
	class(vec) <- "ascendNums"
	vec 
}
"[<-.ascendNums" <- function(x,i,value){
	stop("read-only")
}
"+.ascendNums" <- function(x, y){
  u <- as.vector(x)
  v <- as.vector(y)
  i <- 1
  j <- 1
  while(i <= length(u) && j <= length(v)){
    if(u[i] >= v[j]) {
      u <- c(u[0:(i-1)],v[j], u[i:length(u)])
      j = j + 1
    }
    i = i + 1
  }
  u <- ifelse(rep(i > length(u), length(u) + length(v) - j + 1), c(u, v[j:length(v)]), u)
  u
}
