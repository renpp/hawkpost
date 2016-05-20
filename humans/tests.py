from django.test import TestCase
from boxes.tests import create_and_login_user
from .forms import UpdateUserInfoForm
from .utils import key_state

VALID_KEY = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQINBFZMyTEBEADKO14GykJFXAjlyXYI9QhkSA9mXzF8vQDWeO/KWwS42PS3+bjT
WwIkfOCBRVOXoVqm4m4oD0uzZwp2Dnc5eIceIku7iwUuzQrbIMCl9FDBTYCnF/Sd
Fa/R98xURVAdxyIBNxVUbV07gWBcALLRMO+HWinF/JMDQ1ZhM99jSkia6Y0jMgpy
2fDjz+audlor3Qtc7SCYDSr68PD0EJhfg8PSikYSEphN3cvJvya8Ydvjg+ykcUo/
Vh/+sr+YO41AVBZZBGpROH4bAgprYGiyQJ33rGhfRQV1+Mg/u6lMfnWYwIcB5lyj
VBhS8/15z/qWfsqRLt5uZkElUqCabvCqOhy6G4UtezJXb8h8AeTaNsO0hyu48Nwh
KYIyPy/ajI/tDaf10sCdiFNTzTb80KYijxEo/llMCOMdIJP2rbQRy/ysbJEvxV+b
Pg7sAdi6Y1+EVQEDF/0sY2BchE3dmmb7gocP9oyeATtBU64ccP0rqwO2HjmlGUVd
PG0+gacXwXAOQtJtFoFkk1muD56ylQDdOi/XNmF8XpLHemctXl+ieph2t+pAy6Fx
ZggxHU0meboOKuUMALmnJQSn175RsMiwDJRbTHLTTZom+MrFcNIqZrWyvECQnb6P
0vzNfHFqsHgMmdztHGKmizlbOzaFeRjfE8Xwm3V5T5ZrIAbXVqw9GAiiTwARAQAB
tCpHb27Dp2FsbyBWYWzDqXJpbyA8Z3ZhbGVyaW9Ad2hpdGVzbWl0aC5jbz6JAj8E
EwEIACkFAlZMyTECGyMFCQPCZwAHCwkIBwMCAQYVCAIJCgsEFgIDAQIeAQIXgAAK
CRAywck5F8smut5DD/0TnQz+RZuUKsaD8vnjtmoTGBTR2RiA3aBYL39K34nPeVFU
TuUQ/RUqFA4VEdr6wEKsnOKryVav/M5wjlyhn7U5H3WVFiaYGspD3PDOkM5515KZ
ZuRDiqfJaNveDRO4R6t6ajXEsl2vxmwBw376JXRgB25QvFZYmbT6x1mC8GcHc4SU
04VyQfzhThOGDsDSJEoRm+JbYYYZmzDia/isfjgvM4kRwf5c2rHfays8kKPLfAgp
nuye3OwR+taQysr4TVnCt9DXlDy8J31qpKTsmB+ppNX7aens4ZgIiuMYwkazyym4
8xy+4R0Zx1h+Hj8EPBiROIzRtTkXJ2fdexrF84ka1e+aXdMOL4Z/sGK2sjUin2K+
suH/L8tjNJYltqJMAAO44lMEC9+bWOXClx1vLp4lw9ZxSlfmMJZzJrBmN/5LcP+p
zbjxzLIYOyN07MRPQFpnE44tW4w1GqtUOWYH5RTswhsfADT8O0kqv2RfrUt/UyU2
PXhowdfqrQp28GqbqdIfoYFVoQkce04ivMs+zAwQ8vPNpD7i4mujrKObedfeztGW
k8wEpj6ItNF8/tB3jmVD/2Hw78wfwa8Ci8beTJNotjyD4sKuO09XN45D0S4LpQ4W
EQKojkMs75s25h4pReXluUKzk5HQhaS3VjAV+JdF+YlnnlV0ZnIvcowF/wBzhokC
HAQSAQgABgUCVlW2SwAKCRDfVX8r3MJEXiPsD/9n1ueoA4ImhHvmCXdh98iGFYcz
+RX2lpgw61YxMtuirssORckwk8Xn+/sGkr01hawYxYTNleS92djS7dy5F+5OZMLL
4Tum57dACdx32+qS85ykeDDLmhDjv6BdGyTOkQGejisRdiBRUTYIjhsuMp5ZraXK
tWT1shwWnx8IJ4fCRnfbe7lAbGx0MwSrDSKA1BUGMx0dDUuL8o/cGeM5LMGj/J8p
GGVVQFTnnVF7SKAgbvS4ADTJX2iOSoDwDE0R32HkvL2ZmjQi1LlfHVlr/FcW8ftq
DP9zAUbvZeXKfnU+HnDV5eazFIlTUwEx6tn4K6SUY2VZv7uEYugnxfj7VsZJf1X/
4waDckg6TAcTbvTnKAwxjIbmMkRF172s4Mhs7QPP81eK97pRHyWO7d1nkBY9IQz2
8pPrcicGkSbcgC8MbgAsJJbIQRqg3xYMbHoxotxHccYRcz7/5/R2H0+LE1uANKso
rXy9QUZoQ9wSIH0TpiUp7YRj3yjbkNbocG/5OsnedBXcUyM/AMoHdo6ivKqGLbeN
e86t3eotvBU7DOlvn1W7YMaJEYm29ScPKK2TECi2NqgVRJob6Dnz+zDXEyrkYlRY
lpdzXFdJpcrosmLIVpnAEUbZ4OZjHLXUmXaKZpNqOCEgBzZpEhbYyshUuVaHt1gt
6hU+kjmHKmXEn8v1xokCHAQQAQIABgUCVsShDAAKCRAMOynBaF6lxOLBEACIlbzq
m00E6HDLhYVfrCNw0PxwX6w33DDJvNFfilmyQiFUP7O7v6HH/NR9TS09UmoxwAx1
9mXJvRMNiV5QN/9SE57K4Mk0lBRm2wHjzlnYmZ3T5W/9dyJSAAG8tiVey1gPsi8t
G/CTwT1n/WoL8sV7zEuMvYS5rltQPBMCazGrc7ickW+yMEsFWBLu6h4CDfJXwVkm
iJZbuRTHyTCXoO8ZOS/9NM42kvt3+uIIO+1TDh0/Chp/nmo5ZXE8Rdz9rsKat92z
AQRa/D24oQYZFCyWTAehXajjDQhRDX2YdDsD0jnOBbjG51W7tfROxkr7pQdbgxN0
zN65dKd3RV+1V5JODJRV00rzNxnF/+h75YWEIFlWZ31miZnF/RprNusdYqOIKaPq
UYuycumcVRVqWr7TOCm0bcRxKW07KMBrSIQQfW97w5aVlKy3Bz6B3mq9fMUYHPiq
mAFuzAcEfxqqsFM0L14df3ClsJx9dZrr3EBUkFqVXLdtAHxnnMgJhJmX7k+T0GUk
m2pYC6pPRmFtfpDM4rdDHnf5P3SqgpFbbbcsPpTesra5tRVWSOOWpt/nu6JrqDGS
0+dbXC4uk0AP6cq4iUaZcXxNNAVXTMwyobhRORCvXTZnKgBW2cr4c3nca+//LaHl
0puQkTQOiwl9sM+7sTC3tzsHhj1OUEclKX/GlbkCDQRWTMkxARAAyH5jpsVFIh7/
QR5jCBQWm+JAJ7vXfy0n07eLtPt6VDsPS3SDzuWAG0vvoVM9CH4tVk+yFsBfUFlc
FjEANFzvADSlAjayGm0sG11sRtYyN4PS0z8dY3vyKy2pp9pFjop9JG+R7+K8Ps6C
mbNhAtUIr1ls/J3lmr7aAV4nhECOE/cxE+Vv0furMgnsBz5NljzK3XRIWY+7jF1/
Rd0VJFCywa1p0Sw2Ea1znNrzRj7SBUC8DnPOKj2cRXZhadJep5g1zeBYNccVAyfz
JLXm3HFoIFfUmkjhB7h1RrLJ2250bm4q+fvxgZyWhWkrZYbGIS4tKFDqGz5iH3DQ
L/iDW7p3goQsTYDe2J4WrVABEstJYnLEJNFj0mPMpxExTFH37jC8X03vfxJDxyd5
kN0rfDVbqOJdklZ48ATirY+Y45O60GytLH/Iyu4BibKW+MuI9oFv02Ob0Ujg53rl
XQyGjVgKgAwaLYyHoel+DDznHDKz9nDGFObRRevKls9LNXJOebInP28Spe7bFq4M
mMPdPEqRNqt+WZEdLYRAxR4tRfIMvgXTAhzvy+XG7Ao7WJt5bs7V+WYqolmlhL9P
Cgr2v5gz6Y1JNDfzYKAtmiN3/Flg6ewFz/X5MAhFdved/pzCJ60t/FGcMiX0X85g
GT/ktfIAw+1A+G0z4W0Mm+wGXU6nIU8AEQEAAYkCJQQYAQgADwUCVkzJMQIbDAUJ
A8JnAAAKCRAywck5F8smugs4D/48am1IMqa9VgRP2UxYztGpxaIeNmvnt0sN/Tk6
o6pQXjRFY8mOrMUldr8pRnxAgBD+sco+2fMGvIA5U6El6rsBMr/V5tBeKY7pQF9d
xxF01hQCLFNVBG3HNeYB8dh/0okYObkhtp0DljEYWF96NHcdyZaQTwRdSWpObkSy
V9B761ZIGi4JulbSegQy7owbSrPDRb2KrjmoXeFH3LOVRAgdBD1w1RPb718OHJ2r
0Fbk7YJ+0N9ORAy+Hq8Su8vrYM8Vot2q88/S5JrZFPMjyfAg5sJrta3rdr4U8WW6
JxhQptfYnrQienuDKBHt0y/EINhEQfYCgH8Ffij6xFeQvHczoP3mp4y8diM5ZvFB
D6arVNM6V4Yrnbw5xpU8oAdiW5BjYXpEwZV+Ji+VUBpOpemfhZ+R+dD6s55buxng
Ya7ytBylZ9RWxvIce8k/lyIojHiEzHnvoP3AuNrwjgLDk5bducWXqN0TE9swr5Ap
6/cTg+bfuWVsHStrCvNPz/cN6IWeBPc+AtfO3DcDR5+A88yEE6K+clIFXLv/qrA9
odaHnhRBTx7qi6zLLQQxzNya8eXe5NibB1ypqrKBaf0qrkpFUJGW3bap4796yKyr
qGa8WG40Hc6zMeD3GShB8B877m9HN3fXUwhQ4jrMACx7rb/vdTVdbK3a7YZziwkP
cziA/g==
=yw2V
-----END PGP PUBLIC KEY BLOCK-----
"""

VALID_KEY_FINGERPRINT = "A1B5 01A1 5077 6B0E 65F4 446B 32C1 C939 17CB 26BA"

VALID_KEYSERVER_URL = "https://pgp.mit.edu/pks/lookup?op=get&search=0x32C1C93917CB26BA"

EXPIRED_KEY = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.5
Comment: Hostname: pgp.mit.edu

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
8e6k2TpLNf1VrR1+IUmD+hbFmeSR
=3qZO
-----END PGP PUBLIC KEY BLOCK-----
"""

EXPIRED_KEY_FINGERPRINT = "84009091C9F92152D34BF0919841A6E703BA514A"

REVOKED_KEY = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.5
Comment: Hostname: pgp.mit.edu

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
=+LpS
-----END PGP PUBLIC KEY BLOCK-----
"""

REVOKED_KEY_FINGERPRINT = "C341AE04573A4D7CCBDE594C83AFB921E7A24CCA"


class UpdateUserFormTests(TestCase):

    def test_empty_fingerprint(self):
        data = {
            "first_name": "some name",
            "last_name": "some last name",
            "company": "some company",
            "fingerprint": "",
            "timezone": "UTC",
            "public_key": VALID_KEY
        }
        form = UpdateUserInfoForm(data)
        self.assertEqual(form.is_valid(), False)

    def test_fingerprint_plus_public_key(self):
        data = {
            "first_name": "some name",
            "last_name": "some last name",
            "company": "some company",
            "timezone": "UTC",
            "fingerprint": VALID_KEY_FINGERPRINT,
            "public_key": VALID_KEY
        }
        form = UpdateUserInfoForm(data)
        self.assertEqual(form.is_valid(), True)

    def test_fingerprint_plus_keyserver_url(self):
        data = {
            "first_name": "some name",
            "last_name": "some last name",
            "company": "some company",
            "timezone": "UTC",
            "fingerprint": VALID_KEY_FINGERPRINT,
            "keyserver_url": VALID_KEYSERVER_URL
        }
        form = UpdateUserInfoForm(data)
        self.assertEqual(form.is_valid(), True)

    def test_fingerprint_mismatch(self):
        data = {
            "first_name": "some name",
            "last_name": "some last name",
            "company": "some company",
            "timezone": "UTC",
            "fingerprint": EXPIRED_KEY_FINGERPRINT,
            "public_key": VALID_KEY
        }
        form = UpdateUserInfoForm(data)
        self.assertEqual(form.is_valid(), False)


class UtilsTests(TestCase):

    def test_invalid_key_state(self):
        fingerprint, state = key_state("invalid stuff")
        self.assertEqual(state, "invalid")

    def test_expired_key_state(self):
        fingerprint, state = key_state(EXPIRED_KEY)
        self.assertEqual(state, "expired")

    def test_revoked_key_state(self):
        fingerprint, state = key_state(REVOKED_KEY)
        self.assertEqual(state, "revoked")

    def test_valid_key_state(self):
        fingerprint, state = key_state(VALID_KEY)
        self.assertEqual(state, "valid")


class UserModelTests(TestCase):

    def test_no_setup_complete(self):
        user = create_and_login_user(self.client)
        self.assertEqual(user.has_setup_complete(), False)

    def test_setup_complete(self):
        user = create_and_login_user(self.client)
        user.public_key = VALID_KEY
        user.fingerprint = VALID_KEY_FINGERPRINT
        user.save()
        self.assertEqual(user.has_setup_complete(), True)
