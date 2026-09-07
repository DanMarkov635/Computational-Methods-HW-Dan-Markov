import argparse


def time(h, g):
	t = (2 * h / g) ** 0.5
	return t

parser = argparse.ArgumentParser()

parser.add_argument("--h", type = float, required = True)
parser.add_argument("--g", type = float, default = 9.8)

args = parser.parse_args()

result = time(args.h, args.g)

print(result)
