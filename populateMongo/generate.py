#!/usr/bin/python -tt

import names
import random

def generate_name( gender ):
  #doesn't work, but it's a start
  first_name = names.get_first_name(gender=gender)
  last_name = names.get_last_name()
  return (first_name, last_name)

# def generate_date():
  # put code here

def generate_race():
  # put code here
  return random.choice([(1, "caucasian"), (2, "asian"), (3, "hispanic"), (4, "black_african_american"), (5, "american_indian"), (6, "other")])[0]

def generate_gender():
  # put code here
  return random.choice([(1, "male"), (2, "female"), (3, "other")])[0]

#def generate_pce():
	#put code here

#def generate_patient():
	#put code here

#def generate_observation():
	# put code here

#def generate_encounter():
	# put code here

#def convert_pce_to_json( pce ):
	# put code here

#def convert_patient_to_json( patient ):
	# put code here

#def convert_encounter_to_json( encounter ):
	# put code here

# def main():
  #put code here for execution

if __name__ == "__main__":
  main()
