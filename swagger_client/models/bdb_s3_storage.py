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

class BdbS3Storage(object):
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
        'access_key_id': 'str',
        'bucket_name': 'str',
        'secret_access_key': 'str',
        'subdir': 'str',
        'type': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'bucket_name': 'bucket_name',
        'secret_access_key': 'secret_access_key',
        'subdir': 'subdir',
        'type': 'type'
    }

    def __init__(self, access_key_id=None, bucket_name=None, secret_access_key=None, subdir=None, type=None):  # noqa: E501
        """BdbS3Storage - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._bucket_name = None
        self._secret_access_key = None
        self._subdir = None
        self._type = None
        self.discriminator = None
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if subdir is not None:
            self.subdir = subdir
        if type is not None:
            self.type = type

    @property
    def access_key_id(self):
        """Gets the access_key_id of this BdbS3Storage.  # noqa: E501

        Amazon S3 Access Key ID.  # noqa: E501

        :return: The access_key_id of this BdbS3Storage.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this BdbS3Storage.

        Amazon S3 Access Key ID.  # noqa: E501

        :param access_key_id: The access_key_id of this BdbS3Storage.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this BdbS3Storage.  # noqa: E501

        Amazon S3 bucket name.  # noqa: E501

        :return: The bucket_name of this BdbS3Storage.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this BdbS3Storage.

        Amazon S3 bucket name.  # noqa: E501

        :param bucket_name: The bucket_name of this BdbS3Storage.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this BdbS3Storage.  # noqa: E501

        Amazon S3 Secret Access Key.  # noqa: E501

        :return: The secret_access_key of this BdbS3Storage.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this BdbS3Storage.

        Amazon S3 Secret Access Key.  # noqa: E501

        :param secret_access_key: The secret_access_key of this BdbS3Storage.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def subdir(self):
        """Gets the subdir of this BdbS3Storage.  # noqa: E501

        Optional. Amazon S3 subdir under bucket.  # noqa: E501

        :return: The subdir of this BdbS3Storage.  # noqa: E501
        :rtype: str
        """
        return self._subdir

    @subdir.setter
    def subdir(self, subdir):
        """Sets the subdir of this BdbS3Storage.

        Optional. Amazon S3 subdir under bucket.  # noqa: E501

        :param subdir: The subdir of this BdbS3Storage.  # noqa: E501
        :type: str
        """

        self._subdir = subdir

    @property
    def type(self):
        """Gets the type of this BdbS3Storage.  # noqa: E501


        :return: The type of this BdbS3Storage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BdbS3Storage.


        :param type: The type of this BdbS3Storage.  # noqa: E501
        :type: str
        """
        allowed_values = ["s3"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(BdbS3Storage, dict):
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
        if not isinstance(other, BdbS3Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
