import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cars', type=int, nargs='?', default=50)
parser.add_argument('--barbie', type=int, nargs='?', default=50)
parser.add_argument('--movie', nargs='?', choices=["melodrama", "football", "other"],
                    default='other')
args = parser.parse_args()
answer = {'melodrama': 0, 'football': 100, 'other': 50}
cars = args.cars if 0 <= args.cars <= 100 else 50
barbie = args.barbie if 0 <= args.barbie <= 100 else 50
movie = answer[args.movie]
boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy
print('boy:', boy)
print("girl", girl)
