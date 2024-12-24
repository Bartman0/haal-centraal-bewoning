from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.bewoning_api.models.base_model import Model
from brp.bewoning_api.models.bewoningen_query import BewoningenQuery
import re
from brp.bewoning_api import util

from brp.bewoning_api.models.bewoningen_query import BewoningenQuery  # noqa: E501
import re  # noqa: E501

class BewoningMetPeriode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, datum_van=None, datum_tot=None, adresseerbaar_object_identificatie=None):  # noqa: E501
        """BewoningMetPeriode - a model defined in OpenAPI

        :param type: The type of this BewoningMetPeriode.  # noqa: E501
        :type type: str
        :param datum_van: The datum_van of this BewoningMetPeriode.  # noqa: E501
        :type datum_van: date
        :param datum_tot: The datum_tot of this BewoningMetPeriode.  # noqa: E501
        :type datum_tot: date
        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this BewoningMetPeriode.  # noqa: E501
        :type adresseerbaar_object_identificatie: str
        """
        self.openapi_types = {
            'type': str,
            'datum_van': date,
            'datum_tot': date,
            'adresseerbaar_object_identificatie': str
        }

        self.attribute_map = {
            'type': 'type',
            'datum_van': 'datumVan',
            'datum_tot': 'datumTot',
            'adresseerbaar_object_identificatie': 'adresseerbaarObjectIdentificatie'
        }

        self._type = type
        self._datum_van = datum_van
        self._datum_tot = datum_tot
        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie

    @classmethod
    def from_dict(cls, dikt) -> 'BewoningMetPeriode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BewoningMetPeriode of this BewoningMetPeriode.  # noqa: E501
        :rtype: BewoningMetPeriode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this BewoningMetPeriode.


        :return: The type of this BewoningMetPeriode.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this BewoningMetPeriode.


        :param type: The type of this BewoningMetPeriode.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def datum_van(self) -> date:
        """Gets the datum_van of this BewoningMetPeriode.


        :return: The datum_van of this BewoningMetPeriode.
        :rtype: date
        """
        return self._datum_van

    @datum_van.setter
    def datum_van(self, datum_van: date):
        """Sets the datum_van of this BewoningMetPeriode.


        :param datum_van: The datum_van of this BewoningMetPeriode.
        :type datum_van: date
        """
        if datum_van is None:
            raise ValueError("Invalid value for `datum_van`, must not be `None`")  # noqa: E501

        self._datum_van = datum_van

    @property
    def datum_tot(self) -> date:
        """Gets the datum_tot of this BewoningMetPeriode.


        :return: The datum_tot of this BewoningMetPeriode.
        :rtype: date
        """
        return self._datum_tot

    @datum_tot.setter
    def datum_tot(self, datum_tot: date):
        """Sets the datum_tot of this BewoningMetPeriode.


        :param datum_tot: The datum_tot of this BewoningMetPeriode.
        :type datum_tot: date
        """
        if datum_tot is None:
            raise ValueError("Invalid value for `datum_tot`, must not be `None`")  # noqa: E501

        self._datum_tot = datum_tot

    @property
    def adresseerbaar_object_identificatie(self) -> str:
        """Gets the adresseerbaar_object_identificatie of this BewoningMetPeriode.

        De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)   # noqa: E501

        :return: The adresseerbaar_object_identificatie of this BewoningMetPeriode.
        :rtype: str
        """
        return self._adresseerbaar_object_identificatie

    @adresseerbaar_object_identificatie.setter
    def adresseerbaar_object_identificatie(self, adresseerbaar_object_identificatie: str):
        """Sets the adresseerbaar_object_identificatie of this BewoningMetPeriode.

        De identificatiecode van een adresseerbaar object uitgezonderd de standaardwaarde (0000000000000000)   # noqa: E501

        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this BewoningMetPeriode.
        :type adresseerbaar_object_identificatie: str
        """
        if adresseerbaar_object_identificatie is None:
            raise ValueError("Invalid value for `adresseerbaar_object_identificatie`, must not be `None`")  # noqa: E501
        if adresseerbaar_object_identificatie is not None and not re.search(r'^(?!0{16})[0-9]{16}$', adresseerbaar_object_identificatie):  # noqa: E501
            raise ValueError(r"Invalid value for `adresseerbaar_object_identificatie`, must be a follow pattern or equal to `/^(?!0{16})[0-9]{16}$/`")  # noqa: E501

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie