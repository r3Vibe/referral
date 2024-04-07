""" generete and return referral code """

from uuid import uuid4


def create_ref_code() -> str:
    """
    use this function to generate random referal code for users
    """
    code = uuid4().hex
    return code
