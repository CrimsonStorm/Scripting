library(simmer)

NUM_MACHINES <- 2  		# Number of machines
NUM_REPAIRPERSONS <- 2 	# Number of repair people
REPAIRRATE <- 1/0.5     # Average amount of time to repair a machine
UPRATE <- 1/1.0       	# Average amount of time the machine is working
SIM_TIME <- 10000     	# Total simulation time

set.seed(12345)			# Set seed
env1 <- simmer()		# Instantiate the simulated environment

  # Setup trajectory to simulate a repair event
repair_person <- trajectory() %>%
	# Removes a resource from of the current number of resources
  seize("repair", 1) %>%
	# Create new attribute with random uptime
  set_attribute("newUptime",function(){rexp(1,1/1.0)},global=TRUE) %>%
	# Simulate time up for machine
  timeout(function() {ifelse(is.na(get_attribute(env1,"newUptime")),0,get_attribute(env1,"newUptime"))}) %>%
	# Simulate time to be repaired
  timeout(function(){rexp(1,REPAIRRATE)}) %>%
	# Add the resource back to the current number of resources
  release("repair", 1)
  
# Setup the simulated environment
env1 %>%
	# Adds repair resource for trajectory to pull from
  add_resource("repair", NUM_MACHINES) %>%
	# Add initial events for number of repair people
  add_generator("repair_person", repair_person, at(rep(0,NUM_REPAIRPERSONS))) %>% 
	# Makes arrival events at a randomly distributed rate
  add_generator("create_new_uptime", repair_person, function() sample(rexp(1,1/1.0), 1)) %>%
  
	# Start the simulation
  run(until = SIM_TIME)


  # Store all values of all attribues in the environment
x = env1 %>% get_mon_attributes
  # Store values of newUpTime
y = x$value
  # Sum all values of newUpTime
z = sum(y)
  # Calculate the percentage of upTime
PercentUp = z / (NUM_MACHINES*SIM_TIME)
  # Print the percentage of upTime
print(paste0("Percent machines are up is: ", PercentUp))