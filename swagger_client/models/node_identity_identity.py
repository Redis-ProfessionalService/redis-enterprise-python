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

class NodeIdentityIdentity(object):
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
        'accept_servers': 'bool',
        'addr': 'str',
        'external_addr': 'list[AnyOfnodeIdentityIdentityExternalAddrItems]',
        'name': 'str',
        'override_rack_id': 'bool',
        'rack_id': 'str',
        'uid': 'int'
    }

    attribute_map = {
        'accept_servers': 'accept_servers',
        'addr': 'addr',
        'external_addr': 'external_addr',
        'name': 'name',
        'override_rack_id': 'override_rack_id',
        'rack_id': 'rack_id',
        'uid': 'uid'
    }

    def __init__(self, accept_servers=True, addr=None, external_addr=None, name=None, override_rack_id=None, rack_id=None, uid=None):  # noqa: E501
        """NodeIdentityIdentity - a model defined in Swagger"""  # noqa: E501
        self._accept_servers = None
        self._addr = None
        self._external_addr = None
        self._name = None
        self._override_rack_id = None
        self._rack_id = None
        self._uid = None
        self.discriminator = None
        if accept_servers is not None:
            self.accept_servers = accept_servers
        if addr is not None:
            self.addr = addr
        if external_addr is not None:
            self.external_addr = external_addr
        if name is not None:
            self.name = name
        if override_rack_id is not None:
            self.override_rack_id = override_rack_id
        if rack_id is not None:
            self.rack_id = rack_id
        if uid is not None:
            self.uid = uid

    @property
    def accept_servers(self):
        """Gets the accept_servers of this NodeIdentityIdentity.  # noqa: E501


        :return: The accept_servers of this NodeIdentityIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._accept_servers

    @accept_servers.setter
    def accept_servers(self, accept_servers):
        """Sets the accept_servers of this NodeIdentityIdentity.


        :param accept_servers: The accept_servers of this NodeIdentityIdentity.  # noqa: E501
        :type: bool
        """

        self._accept_servers = accept_servers

    @property
    def addr(self):
        """Gets the addr of this NodeIdentityIdentity.  # noqa: E501

        Internal IP address of node  # noqa: E501

        :return: The addr of this NodeIdentityIdentity.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this NodeIdentityIdentity.

        Internal IP address of node  # noqa: E501

        :param addr: The addr of this NodeIdentityIdentity.  # noqa: E501
        :type: str
        """

        self._addr = addr

    @property
    def external_addr(self):
        """Gets the external_addr of this NodeIdentityIdentity.  # noqa: E501

        External IP addresses of node. GET /jsonschema to retrieve the object's structure.  # noqa: E501

        :return: The external_addr of this NodeIdentityIdentity.  # noqa: E501
        :rtype: list[AnyOfnodeIdentityIdentityExternalAddrItems]
        """
        return self._external_addr

    @external_addr.setter
    def external_addr(self, external_addr):
        """Sets the external_addr of this NodeIdentityIdentity.

        External IP addresses of node. GET /jsonschema to retrieve the object's structure.  # noqa: E501

        :param external_addr: The external_addr of this NodeIdentityIdentity.  # noqa: E501
        :type: list[AnyOfnodeIdentityIdentityExternalAddrItems]
        """

        self._external_addr = external_addr

    @property
    def name(self):
        """Gets the name of this NodeIdentityIdentity.  # noqa: E501

        Node's name.  # noqa: E501

        :return: The name of this NodeIdentityIdentity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeIdentityIdentity.

        Node's name.  # noqa: E501

        :param name: The name of this NodeIdentityIdentity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def override_rack_id(self):
        """Gets the override_rack_id of this NodeIdentityIdentity.  # noqa: E501

        When replacing an existing node in a rack aware cluster, allows the new node to be located in a different rack.  # noqa: E501

        :return: The override_rack_id of this NodeIdentityIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._override_rack_id

    @override_rack_id.setter
    def override_rack_id(self, override_rack_id):
        """Sets the override_rack_id of this NodeIdentityIdentity.

        When replacing an existing node in a rack aware cluster, allows the new node to be located in a different rack.  # noqa: E501

        :param override_rack_id: The override_rack_id of this NodeIdentityIdentity.  # noqa: E501
        :type: bool
        """

        self._override_rack_id = override_rack_id

    @property
    def rack_id(self):
        """Gets the rack_id of this NodeIdentityIdentity.  # noqa: E501

        Rack id, overrides cloud config.  # noqa: E501

        :return: The rack_id of this NodeIdentityIdentity.  # noqa: E501
        :rtype: str
        """
        return self._rack_id

    @rack_id.setter
    def rack_id(self, rack_id):
        """Sets the rack_id of this NodeIdentityIdentity.

        Rack id, overrides cloud config.  # noqa: E501

        :param rack_id: The rack_id of this NodeIdentityIdentity.  # noqa: E501
        :type: str
        """

        self._rack_id = rack_id

    @property
    def uid(self):
        """Gets the uid of this NodeIdentityIdentity.  # noqa: E501

        Assumed node's uid, for cluster joining. Used to replace a dead node with a new one.  # noqa: E501

        :return: The uid of this NodeIdentityIdentity.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodeIdentityIdentity.

        Assumed node's uid, for cluster joining. Used to replace a dead node with a new one.  # noqa: E501

        :param uid: The uid of this NodeIdentityIdentity.  # noqa: E501
        :type: int
        """

        self._uid = uid

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
        if issubclass(NodeIdentityIdentity, dict):
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
        if not isinstance(other, NodeIdentityIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other