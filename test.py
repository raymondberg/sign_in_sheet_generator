from sign_in_sheet import SignInSheet
from faker import Faker

if __name__ == '__main__':
    fake = Faker()
    SignInSheet(
        page_title="Cool Event",
        page_subtitle="Doors at 6:30",
        names=(fake.name() for _ in range(100)),
    ).generate()
