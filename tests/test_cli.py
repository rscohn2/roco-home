from rocohome.cli import main


def test_main():
    main()


def test_db():
    main(['db'])


def test_db_create():
    main(['db', 'create'])
