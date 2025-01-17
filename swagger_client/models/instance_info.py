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

class InstanceInfo(object):
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
        'id': 'InstanceId',
        'compression': 'int',
        'cluster': 'ClusterInfo',
        'db_config': 'Bdb',
        'db_uid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'compression': 'compression',
        'cluster': 'cluster',
        'db_config': 'db_config',
        'db_uid': 'db_uid'
    }

    def __init__(self, id=None, compression=3, cluster=None, db_config=None, db_uid=None):  # noqa: E501
        """InstanceInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._compression = None
        self._cluster = None
        self._db_config = None
        self._db_uid = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if compression is not None:
            self.compression = compression
        if cluster is not None:
            self.cluster = cluster
        if db_config is not None:
            self.db_config = db_config
        if db_uid is not None:
            self.db_uid = db_uid

    @property
    def id(self):
        """Gets the id of this InstanceInfo.  # noqa: E501


        :return: The id of this InstanceInfo.  # noqa: E501
        :rtype: InstanceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceInfo.


        :param id: The id of this InstanceInfo.  # noqa: E501
        :type: InstanceId
        """

        self._id = id

    @property
    def compression(self):
        """Gets the compression of this InstanceInfo.  # noqa: E501

        Compression level when syncing from this source.  # noqa: E501

        :return: The compression of this InstanceInfo.  # noqa: E501
        :rtype: int
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this InstanceInfo.

        Compression level when syncing from this source.  # noqa: E501

        :param compression: The compression of this InstanceInfo.  # noqa: E501
        :type: int
        """

        self._compression = compression

    @property
    def cluster(self):
        """Gets the cluster of this InstanceInfo.  # noqa: E501


        :return: The cluster of this InstanceInfo.  # noqa: E501
        :rtype: ClusterInfo
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this InstanceInfo.


        :param cluster: The cluster of this InstanceInfo.  # noqa: E501
        :type: ClusterInfo
        """

        self._cluster = cluster

    @property
    def db_config(self):
        """Gets the db_config of this InstanceInfo.  # noqa: E501


        :return: The db_config of this InstanceInfo.  # noqa: E501
        :rtype: Bdb
        """
        return self._db_config

    @db_config.setter
    def db_config(self, db_config):
        """Sets the db_config of this InstanceInfo.


        :param db_config: The db_config of this InstanceInfo.  # noqa: E501
        :type: Bdb
        """

        self._db_config = db_config

    @property
    def db_uid(self):
        """Gets the db_uid of this InstanceInfo.  # noqa: E501

        ID of local database instance. This field is likely to be empty for instances other than the local one.  # noqa: E501

        :return: The db_uid of this InstanceInfo.  # noqa: E501
        :rtype: str
        """
        return self._db_uid

    @db_uid.setter
    def db_uid(self, db_uid):
        """Sets the db_uid of this InstanceInfo.

        ID of local database instance. This field is likely to be empty for instances other than the local one.  # noqa: E501

        :param db_uid: The db_uid of this InstanceInfo.  # noqa: E501
        :type: str
        """

        self._db_uid = db_uid

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
        if issubclass(InstanceInfo, dict):
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
        if not isinstance(other, InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
