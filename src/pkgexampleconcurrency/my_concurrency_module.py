import argparse
from .mythreading import MyThreading


def my_threading():
    my_threading_main_parser = argparse.ArgumentParser(
        description="Run default threading example"
    )
    my_threading_parser = my_threading_main_parser.add_mutually_exclusive_group()
    my_threading_parser.add_argument(
        "--nd-concurrent", action="store_true", help="'Non daemon' concurrent example."
    )
    my_threading_parser.add_argument(
        "--nd-nj-concurrent",
        action="store_true",
        help="'Non daemon' 'non-join' concurrent example.",
    )
    my_threading_parser.add_argument(
        "--nd-serial", action="store_true", help="'Non daemon' serial example."
    )
    my_threading_parser.add_argument(
        "--d-concurrent", action="store_true", help="'Daemon' concurrent example."
    )
    my_threading_parser.add_argument(
        "--d-nj-concurrent",
        action="store_true",
        help="'Daemon' 'non-join' concurrent example.",
    )
    my_threading_parser.add_argument(
        "--i-printalpha",
        action="store_true",
        help="Thread by inheritence example. Define own class that prints alphabet.",
    )

    my_args = my_threading_main_parser.parse_args()
    mythreadingexamples = MyThreading()
    if my_args.nd_concurrent == True:
        mythreadingexamples.non_daemon_concurrent_example()
    if my_args.nd_serial == True:
        mythreadingexamples.non_daemon_serial_example()
    if my_args.nd_nj_concurrent == True:
        mythreadingexamples.non_daemon_no_join_concurrent_example()
    if my_args.d_concurrent == True:
        mythreadingexamples.daemon_concurrent_example()
    if my_args.d_nj_concurrent == True:
        mythreadingexamples.daemon_no_join_concurrent_example()
    if my_args.i_printalpha == True:
        mythreadingexamples.print_alpha()


def my_concurrentfutures():
    my_concurrentfutures_parser = argparse.ArgumentParser(
        description="Run default concurrent futures example"
    )
    my_concurrentfutures_parser.add_argument(
        "--run", action="store_true", help="Run default concurrent futures example"
    )
    my_args = my_concurrentfutures_parser.parse_args()
    print(my_args.run)


def my_multiprocessing():
    my_multiprocessing_parser = argparse.ArgumentParser(
        description="Run default multiprocessing example"
    )
    my_multiprocessing_parser.add_argument(
        "--run", action="store_true", help="Run default multiprocessing example"
    )
    my_args = my_multiprocessing_parser.parse_args()
    print(my_args.run)


def my_asyncio():
    my_asyncio_parser = argparse.ArgumentParser(
        description="Run default asyncio example"
    )
    my_asyncio_parser.add_argument(
        "--run", action="store_true", help="Run default asyncio example"
    )
    my_args = my_asyncio_parser.parse_args()
    print(my_args.run)
