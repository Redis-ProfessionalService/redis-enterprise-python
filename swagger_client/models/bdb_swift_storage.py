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

class BdbSwiftStorage(object):
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
        'auth_url': 'str',
        'container': 'str',
        'key': 'str',
        'prefix': 'str',
        'type': 'str',
        'user': 'str'
    }

    attribute_map = {
        'auth_url': 'auth_url',
        'container': 'container',
        'key': 'key',
        'prefix': 'prefix',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, auth_url=None, container=None, key=None, prefix=None, type=None, user=None):  # noqa: E501
        """BdbSwiftStorage - a model defined in Swagger"""  # noqa: E501
        self._auth_url = None
        self._container = None
        self._key = None
        self._prefix = None
        self._type = None
        self._user = None
        self.discriminator = None
        if auth_url is not None:
            self.auth_url = auth_url
        if container is not None:
            self.container = container
        if key is not None:
            self.key = key
        if prefix is not None:
            self.prefix = prefix
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def auth_url(self):
        """Gets the auth_url of this BdbSwiftStorage.  # noqa: E501

        Swift service authentication URL.  # noqa: E501

        :return: The auth_url of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this BdbSwiftStorage.

        Swift service authentication URL.  # noqa: E501

        :param auth_url: The auth_url of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """

        self._auth_url = auth_url

    @property
    def container(self):
        """Gets the container of this BdbSwiftStorage.  # noqa: E501

        Swift object store container for storing the backup files.  # noqa: E501

        :return: The container of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this BdbSwiftStorage.

        Swift object store container for storing the backup files.  # noqa: E501

        :param container: The container of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def key(self):
        """Gets the key of this BdbSwiftStorage.  # noqa: E501

        Swift service access key.  # noqa: E501

        :return: The key of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this BdbSwiftStorage.

        Swift service access key.  # noqa: E501

        :param key: The key of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def prefix(self):
        """Gets the prefix of this BdbSwiftStorage.  # noqa: E501

        Optional. Prefix (path) of backup files in the swift container.  # noqa: E501

        :return: The prefix of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this BdbSwiftStorage.

        Optional. Prefix (path) of backup files in the swift container.  # noqa: E501

        :param prefix: The prefix of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def type(self):
        """Gets the type of this BdbSwiftStorage.  # noqa: E501


        :return: The type of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BdbSwiftStorage.


        :param type: The type of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """
        allowed_values = ["swift"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user(self):
        """Gets the user of this BdbSwiftStorage.  # noqa: E501

        Swift service user name (pattern does not allow special characters &,<,>,\\\")  # noqa: E501

        :return: The user of this BdbSwiftStorage.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BdbSwiftStorage.

        Swift service user name (pattern does not allow special characters &,<,>,\\\")  # noqa: E501

        :param user: The user of this BdbSwiftStorage.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(BdbSwiftStorage, dict):
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
        if not isinstance(other, BdbSwiftStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
