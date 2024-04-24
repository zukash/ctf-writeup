import sys

from pyrage import passphrase


def decrypt():
    filename = "secret.age"
    password = "lattersoleshouldtoparticipationsenatorswithininformeddefinecensusonanswerwhereinprivilegesintofailedthinkcapitationwritings"
    with open(filename, "rb") as f:
        secret = passphrase.decrypt(f.read(), password)
    print(f"{secret=}")


if __name__ == "__main__":
    decrypt()
