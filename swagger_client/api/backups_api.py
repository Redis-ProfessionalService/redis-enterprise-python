# coding: utf-8

"""
    Redis Enterprise API

    REST API Specifications[¶](#rest-api-specifications \"Permalink to this headline\") =================================================================================  Key Concepts[¶](#key-concepts \"Permalink to this headline\") -----------------------------------------------------------  ### Clusters[¶](#clusters \"Permalink to this headline\")  Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.  Protocol and Headers[¶](#protocol-and-headers \"Permalink to this headline\") ---------------------------------------------------------------------------  ### JSON Requests and Responses[¶](#json-requests-and-responses \"Permalink to this headline\")  The Redis Labs REST API uses the JavaScript Object Notation (JSON) for requests and responses.  Some responses may have an empty body, but indicate the response with standard HTTP codes. For more information, see RFC 4627 ([http://www.ietf.org/rfc/rfc4627.txt](http://www.ietf.org/rfc/rfc4627.txt)) and www.json.org.  Both requests and responses may include zero or more objects.  In case the request is for a single entity, the response shall return a single JSON object, or none. In case the request if for a list of entities, the response shall return a single JSON array with 0 or more elements.  Requests may be delivered with some JSON object fields missing. In this case, these fields will be assigned default values (often indicating they are not in use).  ### Request Headers[¶](#request-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Accept | application/json | | Content-Length | Length (in bytes) of request message. | | Content-Type | application/json |   ### Response Headers[¶](#response-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Content-Type | application/json | | Content-Length | Length (in bytes) of request message. |   API Versions[¶](#api-versions \"Permalink to this headline\") -----------------------------------------------------------  All RLEC API operations are versioned, in order to minimize the impact of backwards-incompatible API changes and to coordinate between different versions operating in parallel.  Authentication[¶](#authentication \"Permalink to this headline\") ---------------------------------------------------------------  Authentication to RLEC API occurs via [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide your RLEC username and password as the basic auth credentials.  All calls must be made over SSL, to port 9443.  Example Request:  ```bash curl \\-u \"demo@redislabs.com:password\" https://localhost:9443/v1/bdbs ```  Common Responses[¶](#common-responses \"Permalink to this headline\") -------------------------------------------------------------------  The following are common responses which may be returned in some cases regardless of any specific request.  | Response | Condition / Required handling | |---|---| | 503 (Service Unavailable) | Contacted node is currently not a member of any active cluster. | | 505 (HTTP Version Not Supported) | An unsupported X-API-Version was used, see API Versions above. |   # noqa: E501

    OpenAPI spec version: 6.2.4-55
    Contact: matthew.royal@redis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BackupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def put_v1_bdbs_uid_actions_backup_reset_status(self, uid, **kwargs):  # noqa: E501
        """Reset database current backup status  # noqa: E501

        Reset database current backup status (backup_status) to idle if not in progress. As well clear exiting backup_failure_reason if exits  The above request resets backup_status to idle value and clear failure reason message if exist from backup_failure_reason.  | Required permissions | |---| | reset_bdb_current_backup_status |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_v1_bdbs_uid_actions_backup_reset_status(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: The unique ID of the database (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_v1_bdbs_uid_actions_backup_reset_status_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.put_v1_bdbs_uid_actions_backup_reset_status_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def put_v1_bdbs_uid_actions_backup_reset_status_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Reset database current backup status  # noqa: E501

        Reset database current backup status (backup_status) to idle if not in progress. As well clear exiting backup_failure_reason if exits  The above request resets backup_status to idle value and clear failure reason message if exist from backup_failure_reason.  | Required permissions | |---| | reset_bdb_current_backup_status |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_v1_bdbs_uid_actions_backup_reset_status_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: The unique ID of the database (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_v1_bdbs_uid_actions_backup_reset_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `put_v1_bdbs_uid_actions_backup_reset_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu']  # noqa: E501

        return self.api_client.call_api(
            '/v1/bdbs/{uid}/actions/backup_reset_status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
