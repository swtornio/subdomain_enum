

import argparse
import dns.resolver

# ANSI codes for some pretty terminal output
class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

domains_exist = []

def permute(base, domain, permutations):
    names_to_try = []
    for item in permutations:
        names_to_try.append(f"{item}{base}.{domain}")
        names_to_try.append(f"{base}{item}.{domain}")
        names_to_try.append(f"{item}.{base}.{domain}")
        names_to_try.append(f"{base}.{item}.{domain}")
        names_to_try.append(f"{item}-{base}.{domain}")
        names_to_try.append(f"{base}-{item}.{domain}")
    return names_to_try
    

def resolve(name):
    global domains_exist
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8']
    try:
        answer = resolver.resolve(name, 'A')
        print(f"{bcolors.OK}{name}{bcolors.RESET} exists")
        # We don't care what the IP is, just that the name exists
        domains_exist.append(name)
    # except dns.resolver.NXDOMAIN as e:
        # pass
    except dns.resolver.NoAnswer as e:
        # This exception means there's some kind of record, but no IP was returned
        print(f"Exists but no IP for {bcolors.WARNING}{name}{bcolors.RESET}")
        domains_exist.append(name)
    except Exception as e:
        pass


def main():

    parser = argparse.ArgumentParser(
        description='Enumerate Azure Cloud resources')
    parser.add_argument('--base', help='Base word')
    parser.add_argument('--permutations', default='permutations.txt',
        help='File containing permutations')
    parser.add_argument('--domains', default='domains.txt',
        help='File containing permutations')
    parser.add_argument('--outfile', help='Output file')

    args = parser.parse_args()
    base = args.base
    permutations_file = args.permutations
    domains_file = args.domains
    outfile = args.outfile

    with open(permutations_file) as f:
        permutations = f.read().splitlines()

    with open(domains_file) as f:
        domains = f.read().splitlines()

    for domain in domains:
        candidates = permute(base, domain, permutations)
        candidates.append(f"{base}.{domain}")
        for candidate in candidates:
            resolve(candidate)

    with open(outfile, "w") as f:
        for domain in domains_exist:
            f.write(f"{domain}\n")


if __name__ == '__main__':
    main()