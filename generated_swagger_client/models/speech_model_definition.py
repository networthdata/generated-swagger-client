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


class SpeechModelDefinition(object):
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
        'model_kind': 'str',
        'text': 'str',
        'base_model': 'ModelIdentity',
        'datasets': 'list[DatasetIdentity]',
        'description': 'str',
        'locale': 'str',
        'properties': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'model_kind': 'modelKind',
        'text': 'text',
        'base_model': 'baseModel',
        'datasets': 'datasets',
        'description': 'description',
        'locale': 'locale',
        'properties': 'properties',
        'name': 'name'
    }

    def __init__(self, model_kind=None, text=None, base_model=None, datasets=None, description=None, locale=None, properties=None, name=None):  # noqa: E501
        """SpeechModelDefinition - a model defined in Swagger"""  # noqa: E501

        self._model_kind = None
        self._text = None
        self._base_model = None
        self._datasets = None
        self._description = None
        self._locale = None
        self._properties = None
        self._name = None
        self.discriminator = None

        self.model_kind = model_kind
        if text is not None:
            self.text = text
        if base_model is not None:
            self.base_model = base_model
        if datasets is not None:
            self.datasets = datasets
        if description is not None:
            self.description = description
        self.locale = locale
        if properties is not None:
            self.properties = properties
        self.name = name

    @property
    def model_kind(self):
        """Gets the model_kind of this SpeechModelDefinition.  # noqa: E501

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :return: The model_kind of this SpeechModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._model_kind

    @model_kind.setter
    def model_kind(self, model_kind):
        """Sets the model_kind of this SpeechModelDefinition.

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :param model_kind: The model_kind of this SpeechModelDefinition.  # noqa: E501
        :type: str
        """
        if model_kind is None:
            raise ValueError("Invalid value for `model_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["Acoustic", "Language", "AcousticAndLanguage", "None", "CustomVoice", "Sentiment", "LanguageIdentification", "Diarization", "Keyword", "PronunciationScore"]  # noqa: E501
        if model_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `model_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(model_kind, allowed_values)
            )

        self._model_kind = model_kind

    @property
    def text(self):
        """Gets the text of this SpeechModelDefinition.  # noqa: E501

        The text used to adapt this language model  # noqa: E501

        :return: The text of this SpeechModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SpeechModelDefinition.

        The text used to adapt this language model  # noqa: E501

        :param text: The text of this SpeechModelDefinition.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def base_model(self):
        """Gets the base_model of this SpeechModelDefinition.  # noqa: E501

        The base model used for adaptation  # noqa: E501

        :return: The base_model of this SpeechModelDefinition.  # noqa: E501
        :rtype: ModelIdentity
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        """Sets the base_model of this SpeechModelDefinition.

        The base model used for adaptation  # noqa: E501

        :param base_model: The base_model of this SpeechModelDefinition.  # noqa: E501
        :type: ModelIdentity
        """

        self._base_model = base_model

    @property
    def datasets(self):
        """Gets the datasets of this SpeechModelDefinition.  # noqa: E501

        Datasets used for adaptation  # noqa: E501

        :return: The datasets of this SpeechModelDefinition.  # noqa: E501
        :rtype: list[DatasetIdentity]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this SpeechModelDefinition.

        Datasets used for adaptation  # noqa: E501

        :param datasets: The datasets of this SpeechModelDefinition.  # noqa: E501
        :type: list[DatasetIdentity]
        """

        self._datasets = datasets

    @property
    def description(self):
        """Gets the description of this SpeechModelDefinition.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this SpeechModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SpeechModelDefinition.

        The description of the object  # noqa: E501

        :param description: The description of this SpeechModelDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def locale(self):
        """Gets the locale of this SpeechModelDefinition.  # noqa: E501

        The locale of the contained data  # noqa: E501

        :return: The locale of this SpeechModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this SpeechModelDefinition.

        The locale of the contained data  # noqa: E501

        :param locale: The locale of this SpeechModelDefinition.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def properties(self):
        """Gets the properties of this SpeechModelDefinition.  # noqa: E501

        The custom properties of this entity  # noqa: E501

        :return: The properties of this SpeechModelDefinition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SpeechModelDefinition.

        The custom properties of this entity  # noqa: E501

        :param properties: The properties of this SpeechModelDefinition.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def name(self):
        """Gets the name of this SpeechModelDefinition.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this SpeechModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpeechModelDefinition.

        The name of the object  # noqa: E501

        :param name: The name of this SpeechModelDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(SpeechModelDefinition, dict):
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
        if not isinstance(other, SpeechModelDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
