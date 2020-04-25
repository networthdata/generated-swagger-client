# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InnerErrorV2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'innererror': 'InnerErrorV2'
    }

    attribute_map = {
        'code': 'code',
        'innererror': 'innererror'
    }

    def __init__(self, code=None, innererror=None):  # noqa: E501
        """InnerErrorV2 - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._innererror = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if innererror is not None:
            self.innererror = innererror

    @property
    def code(self):
        """Gets the code of this InnerErrorV2.  # noqa: E501

        A service-defined error code that should be human-readable.  This code serves as a more specific indicator of the error than  the HTTP error code specified in the response  # noqa: E501

        :return: The code of this InnerErrorV2.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InnerErrorV2.

        A service-defined error code that should be human-readable.  This code serves as a more specific indicator of the error than  the HTTP error code specified in the response  # noqa: E501

        :param code: The code of this InnerErrorV2.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def innererror(self):
        """Gets the innererror of this InnerErrorV2.  # noqa: E501

        A human-readable representation of the error. It is intended as  an aid to developers and is not suitable for exposure to end users  # noqa: E501

        :return: The innererror of this InnerErrorV2.  # noqa: E501
        :rtype: InnerErrorV2
        """
        return self._innererror

    @innererror.setter
    def innererror(self, innererror):
        """Sets the innererror of this InnerErrorV2.

        A human-readable representation of the error. It is intended as  an aid to developers and is not suitable for exposure to end users  # noqa: E501

        :param innererror: The innererror of this InnerErrorV2.  # noqa: E501
        :type: InnerErrorV2
        """

        self._innererror = innererror

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InnerErrorV2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InnerErrorV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other