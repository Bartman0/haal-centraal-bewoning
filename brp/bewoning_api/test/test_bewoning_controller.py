import unittest

from flask import json

from brp.bewoning_api.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from brp.bewoning_api.models.bewoningen_query import BewoningenQuery  # noqa: E501
from brp.bewoning_api.models.bewoningen_query_response import BewoningenQueryResponse  # noqa: E501
from brp.bewoning_api.models.foutbericht import Foutbericht  # noqa: E501
from brp.bewoning_api.test import BaseTestCase


class TestBewoningController(BaseTestCase):
    """BewoningController integration test stubs"""

    @unittest.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
    def test_bewoningen(self):
        """Test case for bewoningen

        Raadplegen van bewoningen
        """
        bewoningen_query = brp.bewoning_api.BewoningenQuery()
        headers = { 
            'Accept': 'application/problem+json',
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = self.client.open(
            '/bewoningen',
            method='POST',
            headers=headers,
            data=json.dumps(bewoningen_query),
            content_type='application/json; charset=utf-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
