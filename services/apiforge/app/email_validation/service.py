from email_validator import validate_email
from email_validator import EmailNotValidError

import dns.resolver

from app.email_validation.schemas import (
    EmailVerificationResponse
)

from app.email_validation.exceptions import (
    EmailValidationException
)


DISPOSABLE_DOMAINS = {
    "mailinator.com",
    "10minutemail.com",
    "temp-mail.org",
    "guerrillamail.com",
    "yopmail.com"
}


class EmailValidationService:

    async def verify(
        self,
        email: str
    ):

        valid_syntax = False
        mx_found = False
        disposable = False

        try:

            validate_email(
                email,
                check_deliverability=False
            )

            valid_syntax = True

        except EmailNotValidError:

            return EmailVerificationResponse(
                email=email,
                valid_syntax=False,
                mx_found=False,
                disposable=False,
                is_valid=False
            )

        try:

            domain = email.split("@")[1]

            dns.resolver.resolve(
                domain,
                "MX"
            )

            mx_found = True

        except:

            mx_found = False


        disposable = domain.lower() in DISPOSABLE_DOMAINS


        is_valid = (

            valid_syntax

            and

            mx_found

            and

            not disposable
        )


        return EmailVerificationResponse(

            email=email,

            valid_syntax=valid_syntax,

            mx_found=mx_found,

            disposable=disposable,

            is_valid=is_valid
        )