import argparse
from atm_app import run_atm


def parse_arguments():
    parser = argparse.ArgumentParser(description="ATM application")
    parser.add_argument("--logfile", type=str, default="atm.log", help="Specify the log file")
    parser.add_argument("--users-file", type=str, default="users.json", help="Specify the users data file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    run_atm(args.logfile, args.users_file)
