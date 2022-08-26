"""
Public API for token_utils.
"""
from token_utils.sign import create_jwt


def sign_token_for(lms_user_id, expires_in_seconds, additional_token_claims):
    """
    Produce a signed JWT token indicating some temporary permission for the indicated user.

    What permission that is must be encoded in additional_claims.
    Arguments:
        lms_user_id (int): LMS user ID this token is being generated for
        expires_in_seconds (int): Time to token expiry, specified in seconds.
        additional_token_claims (dict): Additional claims to include in the token.
    """
    return create_jwt(lms_user_id, expires_in_seconds, additional_token_claims)
