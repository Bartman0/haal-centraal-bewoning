from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.bewoning_api.models.base_model import Model
from brp.bewoning_api.models.bewoner import Bewoner
from brp.bewoning_api.models.periode import Periode
import re
from brp.bewoning_api import util

from brp.bewoning_api.models.bewoner import Bewoner  # noqa: E501
from brp.bewoning_api.models.periode import Periode  # noqa: E501
import re  # noqa: E501

class Bewoning(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, adresseerbaar_object_identificatie=None, periode=None, bewoners=None, mogelijke_bewoners=None, indicatie_veel_bewoners=None):  # noqa: E501
        """Bewoning - a model defined in OpenAPI

        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this Bewoning.  # noqa: E501
        :type adresseerbaar_object_identificatie: str
        :param periode: The periode of this Bewoning.  # noqa: E501
        :type periode: Periode
        :param bewoners: The bewoners of this Bewoning.  # noqa: E501
        :type bewoners: List[Bewoner]
        :param mogelijke_bewoners: The mogelijke_bewoners of this Bewoning.  # noqa: E501
        :type mogelijke_bewoners: List[Bewoner]
        :param indicatie_veel_bewoners: The indicatie_veel_bewoners of this Bewoning.  # noqa: E501
        :type indicatie_veel_bewoners: bool
        """
        self.openapi_types = {
            'adresseerbaar_object_identificatie': str,
            'periode': Periode,
            'bewoners': List[Bewoner],
            'mogelijke_bewoners': List[Bewoner],
            'indicatie_veel_bewoners': bool
        }

        self.attribute_map = {
            'adresseerbaar_object_identificatie': 'adresseerbaarObjectIdentificatie',
            'periode': 'periode',
            'bewoners': 'bewoners',
            'mogelijke_bewoners': 'mogelijkeBewoners',
            'indicatie_veel_bewoners': 'indicatieVeelBewoners'
        }

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie
        self._periode = periode
        self._bewoners = bewoners
        self._mogelijke_bewoners = mogelijke_bewoners
        self._indicatie_veel_bewoners = indicatie_veel_bewoners

    @classmethod
    def from_dict(cls, dikt) -> 'Bewoning':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bewoning of this Bewoning.  # noqa: E501
        :rtype: Bewoning
        """
        return util.deserialize_model(dikt, cls)

    @property
    def adresseerbaar_object_identificatie(self) -> str:
        """Gets the adresseerbaar_object_identificatie of this Bewoning.

        De identificatiecode van een adresseerbaar object.   # noqa: E501

        :return: The adresseerbaar_object_identificatie of this Bewoning.
        :rtype: str
        """
        return self._adresseerbaar_object_identificatie

    @adresseerbaar_object_identificatie.setter
    def adresseerbaar_object_identificatie(self, adresseerbaar_object_identificatie: str):
        """Sets the adresseerbaar_object_identificatie of this Bewoning.

        De identificatiecode van een adresseerbaar object.   # noqa: E501

        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this Bewoning.
        :type adresseerbaar_object_identificatie: str
        """
        if adresseerbaar_object_identificatie is not None and not re.search(r'^[0-9]{16}$', adresseerbaar_object_identificatie):  # noqa: E501
            raise ValueError(r"Invalid value for `adresseerbaar_object_identificatie`, must be a follow pattern or equal to `/^[0-9]{16}$/`")  # noqa: E501

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie

    @property
    def periode(self) -> Periode:
        """Gets the periode of this Bewoning.


        :return: The periode of this Bewoning.
        :rtype: Periode
        """
        return self._periode

    @periode.setter
    def periode(self, periode: Periode):
        """Sets the periode of this Bewoning.


        :param periode: The periode of this Bewoning.
        :type periode: Periode
        """

        self._periode = periode

    @property
    def bewoners(self) -> List[Bewoner]:
        """Gets the bewoners of this Bewoning.

        De personen die in de bewoning periode staan ingeschreven op het adresseerbaar object.   # noqa: E501

        :return: The bewoners of this Bewoning.
        :rtype: List[Bewoner]
        """
        return self._bewoners

    @bewoners.setter
    def bewoners(self, bewoners: List[Bewoner]):
        """Sets the bewoners of this Bewoning.

        De personen die in de bewoning periode staan ingeschreven op het adresseerbaar object.   # noqa: E501

        :param bewoners: The bewoners of this Bewoning.
        :type bewoners: List[Bewoner]
        """
        if bewoners is not None and len(bewoners) > 100:
            raise ValueError("Invalid value for `bewoners`, number of items must be less than or equal to `100`")  # noqa: E501
        if bewoners is not None and len(bewoners) < 0:
            raise ValueError("Invalid value for `bewoners`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._bewoners = bewoners

    @property
    def mogelijke_bewoners(self) -> List[Bewoner]:
        """Gets the mogelijke_bewoners of this Bewoning.

        De personen die in de bewoning periode mogelijk staan ingeschreven op het adresseerbaar object.   # noqa: E501

        :return: The mogelijke_bewoners of this Bewoning.
        :rtype: List[Bewoner]
        """
        return self._mogelijke_bewoners

    @mogelijke_bewoners.setter
    def mogelijke_bewoners(self, mogelijke_bewoners: List[Bewoner]):
        """Sets the mogelijke_bewoners of this Bewoning.

        De personen die in de bewoning periode mogelijk staan ingeschreven op het adresseerbaar object.   # noqa: E501

        :param mogelijke_bewoners: The mogelijke_bewoners of this Bewoning.
        :type mogelijke_bewoners: List[Bewoner]
        """
        if mogelijke_bewoners is not None and len(mogelijke_bewoners) > 100:
            raise ValueError("Invalid value for `mogelijke_bewoners`, number of items must be less than or equal to `100`")  # noqa: E501
        if mogelijke_bewoners is not None and len(mogelijke_bewoners) < 0:
            raise ValueError("Invalid value for `mogelijke_bewoners`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._mogelijke_bewoners = mogelijke_bewoners

    @property
    def indicatie_veel_bewoners(self) -> bool:
        """Gets the indicatie_veel_bewoners of this Bewoning.

        Geeft aan dat de bewoning in totaal meer dan 100 bewoners en/of mogelijke bewoners heeft.   # noqa: E501

        :return: The indicatie_veel_bewoners of this Bewoning.
        :rtype: bool
        """
        return self._indicatie_veel_bewoners

    @indicatie_veel_bewoners.setter
    def indicatie_veel_bewoners(self, indicatie_veel_bewoners: bool):
        """Sets the indicatie_veel_bewoners of this Bewoning.

        Geeft aan dat de bewoning in totaal meer dan 100 bewoners en/of mogelijke bewoners heeft.   # noqa: E501

        :param indicatie_veel_bewoners: The indicatie_veel_bewoners of this Bewoning.
        :type indicatie_veel_bewoners: bool
        """

        self._indicatie_veel_bewoners = indicatie_veel_bewoners