def code_intro():
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------  Project Euler Problem 151  --------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------- This project was done as part https://projecteuler.net/ ----------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
	print ' A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5. Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special paper with size A1. He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them in half to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for the first batch of the week. All the unused sheets are placed back in the envelope. At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random. If it is of size A5, he uses it. If it is larger, he repeats the cut-in-half procedure until he has what he needs and any remaining sheets are always placed back in the envelope. Excluding the first and last batch of the week, find the expected number of times (during each week) that the foreman finds a single sheet of paper in the envelope. Give your answer rounded to six decimal places using the format x.xxxxxx .'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)

def main():

	code_intro()
	starting_envelope = (1,)
	envelope_percent_map = {}
	# We substract two because we don't count the starting envelope(always one piece of paper)
	# and the end envelope (always always one piece of paper)
	probability_of_finding_only_one_sheet_in_envelope = get_probability_of_only_one_sheet_in_envelope(starting_envelope, envelope_percent_map) - 2
	return "{:.6f}".format(probability_of_finding_only_one_sheet_in_envelope)


def get_probability_of_only_one_sheet_in_envelope(current_envelope, envelope_percent_map):
	# if the probability of this state has not been calcuated, let's calcuate it
	if current_envelope not in envelope_percent_map:
		percent_chance_to_find_only_one_sheet = 0.0
		if len(current_envelope) > 0:

			# iternate through every possible sheet selection
			for picked_sheet in range(len(current_envelope)):
				# new_envelope simulates one cut after current_envelope in the recurrsion
				# current_envelope is used to to elauate the current state
				new_envelope = list(current_envelope)

				# this cuts the paper
				new_envelope = cut_paper(new_envelope,picked_sheet)
				# !!! the recursive bit !!!
				# this statement builds a tree of probabilities depth first (from the roots up)
				# as the roots of the tree are combined the probabilities are combined
				percent_chance_to_find_only_one_sheet += get_probability_of_only_one_sheet_in_envelope(tuple(new_envelope), envelope_percent_map)
			# to get the average probability of the given state we add to probabilities
			# of each branch together and divide by the number of branches
			percent_chance_to_find_only_one_sheet /= len(current_envelope)

			# if the current_envelope only has one sheet, you will HAVE to grab that sheet
			if len(current_envelope) == 1:
				percent_chance_to_find_only_one_sheet += 1.0
				if not current_envelope == (5,):
					print current_envelope,percent_chance_to_find_only_one_sheet-2
		# add a key value pair of
		# - the current state and
		# - the probability that from this state you will find only one sheet of paper in the envelope
		# to the envelope_percent_map
		envelope_percent_map[current_envelope] = percent_chance_to_find_only_one_sheet
		# print "given state / probability of one sheet", current_envelope, envelope_percent_map[current_envelope]
	return envelope_percent_map[current_envelope]



def cut_paper(new_envelope,picked_sheet):
	sheet = new_envelope[picked_sheet]
	del new_envelope[picked_sheet]
	for cut_sheet in range(sheet + 1, 6):
		new_envelope.append(cut_sheet)
	new_envelope.sort()
	return new_envelope

if __name__ == "__main__":
	print(main())
