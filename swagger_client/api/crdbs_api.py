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


class CrdbsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v1_crdb(self, **kwargs):  # noqa: E501
        """Get a list of all Active-Active database on the cluster.  # noqa: E501

        Get a list of all Active-Active database on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_crdb(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_task_id: Specified task ID.
        :param int x_result_ttl: Time (in seconds) to keep task result.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_crdb_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_crdb_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_v1_crdb_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of all Active-Active database on the cluster.  # noqa: E501

        Get a list of all Active-Active database on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_crdb_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_task_id: Specified task ID.
        :param int x_result_ttl: Time (in seconds) to keep task result.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_task_id', 'x_result_ttl']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_crdb" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_task_id' in params:
            header_params['X-Task-ID'] = params['x_task_id']  # noqa: E501
        if 'x_result_ttl' in params:
            header_params['X-Result-TTL'] = params['x_result_ttl']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu']  # noqa: E501

        return self.api_client.call_api(
            '/v1/crdbs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v1_crdbs(self, **kwargs):  # noqa: E501
        """Create a new Active-Active database.  # noqa: E501

        Create a new Active-Active database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_crdbs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Crdb body:
        :param str x_task_id: Specified task ID.
        :param int x_result_ttl: Time (in seconds) to keep task result.
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v1_crdbs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_v1_crdbs_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_v1_crdbs_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new Active-Active database.  # noqa: E501

        Create a new Active-Active database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_crdbs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Crdb body:
        :param str x_task_id: Specified task ID.
        :param int x_result_ttl: Time (in seconds) to keep task result.
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_task_id', 'x_result_ttl']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v1_crdbs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_task_id' in params:
            header_params['X-Task-ID'] = params['x_task_id']  # noqa: E501
        if 'x_result_ttl' in params:
            header_params['X-Result-TTL'] = params['x_result_ttl']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu']  # noqa: E501

        return self.api_client.call_api(
            '/v1/crdbs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
