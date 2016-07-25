import sys

def convert(input_file, output_file):

	with open(input_file, 'r') as f:
		input_str = f.read()

	output_str = unicode(input_str, errors='ignore')

	with open(output_file, 'w') as f:
		f.write(output_str)

if __name__ == '__main__':

	args = sys.argv

	if (not len(args) == 3):
		raise ValueError('Takes two arguments: <name of input file> <name of output file>')

	convert(args[1], args[2])