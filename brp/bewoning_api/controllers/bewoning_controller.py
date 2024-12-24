import os
import sys
import json
from http import HTTPStatus
import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from brp.bewoning_api.models.bad_request_foutbericht import (
    BadRequestFoutbericht,
)  # noqa: E501
from brp.bewoning_api.models.bewoningen_query import BewoningenQuery  # noqa: E501
from brp.bewoning_api.models.bewoningen_query_response import (
    BewoningenQueryResponse,
)  # noqa: E501
from brp.bewoning_api.models.foutbericht import Foutbericht  # noqa: E501
from brp.bewoning_api import util

import brp_bewoning_client

import pprint

pp = pprint.PrettyPrinter(indent=4, stream=sys.stderr)

configuration = brp_bewoning_client.Configuration(
    host=os.getenv("BRP_BEWONING_URL", "http://localhost"),
)


def bewoningen(bewoningen_query=None):  # noqa: E501
    """Raadplegen van bewoningen

    Met de API kun je raadplegen:  **Bewoning:** welke personen (bewoners) een adresseerbaar object bewoonden op een opgegeven moment (peildatum) of welke samenstellingen van personen een adresseerbaar object bewoonden in een opgegeven periode.  # noqa: E501

    :param bewoningen_query:
    :type bewoningen_query: dict | bytes

    :rtype: Union[BewoningenQueryResponse, Tuple[BewoningenQueryResponse, int], Tuple[BewoningenQueryResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        bewoningen_query = BewoningenQuery.from_dict(
            connexion.request.get_json()
        )  # noqa: E501

    # TODO: make this more direct than converting through JSON and back again
    try:
        bewoningen_query = brp_bewoning_client.BewoningenQuery.from_dict(
            connexion.request.get_json()
        )
    except Exception as e:
        return {
            "detail": str(e),
            "status": HTTPStatus.BAD_REQUEST,
            "title": str(type(e)),
        }, HTTPStatus.BAD_REQUEST

    with brp_bewoning_client.ApiClient(
        configuration=configuration,
        header_name="X-API-Key",
        header_value=os.getenv("BRP_BEWONING_API_KEY", ""),
    ) as api_client:
        try:
            api_instance = brp_bewoning_client.BewoningApi(api_client)
            api_response = api_instance.bewoningen(bewoningen_query=bewoningen_query)
            return api_response.to_dict(), HTTPStatus.OK
        except brp_bewoning_client.ApiException as ae:
            return json.loads(ae.body), ae.status
