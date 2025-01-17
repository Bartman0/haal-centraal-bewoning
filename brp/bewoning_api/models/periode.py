from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.bewoning_api.models.base_model import Model
from brp.bewoning_api import util


class Periode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datum_van=None, datum_tot=None):  # noqa: E501
        """Periode - a model defined in OpenAPI

        :param datum_van: The datum_van of this Periode.  # noqa: E501
        :type datum_van: date
        :param datum_tot: The datum_tot of this Periode.  # noqa: E501
        :type datum_tot: date
        """
        self.openapi_types = {
            'datum_van': date,
            'datum_tot': date
        }

        self.attribute_map = {
            'datum_van': 'datumVan',
            'datum_tot': 'datumTot'
        }

        self._datum_van = datum_van
        self._datum_tot = datum_tot

    @classmethod
    def from_dict(cls, dikt) -> 'Periode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Periode of this Periode.  # noqa: E501
        :rtype: Periode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datum_van(self) -> date:
        """Gets the datum_van of this Periode.

        De begindatum van de periode.   # noqa: E501

        :return: The datum_van of this Periode.
        :rtype: date
        """
        return self._datum_van

    @datum_van.setter
    def datum_van(self, datum_van: date):
        """Sets the datum_van of this Periode.

        De begindatum van de periode.   # noqa: E501

        :param datum_van: The datum_van of this Periode.
        :type datum_van: date
        """

        self._datum_van = datum_van

    @property
    def datum_tot(self) -> date:
        """Gets the datum_tot of this Periode.

        De einddatum van de periode.   # noqa: E501

        :return: The datum_tot of this Periode.
        :rtype: date
        """
        return self._datum_tot

    @datum_tot.setter
    def datum_tot(self, datum_tot: date):
        """Sets the datum_tot of this Periode.

        De einddatum van de periode.   # noqa: E501

        :param datum_tot: The datum_tot of this Periode.
        :type datum_tot: date
        """

        self._datum_tot = datum_tot
