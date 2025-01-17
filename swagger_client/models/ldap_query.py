# coding: utf-8

"""
    Redis Enterprise API

    REST API Specifications[¶](#rest-api-specifications \"Permalink to this headline\") =================================================================================  Key Concepts[¶](#key-concepts \"Permalink to this headline\") -----------------------------------------------------------  ### Clusters[¶](#clusters \"Permalink to this headline\")  Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.  Protocol and Headers[¶](#protocol-and-headers \"Permalink to this headline\") ---------------------------------------------------------------------------  ### JSON Requests and Responses[¶](#json-requests-and-responses \"Permalink to this headline\")  The Redis Labs REST API uses the JavaScript Object Notation (JSON) for requests and responses.  Some responses may have an empty body, but indicate the response with standard HTTP codes. For more information, see RFC 4627 ([http://www.ietf.org/rfc/rfc4627.txt](http://www.ietf.org/rfc/rfc4627.txt)) and www.json.org.  Both requests and responses may include zero or more objects.  In case the request is for a single entity, the response shall return a single JSON object, or none. In case the request if for a list of entities, the response shall return a single JSON array with 0 or more elements.  Requests may be delivered with some JSON object fields missing. In this case, these fields will be assigned default values (often indicating they are not in use).  ### Request Headers[¶](#request-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Accept | application/json | | Content-Length | Length (in bytes) of request message. | | Content-Type | application/json |   ### Response Headers[¶](#response-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Content-Type | application/json | | Content-Length | Length (in bytes) of request message. |   API Versions[¶](#api-versions \"Permalink to this headline\") -----------------------------------------------------------  All RLEC API operations are versioned, in order to minimize the impact of backwards-incompatible API changes and to coordinate between different versions operating in parallel.  Authentication[¶](#authentication \"Permalink to this headline\") ---------------------------------------------------------------  Authentication to RLEC API occurs via [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide your RLEC username and password as the basic auth credentials.  All calls must be made over SSL, to port 9443.  Example Request:  ```bash curl \\-u \"demo@redislabs.com:password\" https://localhost:9443/v1/bdbs ```  Common Responses[¶](#common-responses \"Permalink to this headline\") -------------------------------------------------------------------  The following are common responses which may be returned in some cases regardless of any specific request.  | Response | Condition / Required handling | |---|---| | 503 (Service Unavailable) | Contacted node is currently not a member of any active cluster. | | 505 (HTTP Version Not Supported) | An unsupported X-API-Version was used, see API Versions above. |   # noqa: E501

    OpenAPI spec version: 6.2.4-55
    Contact: matthew.royal@redis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LdapQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base': 'str',
        'filter': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'base': 'base',
        'filter': 'filter',
        'scope': 'scope'
    }

    def __init__(self, base=None, filter=None, scope=None):  # noqa: E501
        """LdapQuery - a model defined in Swagger"""  # noqa: E501
        self._base = None
        self._filter = None
        self._scope = None
        self.discriminator = None
        if base is not None:
            self.base = base
        if filter is not None:
            self.filter = filter
        if scope is not None:
            self.scope = scope

    @property
    def base(self):
        """Gets the base of this LdapQuery.  # noqa: E501

        The DN of the entry at which to start the search  # noqa: E501

        :return: The base of this LdapQuery.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this LdapQuery.

        The DN of the entry at which to start the search  # noqa: E501

        :param base: The base of this LdapQuery.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def filter(self):
        """Gets the filter of this LdapQuery.  # noqa: E501

        An RFC-4515 string representation of the filter to apply in the search  # noqa: E501

        :return: The filter of this LdapQuery.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this LdapQuery.

        An RFC-4515 string representation of the filter to apply in the search  # noqa: E501

        :param filter: The filter of this LdapQuery.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def scope(self):
        """Gets the scope of this LdapQuery.  # noqa: E501

        One of \"base\" (to search the base object itself), \"one\" (to search the base object's immediate children), or \"subtree\" (to search the base object and all its descendants)  # noqa: E501

        :return: The scope of this LdapQuery.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this LdapQuery.

        One of \"base\" (to search the base object itself), \"one\" (to search the base object's immediate children), or \"subtree\" (to search the base object and all its descendants)  # noqa: E501

        :param scope: The scope of this LdapQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["base", "one", "subtree"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LdapQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LdapQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
