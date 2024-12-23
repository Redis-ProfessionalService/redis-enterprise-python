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

class User(object):
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
        'account_id': 'int',
        'action_uid': 'str',
        'auth_method': 'str',
        'bdbs_email_alerts': 'AnyOfuserBdbsEmailAlerts',
        'cluster_email_alerts': 'bool',
        'email': 'str',
        'email_alerts': 'bool',
        'name': 'str',
        'password': 'str',
        'password_hashing_method': 'int',
        'password_issue_date': 'datetime',
        'role': 'str',
        'role_uids': 'list[int]'
    }

    attribute_map = {
        'account_id': 'account_id',
        'action_uid': 'action_uid',
        'auth_method': 'auth_method',
        'bdbs_email_alerts': 'bdbs_email_alerts',
        'cluster_email_alerts': 'cluster_email_alerts',
        'email': 'email',
        'email_alerts': 'email_alerts',
        'name': 'name',
        'password': 'password',
        'password_hashing_method': 'password_hashing_method',
        'password_issue_date': 'password_issue_date',
        'role': 'role',
        'role_uids': 'role_uids'
    }

    def __init__(self, account_id=None, action_uid=None, auth_method='regular', bdbs_email_alerts=None, cluster_email_alerts=None, email=None, email_alerts=True, name=None, password=None, password_hashing_method=None, password_issue_date=None, role='db_viewer', role_uids=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._action_uid = None
        self._auth_method = None
        self._bdbs_email_alerts = None
        self._cluster_email_alerts = None
        self._email = None
        self._email_alerts = None
        self._name = None
        self._password = None
        self._password_hashing_method = None
        self._password_issue_date = None
        self._role = None
        self._role_uids = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if action_uid is not None:
            self.action_uid = action_uid
        if auth_method is not None:
            self.auth_method = auth_method
        if bdbs_email_alerts is not None:
            self.bdbs_email_alerts = bdbs_email_alerts
        if cluster_email_alerts is not None:
            self.cluster_email_alerts = cluster_email_alerts
        if email is not None:
            self.email = email
        if email_alerts is not None:
            self.email_alerts = email_alerts
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if password_hashing_method is not None:
            self.password_hashing_method = password_hashing_method
        if password_issue_date is not None:
            self.password_issue_date = password_issue_date
        if role is not None:
            self.role = role
        if role_uids is not None:
            self.role_uids = role_uids

    @property
    def account_id(self):
        """Gets the account_id of this User.  # noqa: E501

        SM account ID  # noqa: E501

        :return: The account_id of this User.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this User.

        SM account ID  # noqa: E501

        :param account_id: The account_id of this User.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def action_uid(self):
        """Gets the action_uid of this User.  # noqa: E501

        Action uid. If exists - progress can be tracked by the GET /actions/<uid> API  # noqa: E501

        :return: The action_uid of this User.  # noqa: E501
        :rtype: str
        """
        return self._action_uid

    @action_uid.setter
    def action_uid(self, action_uid):
        """Sets the action_uid of this User.

        Action uid. If exists - progress can be tracked by the GET /actions/<uid> API  # noqa: E501

        :param action_uid: The action_uid of this User.  # noqa: E501
        :type: str
        """

        self._action_uid = action_uid

    @property
    def auth_method(self):
        """Gets the auth_method of this User.  # noqa: E501

        User's authentication method.  # noqa: E501

        :return: The auth_method of this User.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this User.

        User's authentication method.  # noqa: E501

        :param auth_method: The auth_method of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["regular", "external"]  # noqa: E501
        if auth_method not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_method` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_method, allowed_values)
            )

        self._auth_method = auth_method

    @property
    def bdbs_email_alerts(self):
        """Gets the bdbs_email_alerts of this User.  # noqa: E501

        UIDs of databases that user will receive alerts for.  # noqa: E501

        :return: The bdbs_email_alerts of this User.  # noqa: E501
        :rtype: AnyOfuserBdbsEmailAlerts
        """
        return self._bdbs_email_alerts

    @bdbs_email_alerts.setter
    def bdbs_email_alerts(self, bdbs_email_alerts):
        """Sets the bdbs_email_alerts of this User.

        UIDs of databases that user will receive alerts for.  # noqa: E501

        :param bdbs_email_alerts: The bdbs_email_alerts of this User.  # noqa: E501
        :type: AnyOfuserBdbsEmailAlerts
        """

        self._bdbs_email_alerts = bdbs_email_alerts

    @property
    def cluster_email_alerts(self):
        """Gets the cluster_email_alerts of this User.  # noqa: E501

        Activate cluster email alerts for a user.  # noqa: E501

        :return: The cluster_email_alerts of this User.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_email_alerts

    @cluster_email_alerts.setter
    def cluster_email_alerts(self, cluster_email_alerts):
        """Sets the cluster_email_alerts of this User.

        Activate cluster email alerts for a user.  # noqa: E501

        :param cluster_email_alerts: The cluster_email_alerts of this User.  # noqa: E501
        :type: bool
        """

        self._cluster_email_alerts = cluster_email_alerts

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        User's email. (pattern matching only ascii characters)  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        User's email. (pattern matching only ascii characters)  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_alerts(self):
        """Gets the email_alerts of this User.  # noqa: E501

        Activate email alerts for a user.  # noqa: E501

        :return: The email_alerts of this User.  # noqa: E501
        :rtype: bool
        """
        return self._email_alerts

    @email_alerts.setter
    def email_alerts(self, email_alerts):
        """Sets the email_alerts of this User.

        Activate email alerts for a user.  # noqa: E501

        :param email_alerts: The email_alerts of this User.  # noqa: E501
        :type: bool
        """

        self._email_alerts = email_alerts

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        User's name. (pattern does not allow non ascii and special characters &,<,>,\\\")  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        User's name. (pattern does not allow non ascii and special characters &,<,>,\\\")  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501

        User's password. Note that it could also be an already-hashed value, in which case 'password_hash_method' parameter is also provided.  # noqa: E501

        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        User's password. Note that it could also be an already-hashed value, in which case 'password_hash_method' parameter is also provided.  # noqa: E501

        :param password: The password of this User.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_hashing_method(self):
        """Gets the password_hashing_method of this User.  # noqa: E501

        Used when password is passed pre-hashed to specify the hashing method  # noqa: E501

        :return: The password_hashing_method of this User.  # noqa: E501
        :rtype: int
        """
        return self._password_hashing_method

    @password_hashing_method.setter
    def password_hashing_method(self, password_hashing_method):
        """Sets the password_hashing_method of this User.

        Used when password is passed pre-hashed to specify the hashing method  # noqa: E501

        :param password_hashing_method: The password_hashing_method of this User.  # noqa: E501
        :type: int
        """
        allowed_values = [1]  # noqa: E501
        if password_hashing_method not in allowed_values:
            raise ValueError(
                "Invalid value for `password_hashing_method` ({0}), must be one of {1}"  # noqa: E501
                .format(password_hashing_method, allowed_values)
            )

        self._password_hashing_method = password_hashing_method

    @property
    def password_issue_date(self):
        """Gets the password_issue_date of this User.  # noqa: E501

        The date in which the password was set .  # noqa: E501

        :return: The password_issue_date of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._password_issue_date

    @password_issue_date.setter
    def password_issue_date(self, password_issue_date):
        """Sets the password_issue_date of this User.

        The date in which the password was set .  # noqa: E501

        :param password_issue_date: The password_issue_date of this User.  # noqa: E501
        :type: datetime
        """

        self._password_issue_date = password_issue_date

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501

        User's role.  # noqa: E501

        :return: The role of this User.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.

        User's role.  # noqa: E501

        :param role: The role of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "cluster_member", "db_viewer", "db_member", "cluster_viewer", "none"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def role_uids(self):
        """Gets the role_uids of this User.  # noqa: E501

        List of role uids associated with the LDAP group  # noqa: E501

        :return: The role_uids of this User.  # noqa: E501
        :rtype: list[int]
        """
        return self._role_uids

    @role_uids.setter
    def role_uids(self, role_uids):
        """Sets the role_uids of this User.

        List of role uids associated with the LDAP group  # noqa: E501

        :param role_uids: The role_uids of this User.  # noqa: E501
        :type: list[int]
        """

        self._role_uids = role_uids

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
