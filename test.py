from faker import Faker

from sign_in_sheet_generator import SignInSheet

if __name__ == '__main__':
    fake = Faker()
    SignInSheet(
        page_title="Cool Event",
        page_subtitle="Doors at 6:30",
        names=(fake.name() for _ in range(100)),
    ).generate()
