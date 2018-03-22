library(simmer)

NUM_MACHINES <- 2  # Number of machines
NUM_REPAIRPERSONS <- 2 # Number of repair people
REPAIRRATE <- 1/0.5      # Reciprocal of mean repair time
UPRATE <- 1/1.0       # Reciprocal of mean up time 
SIM_TIME <- 10000     # Simulation time 

# setup
set.seed(12345)
env1 <- simmer()

repair_person <- trajectory() %>%
  seize("fix", 1) %>%
  set_attribute("newUptime",function(){rexp(1,1/1.0)},global=TRUE) %>%
  timeout(function() {ifelse(is.na(get_attribute(env1,"newUptime")),0,get_attribute(env1,"newUptime"))}) %>%
  timeout(function(){rexp(1,REPAIRRATE)}) %>%
  release("fix", 1) 
  
  env1 %>%
  add_resource("fix", NUM_MACHINES) %>%
  add_generator("repair_person", repair_person, at(rep(0,NUM_REPAIRPERSONS))) %>%
  add_generator("create_new_uptime", repair_person, function() sample(rexp(1,1/1.0), 1)) %>%
  # start the simulation
  run(until = SIM_TIME)
  
x = env1 %>% get_mon_attributes
y = x$value
z = sum(y)
PercentUp = z / (NUM_MACHINES*SIM_TIME)
print(paste0("Percent machines are up is: ", PercentUp))
