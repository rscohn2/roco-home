def add_parser(subparsers):
    db_parser = subparsers.add_parser('db', help='Database maintenance')
    subparser = db_parser.add_subparsers()
    create_parser = subparser.add_parser('create', help='Create a database')
    create_parser.set_defaults(func=create)


def create():
    pass
