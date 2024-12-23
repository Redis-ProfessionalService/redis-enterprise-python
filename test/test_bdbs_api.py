# coding: utf-8

"""
    Redis Enterprise API

    REST API Specifications[¶](#rest-api-specifications \"Permalink to this headline\") =================================================================================  Key Concepts[¶](#key-concepts \"Permalink to this headline\") -----------------------------------------------------------  ### Clusters[¶](#clusters \"Permalink to this headline\")  Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.  Protocol and Headers[¶](#protocol-and-headers \"Permalink to this headline\") ---------------------------------------------------------------------------  ### JSON Requests and Responses[¶](#json-requests-and-responses \"Permalink to this headline\")  The Redis Labs REST API uses the JavaScript Object Notation (JSON) for requests and responses.  Some responses may have an empty body, but indicate the response with standard HTTP codes. For more information, see RFC 4627 ([http://www.ietf.org/rfc/rfc4627.txt](http://www.ietf.org/rfc/rfc4627.txt)) and www.json.org.  Both requests and responses may include zero or more objects.  In case the request is for a single entity, the response shall return a single JSON object, or none. In case the request if for a list of entities, the response shall return a single JSON array with 0 or more elements.  Requests may be delivered with some JSON object fields missing. In this case, these fields will be assigned default values (often indicating they are not in use).  ### Request Headers[¶](#request-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Accept | application/json | | Content-Length | Length (in bytes) of request message. | | Content-Type | application/json |   ### Response Headers[¶](#response-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Content-Type | application/json | | Content-Length | Length (in bytes) of request message. |   API Versions[¶](#api-versions \"Permalink to this headline\") -----------------------------------------------------------  All RLEC API operations are versioned, in order to minimize the impact of backwards-incompatible API changes and to coordinate between different versions operating in parallel.  Authentication[¶](#authentication \"Permalink to this headline\") ---------------------------------------------------------------  Authentication to RLEC API occurs via [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide your RLEC username and password as the basic auth credentials.  All calls must be made over SSL, to port 9443.  Example Request:  ```bash curl \\-u \"demo@redislabs.com:password\" https://localhost:9443/v1/bdbs ```  Common Responses[¶](#common-responses \"Permalink to this headline\") -------------------------------------------------------------------  The following are common responses which may be returned in some cases regardless of any specific request.  | Response | Condition / Required handling | |---|---| | 503 (Service Unavailable) | Contacted node is currently not a member of any active cluster. | | 505 (HTTP Version Not Supported) | An unsupported X-API-Version was used, see API Versions above. |   # noqa: E501

    OpenAPI spec version: 6.2.4-55
    Contact: matthew.royal@redis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.bdbs_api import BdbsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBdbsApi(unittest.TestCase):
    """BdbsApi unit test stubs"""

    def setUp(self):
        self.api = BdbsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_v1_bdbs_uid_passwords(self):
        """Test case for delete_v1_bdbs_uid_passwords

        Delete a password from the bdb’s default user  # noqa: E501
        """
        pass

    def test_get_v1_bdbs(self):
        """Test case for get_v1_bdbs

        Get all databases in the cluster.  # noqa: E501
        """
        pass

    def test_get_v1_bdbs_uid(self):
        """Test case for get_v1_bdbs_uid

        Get single database (bdb object) as json.  # noqa: E501
        """
        pass

    def test_get_v1_bdbs_uid_actions_optimize_shards_placement(self):
        """Test case for get_v1_bdbs_uid_actions_optimize_shards_placement

        Get optimized shards placement for the given database.  # noqa: E501
        """
        pass

    def test_get_v1_bdbs_uid_actions_recover(self):
        """Test case for get_v1_bdbs_uid_actions_recover

        Fetch the recovery plan for a database in recovery mode  # noqa: E501
        """
        pass

    def test_post_v1_bdbs(self):
        """Test case for post_v1_bdbs

        Create a new database in the cluster.  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_actions_export(self):
        """Test case for post_v1_bdbs_uid_actions_export

        Initiate a database export.  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_actions_import(self):
        """Test case for post_v1_bdbs_uid_actions_import

        Initiate a manual import process.  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_actions_recover(self):
        """Test case for post_v1_bdbs_uid_actions_recover

        Initiate recovery for a database in recovery state.  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_command(self):
        """Test case for post_v1_bdbs_uid_command

        Execute a redis/memcached command  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_passwords(self):
        """Test case for post_v1_bdbs_uid_passwords

        Add a password to the bdb’s default user  # noqa: E501
        """
        pass

    def test_post_v1_bdbs_uid_upgrade(self):
        """Test case for post_v1_bdbs_uid_upgrade

        Upgrade a BDB  # noqa: E501
        """
        pass

    def test_put_v1_bdbs_uid(self):
        """Test case for put_v1_bdbs_uid

        Update the configuration of an active database.  # noqa: E501
        """
        pass

    def test_put_v1_bdbs_uid_action(self):
        """Test case for put_v1_bdbs_uid_action

        Update the configuration of an active database.  # noqa: E501
        """
        pass

    def test_put_v1_bdbs_uid_actions_backup_reset_status(self):
        """Test case for put_v1_bdbs_uid_actions_backup_reset_status

        Reset database current backup status  # noqa: E501
        """
        pass

    def test_put_v1_bdbs_uid_actions_export_reset_status(self):
        """Test case for put_v1_bdbs_uid_actions_export_reset_status

        Reset database current export status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
