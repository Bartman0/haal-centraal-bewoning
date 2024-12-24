from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.bewoning_api.models.base_model import Model
from brp.bewoning_api.models.bewoningen_query import BewoningenQuery
import re
from brp.bewoning_api import util

from brp.bewoning_api.models.bewoningen_query import BewoningenQuery  # noqa: E501
import re  # noqa: E501

class BewoningMetPeildatum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, peildatum=None, adresseerbaar_object_identificatie=None):  # noqa: E501
        """BewoningMetPeildatum - a model defined in OpenAPI

        :param type: The type of this BewoningMetPeildatum.  # noqa: E501
        :type type: str
        :param peildatum: The peildatum of this BewoningMetPeildatum.  # noqa: E501
        :type peildatum: date
        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this BewoningMetPeildatum.  # noqa: E501
        :type adresseerbaar_object_identificatie: str
        """
        self.openapi_types = {
            'type': str,
            'peildatum': date,
            'adresseerbaar_object_identificatie': str
        }

        self.attribute_map = {
            'type': 'type',
            'peildatum': 'peildatum',
            'adresseerbaar_object_identificatie': 'adresseerbaarObjectIdentificatie'
        }

        self._type = type
        self._peildatum = peildatum
        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie

    @classmethod
    def from_dict(cls, dikt) -> 'BewoningMetPeildatum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BewoningMetPeildatum of this BewoningMetPeildatum.  # noqa: E501
        :rtype: BewoningMetPeildatum
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this BewoningMetPeildatum.


        :return: The type of this BewoningMetPeildatum.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this BewoningMetPeildatum.


        :param type: The type of this BewoningMetPeildatum.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def peildatum(self) -> date:
        """Gets the peildatum of this BewoningMetPeildatum.


        :return: The peildatum of this BewoningMetPeildatum.
        :rtype: date
        """
        return self._peildatum

    @peildatum.setter
    def peildatum(self, peildatum: date):
        """Sets the peildatum of this BewoningMetPeildatum.


        :param peildatum: The peildatum of this BewoningMetPeildatum.
        :type peildatum: date
        """
        if peildatum is None:
            raise ValueError("Invalid value for `peildatum`, must not be `None`")  # noqa: E501

        self._peildatum = peildatum

    @property
    def adresseerbaar_object_identificatie(self) -> str:
        """Gets the adresseerbaar_object_identificatie of this BewoningMetPeildatum.

        De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)   # noqa: E501

        :return: The adresseerbaar_object_identificatie of this BewoningMetPeildatum.
        :rtype: str
        """
        return self._adresseerbaar_object_identificatie

    @adresseerbaar_object_identificatie.setter
    def adresseerbaar_object_identificatie(self, adresseerbaar_object_identificatie: str):
        """Sets the adresseerbaar_object_identificatie of this BewoningMetPeildatum.

        De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)   # noqa: E501

        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this BewoningMetPeildatum.
        :type adresseerbaar_object_identificatie: str
        """
        if adresseerbaar_object_identificatie is None:
            raise ValueError("Invalid value for `adresseerbaar_object_identificatie`, must not be `None`")  # noqa: E501
        if adresseerbaar_object_identificatie is not None and not re.search(r'^(?!0{16})[0-9]{16}$', adresseerbaar_object_identificatie):  # noqa: E501
            raise ValueError(r"Invalid value for `adresseerbaar_object_identificatie`, must be a follow pattern or equal to `/^(?!0{16})[0-9]{16}$/`")  # noqa: E501

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie
