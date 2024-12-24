from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.bewoning_api.models.base_model import Model
from brp.bewoning_api.models.abstract_datum import AbstractDatum
import re
from brp.bewoning_api import util

from brp.bewoning_api.models.abstract_datum import AbstractDatum  # noqa: E501
import re  # noqa: E501

class DatumOnbekend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, lang_formaat=None, onbekend=True):  # noqa: E501
        """DatumOnbekend - a model defined in OpenAPI

        :param type: The type of this DatumOnbekend.  # noqa: E501
        :type type: str
        :param lang_formaat: The lang_formaat of this DatumOnbekend.  # noqa: E501
        :type lang_formaat: str
        :param onbekend: The onbekend of this DatumOnbekend.  # noqa: E501
        :type onbekend: bool
        """
        self.openapi_types = {
            'type': str,
            'lang_formaat': str,
            'onbekend': bool
        }

        self.attribute_map = {
            'type': 'type',
            'lang_formaat': 'langFormaat',
            'onbekend': 'onbekend'
        }

        self._type = type
        self._lang_formaat = lang_formaat
        self._onbekend = onbekend

    @classmethod
    def from_dict(cls, dikt) -> 'DatumOnbekend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatumOnbekend of this DatumOnbekend.  # noqa: E501
        :rtype: DatumOnbekend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this DatumOnbekend.


        :return: The type of this DatumOnbekend.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this DatumOnbekend.


        :param type: The type of this DatumOnbekend.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def lang_formaat(self) -> str:
        """Gets the lang_formaat of this DatumOnbekend.


        :return: The lang_formaat of this DatumOnbekend.
        :rtype: str
        """
        return self._lang_formaat

    @lang_formaat.setter
    def lang_formaat(self, lang_formaat: str):
        """Sets the lang_formaat of this DatumOnbekend.


        :param lang_formaat: The lang_formaat of this DatumOnbekend.
        :type lang_formaat: str
        """
        if lang_formaat is None:
            raise ValueError("Invalid value for `lang_formaat`, must not be `None`")  # noqa: E501
        if lang_formaat is not None and not re.search(r'^[a-z0-9 ]{1,17}$', lang_formaat):  # noqa: E501
            raise ValueError(r"Invalid value for `lang_formaat`, must be a follow pattern or equal to `/^[a-z0-9 ]{1,17}$/`")  # noqa: E501

        self._lang_formaat = lang_formaat

    @property
    def onbekend(self) -> bool:
        """Gets the onbekend of this DatumOnbekend.


        :return: The onbekend of this DatumOnbekend.
        :rtype: bool
        """
        return self._onbekend

    @onbekend.setter
    def onbekend(self, onbekend: bool):
        """Sets the onbekend of this DatumOnbekend.


        :param onbekend: The onbekend of this DatumOnbekend.
        :type onbekend: bool
        """
        if onbekend is None:
            raise ValueError("Invalid value for `onbekend`, must not be `None`")  # noqa: E501

        self._onbekend = onbekend