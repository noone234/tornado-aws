"""
The following exceptions may be raised during the corse of using
:py:class:`tornado_aws.AWSClient` and :py:class:`tornado_aws.AsyncAWSClient`.

"""

class AWSClientException(Exception):
    """Base exception class for AWSClient

    :ivar msg: The error message

    """
    fmt = 'An error occurred'

    def __init__(self, **kwargs):
        super(AWSClientException, self).__init__(self.fmt.format(**kwargs))


class ConfigNotFound(AWSClientException):
    """The configuration file could not be parsed.

    :ivar path: The path to the config file

    """
    fmt = 'The config file could not be found ({path})'


class ConfigParserError(AWSClientException):
    """Error raised when parsing a configuration file with
    :py:class`configparser.RawConfigParser`

    :ivar path: The path to the config file

    """
    fmt = 'Unable to parse config file ({path})'


class NoCredentialsError(AWSClientException):
    """Raised when the credentials could not be located."""
    fmt = 'Credentials not found'


class NoProfileError(AWSClientException):
    """Raised when the specified profile could not be located.

    :ivar path: The path to the config file
    :ivar profile: The profile that was specified

    """
    fmt = 'Profile ({profile}) not found ({path})'
