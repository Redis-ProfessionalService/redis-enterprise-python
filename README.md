# swagger-client
REST API Specifications[¶](#rest-api-specifications "Permalink to this headline") 
=================================================================================  

Key Concepts[¶](#key-concepts "Permalink to this headline") 

-----------------------------------------------------------  

### Clusters[¶](#clusters "Permalink to this headline")  

Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.  

Protocol and Headers[¶](#protocol-and-headers "Permalink to this headline") 

---------------------------------------------------------------------------  

### JSON Requests and Responses[¶](#json-requests-and-responses "Permalink to this headline")  

The Redis Labs REST API uses the JavaScript Object Notation (JSON) for requests and responses.  Some responses may have an empty body, but indicate the response with standard HTTP codes. For more information, see RFC 4627 ([http://www.ietf.org/rfc/rfc4627.txt](http://www.ietf.org/rfc/rfc4627.txt)) and www.json.org.  Both requests and responses may include zero or more objects.  In case the request is for a single entity, the response shall return a single JSON object, or none. In case the request if for a list of entities, the response shall return a single JSON array with 0 or more elements.  Requests may be delivered with some JSON object fields missing. In this case, these fields will be assigned default values (often indicating they are not in use).  

### Request Headers[¶](#request-headers "Permalink to this headline")  

The Redis Labs REST API supports the following HTTP headers:  

| Header | Supported/Required Values |
|---|---|
| Accept | application/json |
| Content-Length | Length (in bytes) of request message. |
| Content-Type | application/json |

### Response Headers[¶](#response-headers "Permalink to this headline")  

The Redis Labs REST API supports the following HTTP headers:  

| Header | Supported/Required Values |
|---|---|
| Content-Type | application/json |
| Content-Length | Length (in bytes) of request message. |

API Versions[¶](#api-versions "Permalink to this headline")

-----------------------------------------------------------  

All RLEC API operations are versioned, in order to minimize the impact of backwards-incompatible API changes and to coordinate between different versions operating in parallel.  

Authentication[¶](#authentication "Permalink to this headline") 

---------------------------------------------------------------  

Authentication to RLEC API occurs via [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide your RLEC username and password as the basic auth credentials.  All calls must be made over SSL, to port 9443.  Example Request:  

```bash
curl -u "demo@redislabs.com:password" https://localhost:9443/v1/bdbs
``` 

Common Responses[¶](#common-responses "Permalink to this headline")

-------------------------------------------------------------------  

The following are common responses which may be returned in some cases regardless of any specific request.  

| Response | Condition / Required handling |
|---|---|
| 503 (Service Unavailable) | Contacted node is currently not a member of any active cluster. |
| 505 (HTTP Version Not Supported) | An unsupported X-API-Version was used, see API Versions above. | 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 6.2.4-55
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Get optimized shards placement for the given database.
    api_response = api_instance.get_v1_bdbs_uid_actions_optimize_shards_placement(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->get_v1_bdbs_uid_actions_optimize_shards_placement: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database to recover.

try:
    # Fetch the recovery plan for a database in recovery mode
    api_instance.get_v1_bdbs_uid_actions_recover(uid)
except ApiException as e:
    print("Exception when calling ActionsApi->get_v1_bdbs_uid_actions_recover: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database
body = swagger_client.ActionsExportBody() # ActionsExportBody | The request body should contain a JSON object (optional)

try:
    # Initiate a database export.
    api_instance.post_v1_bdbs_uid_actions_export(uid, body=body)
except ApiException as e:
    print("Exception when calling ActionsApi->post_v1_bdbs_uid_actions_export: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database
body = swagger_client.ActionsImportBody() # ActionsImportBody |  (optional)

try:
    # Initiate a manual import process.
    api_instance.post_v1_bdbs_uid_actions_import(uid, body=body)
except ApiException as e:
    print("Exception when calling ActionsApi->post_v1_bdbs_uid_actions_import: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database to recover.
body = swagger_client.ActionsRecoverBody() # ActionsRecoverBody | Optional body -- The request body may be empty, in which case the database will be recovered automatically.

The request may include a request body with an explicit recovery plan. (optional)

try:
    # Initiate recovery for a database in recovery state.
    api_instance.post_v1_bdbs_uid_actions_recover(uid, body=body)
except ApiException as e:
    print("Exception when calling ActionsApi->post_v1_bdbs_uid_actions_recover: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 56 # int | The uid of the db on which the command will be performed.
body = swagger_client.DbCommand() # DbCommand | The request must contain a redis command JSON representation consists of a ‘command’ field. It may also consist of an ‘args’ array. (optional)

try:
    # Execute a redis/memcached command
    api_response = api_instance.post_v1_bdbs_uid_command(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->post_v1_bdbs_uid_command: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database for which update is requested.
action = 'action_example' # str | Additional action to perform. Currently the supported actions are: flush, reset_admin_pass.
body = swagger_client.Bdb() # Bdb |  (optional)
dry_run = 'dry_run_example' # str | Validate the bdb object against the existing bdb, but do not invoke the state machine to update it. (optional)

try:
    # Update the configuration of an active database.
    api_instance.put_v1_bdbs_uid_action(uid, action, body=body, dry_run=dry_run)
except ApiException as e:
    print("Exception when calling ActionsApi->put_v1_bdbs_uid_action: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database

try:
    # Reset database current backup status
    api_instance.put_v1_bdbs_uid_actions_backup_reset_status(uid)
except ApiException as e:
    print("Exception when calling ActionsApi->put_v1_bdbs_uid_actions_backup_reset_status: %s\n" % e)
# Configure HTTP basic authorization: YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | The unique ID of the database

try:
    # Reset database current export status
    api_instance.put_v1_bdbs_uid_actions_export_reset_status(uid)
except ApiException as e:
    print("Exception when calling ActionsApi->put_v1_bdbs_uid_actions_export_reset_status: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:9443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionsApi* | [**get_v1_bdbs_uid_actions_optimize_shards_placement**](docs/ActionsApi.md#get_v1_bdbs_uid_actions_optimize_shards_placement) | **GET** /v1/bdbs/{uid}/actions/optimize_shards_placement | Get optimized shards placement for the given database.
*ActionsApi* | [**get_v1_bdbs_uid_actions_recover**](docs/ActionsApi.md#get_v1_bdbs_uid_actions_recover) | **GET** /v1/bdbs/{uid}/actions/recover | Fetch the recovery plan for a database in recovery mode
*ActionsApi* | [**post_v1_bdbs_uid_actions_export**](docs/ActionsApi.md#post_v1_bdbs_uid_actions_export) | **POST** /v1/bdbs/{uid}/actions/export | Initiate a database export.
*ActionsApi* | [**post_v1_bdbs_uid_actions_import**](docs/ActionsApi.md#post_v1_bdbs_uid_actions_import) | **POST** /v1/bdbs/{uid}/actions/import | Initiate a manual import process.
*ActionsApi* | [**post_v1_bdbs_uid_actions_recover**](docs/ActionsApi.md#post_v1_bdbs_uid_actions_recover) | **POST** /v1/bdbs/{uid}/actions/recover | Initiate recovery for a database in recovery state.
*ActionsApi* | [**post_v1_bdbs_uid_command**](docs/ActionsApi.md#post_v1_bdbs_uid_command) | **POST** /v1/bdbs/{uid}/command | Execute a redis/memcached command
*ActionsApi* | [**put_v1_bdbs_uid_action**](docs/ActionsApi.md#put_v1_bdbs_uid_action) | **PUT** /v1/bdbs/{uid}/{action} | Update the configuration of an active database.
*ActionsApi* | [**put_v1_bdbs_uid_actions_backup_reset_status**](docs/ActionsApi.md#put_v1_bdbs_uid_actions_backup_reset_status) | **PUT** /v1/bdbs/{uid}/actions/backup_reset_status | Reset database current backup status
*ActionsApi* | [**put_v1_bdbs_uid_actions_export_reset_status**](docs/ActionsApi.md#put_v1_bdbs_uid_actions_export_reset_status) | **PUT** /v1/bdbs/{uid}/actions/export_reset_status | Reset database current export status
*BackupApi* | [**post_v1_bdbs_uid_actions_import**](docs/BackupApi.md#post_v1_bdbs_uid_actions_import) | **POST** /v1/bdbs/{uid}/actions/import | Initiate a manual import process.
*BackupsApi* | [**put_v1_bdbs_uid_actions_backup_reset_status**](docs/BackupsApi.md#put_v1_bdbs_uid_actions_backup_reset_status) | **PUT** /v1/bdbs/{uid}/actions/backup_reset_status | Reset database current backup status
*BdbsApi* | [**delete_v1_bdbs_uid_passwords**](docs/BdbsApi.md#delete_v1_bdbs_uid_passwords) | **DELETE** /v1/bdbs/{uid}/passwords | Delete a password from the bdb’s default user
*BdbsApi* | [**get_v1_bdbs**](docs/BdbsApi.md#get_v1_bdbs) | **GET** /v1/bdbs | Get all databases in the cluster.
*BdbsApi* | [**get_v1_bdbs_uid**](docs/BdbsApi.md#get_v1_bdbs_uid) | **GET** /v1/bdbs/{uid} | Get single database (bdb object) as json.
*BdbsApi* | [**get_v1_bdbs_uid_actions_optimize_shards_placement**](docs/BdbsApi.md#get_v1_bdbs_uid_actions_optimize_shards_placement) | **GET** /v1/bdbs/{uid}/actions/optimize_shards_placement | Get optimized shards placement for the given database.
*BdbsApi* | [**get_v1_bdbs_uid_actions_recover**](docs/BdbsApi.md#get_v1_bdbs_uid_actions_recover) | **GET** /v1/bdbs/{uid}/actions/recover | Fetch the recovery plan for a database in recovery mode
*BdbsApi* | [**post_v1_bdbs**](docs/BdbsApi.md#post_v1_bdbs) | **POST** /v1/bdbs | Create a new database in the cluster.
*BdbsApi* | [**post_v1_bdbs_uid_actions_export**](docs/BdbsApi.md#post_v1_bdbs_uid_actions_export) | **POST** /v1/bdbs/{uid}/actions/export | Initiate a database export.
*BdbsApi* | [**post_v1_bdbs_uid_actions_import**](docs/BdbsApi.md#post_v1_bdbs_uid_actions_import) | **POST** /v1/bdbs/{uid}/actions/import | Initiate a manual import process.
*BdbsApi* | [**post_v1_bdbs_uid_actions_recover**](docs/BdbsApi.md#post_v1_bdbs_uid_actions_recover) | **POST** /v1/bdbs/{uid}/actions/recover | Initiate recovery for a database in recovery state.
*BdbsApi* | [**post_v1_bdbs_uid_command**](docs/BdbsApi.md#post_v1_bdbs_uid_command) | **POST** /v1/bdbs/{uid}/command | Execute a redis/memcached command
*BdbsApi* | [**post_v1_bdbs_uid_passwords**](docs/BdbsApi.md#post_v1_bdbs_uid_passwords) | **POST** /v1/bdbs/{uid}/passwords | Add a password to the bdb’s default user
*BdbsApi* | [**post_v1_bdbs_uid_upgrade**](docs/BdbsApi.md#post_v1_bdbs_uid_upgrade) | **POST** /v1/bdbs/{uid}/upgrade | Upgrade a BDB
*BdbsApi* | [**put_v1_bdbs_uid**](docs/BdbsApi.md#put_v1_bdbs_uid) | **PUT** /v1/bdbs/{uid} | Update the configuration of an active database.
*BdbsApi* | [**put_v1_bdbs_uid_action**](docs/BdbsApi.md#put_v1_bdbs_uid_action) | **PUT** /v1/bdbs/{uid}/{action} | Update the configuration of an active database.
*BdbsApi* | [**put_v1_bdbs_uid_actions_backup_reset_status**](docs/BdbsApi.md#put_v1_bdbs_uid_actions_backup_reset_status) | **PUT** /v1/bdbs/{uid}/actions/backup_reset_status | Reset database current backup status
*BdbsApi* | [**put_v1_bdbs_uid_actions_export_reset_status**](docs/BdbsApi.md#put_v1_bdbs_uid_actions_export_reset_status) | **PUT** /v1/bdbs/{uid}/actions/export_reset_status | Reset database current export status
*ClusterApi* | [**delete_v1_cluster_certificates_certificate_name**](docs/ClusterApi.md#delete_v1_cluster_certificates_certificate_name) | **DELETE** /v1/cluster/certificates/{certificate_name} | Removes specified cluster certificate
*ClusterApi* | [**get_v1_cluster_certificates**](docs/ClusterApi.md#get_v1_cluster_certificates) | **GET** /v1/cluster/certificates | Get the clusters certificates.
*ClusterApi* | [**post_v1_cluster_certificates_rotate**](docs/ClusterApi.md#post_v1_cluster_certificates_rotate) | **POST** /v1/cluster/certificates/rotate | Regenerate all internal cluster certificates
*ClusterApi* | [**put_v1_cluster_update_cert**](docs/ClusterApi.md#put_v1_cluster_update_cert) | **PUT** /v1/cluster/update_cert | Replaces specified cluster certificate
*CrdbsApi* | [**get_v1_crdb**](docs/CrdbsApi.md#get_v1_crdb) | **GET** /v1/crdbs | Get a list of all Active-Active database on the cluster.
*CrdbsApi* | [**post_v1_crdbs**](docs/CrdbsApi.md#post_v1_crdbs) | **POST** /v1/crdbs | Create a new Active-Active database.
*DefaultApi* | [**delete_v1_bdbs_uid**](docs/DefaultApi.md#delete_v1_bdbs_uid) | **DELETE** /v1/bdbs/{uid} | Delete an active database.
*DefaultApi* | [**put_v1_bdbs_uid_passwords**](docs/DefaultApi.md#put_v1_bdbs_uid_passwords) | **PUT** /v1/bdbs/{uid}/passwords | Set a (single) password
*ShardsApi* | [**get_v1_bdbs_uid_actions_optimize_shards_placement**](docs/ShardsApi.md#get_v1_bdbs_uid_actions_optimize_shards_placement) | **GET** /v1/bdbs/{uid}/actions/optimize_shards_placement | Get optimized shards placement for the given database.
*UsersApi* | [**delete_v1_users**](docs/UsersApi.md#delete_v1_users) | **DELETE** /v1/users/{uid} | Delete a RLEC user.
*UsersApi* | [**delete_v1_users_password**](docs/UsersApi.md#delete_v1_users_password) | **DELETE** /v1/users/password | Delete a password from a user
*UsersApi* | [**get_v1_users**](docs/UsersApi.md#get_v1_users) | **GET** /v1/users/{uid} | Get a single RLEC user.
*UsersApi* | [**post_v1_users**](docs/UsersApi.md#post_v1_users) | **POST** /v1/users | Create a new RLEC user.
*UsersApi* | [**post_v1_users_password**](docs/UsersApi.md#post_v1_users_password) | **POST** /v1/users/password | Add a new password to an internal user
*UsersApi* | [**put_v1_users_password**](docs/UsersApi.md#put_v1_users_password) | **PUT** /v1/users/password | Reset the password list of an internal user

## Documentation For Models

 - [Action](docs/Action.md)
 - [ActionCluster](docs/ActionCluster.md)
 - [ActionClusterChangeMaster](docs/ActionClusterChangeMaster.md)
 - [ActionNode](docs/ActionNode.md)
 - [ActionNodeCloneNodeSettings](docs/ActionNodeCloneNodeSettings.md)
 - [ActionNodeEnslaveNode](docs/ActionNodeEnslaveNode.md)
 - [ActionNodeMaintenanceOff](docs/ActionNodeMaintenanceOff.md)
 - [ActionNodeMaintenanceOn](docs/ActionNodeMaintenanceOn.md)
 - [ActionsExportBody](docs/ActionsExportBody.md)
 - [ActionsImportBody](docs/ActionsImportBody.md)
 - [ActionsRecoverBody](docs/ActionsRecoverBody.md)
 - [AlertSettingsWithThreshold](docs/AlertSettingsWithThreshold.md)
 - [AllOfactionsExportBodyExportLocation](docs/AllOfactionsExportBodyExportLocation.md)
 - [AllOfbdbCrdtSources](docs/AllOfbdbCrdtSources.md)
 - [AllOfbdbCrdtSync](docs/AllOfbdbCrdtSync.md)
 - [AllOfbdbImportFailureReason](docs/AllOfbdbImportFailureReason.md)
 - [AllOfbdbReplicaSources](docs/AllOfbdbReplicaSources.md)
 - [AllOfbdbReplicaSync](docs/AllOfbdbReplicaSync.md)
 - [AllOfbdbSnapshotPolicy](docs/AllOfbdbSnapshotPolicy.md)
 - [AllOfbdbSync](docs/AllOfbdbSync.md)
 - [AllOfclusterAlertSettingsClusterCertsAboutToExpire](docs/AllOfclusterAlertSettingsClusterCertsAboutToExpire.md)
 - [AllOfclusterAlertSettingsNodeCpuUtilization](docs/AllOfclusterAlertSettingsNodeCpuUtilization.md)
 - [AllOfclusterAlertSettingsNodeEphemeralStorage](docs/AllOfclusterAlertSettingsNodeEphemeralStorage.md)
 - [AllOfclusterAlertSettingsNodeFreeFlash](docs/AllOfclusterAlertSettingsNodeFreeFlash.md)
 - [AllOfclusterAlertSettingsNodeInternalCertsAboutToExpire](docs/AllOfclusterAlertSettingsNodeInternalCertsAboutToExpire.md)
 - [AllOfclusterAlertSettingsNodeMemory](docs/AllOfclusterAlertSettingsNodeMemory.md)
 - [AllOfclusterAlertSettingsNodeNetThroughput](docs/AllOfclusterAlertSettingsNodeNetThroughput.md)
 - [AllOfclusterAlertSettingsNodePersistentStorage](docs/AllOfclusterAlertSettingsNodePersistentStorage.md)
 - [AllOfdbAlertsSettingsBdbBackupDelayed](docs/AllOfdbAlertsSettingsBdbBackupDelayed.md)
 - [AllOfdbAlertsSettingsBdbCrdtSrcHighSyncerLag](docs/AllOfdbAlertsSettingsBdbCrdtSrcHighSyncerLag.md)
 - [AllOfdbAlertsSettingsBdbCrdtSrcSyncerConnectionError](docs/AllOfdbAlertsSettingsBdbCrdtSrcSyncerConnectionError.md)
 - [AllOfdbAlertsSettingsBdbCrdtSrcSyncerGeneralError](docs/AllOfdbAlertsSettingsBdbCrdtSrcSyncerGeneralError.md)
 - [AllOfdbAlertsSettingsBdbHighLatency](docs/AllOfdbAlertsSettingsBdbHighLatency.md)
 - [AllOfdbAlertsSettingsBdbHighSyncerLag](docs/AllOfdbAlertsSettingsBdbHighSyncerLag.md)
 - [AllOfdbAlertsSettingsBdbHighThroughput](docs/AllOfdbAlertsSettingsBdbHighThroughput.md)
 - [AllOfdbAlertsSettingsBdbLongRunningAction](docs/AllOfdbAlertsSettingsBdbLongRunningAction.md)
 - [AllOfdbAlertsSettingsBdbLowThroughput](docs/AllOfdbAlertsSettingsBdbLowThroughput.md)
 - [AllOfdbAlertsSettingsBdbRamDatasetOverhead](docs/AllOfdbAlertsSettingsBdbRamDatasetOverhead.md)
 - [AllOfdbAlertsSettingsBdbRamValues](docs/AllOfdbAlertsSettingsBdbRamValues.md)
 - [AllOfdbAlertsSettingsBdbReplicaSrcHighSyncerLag](docs/AllOfdbAlertsSettingsBdbReplicaSrcHighSyncerLag.md)
 - [AllOfdbAlertsSettingsBdbReplicaSrcSyncerConnectionError](docs/AllOfdbAlertsSettingsBdbReplicaSrcSyncerConnectionError.md)
 - [AllOfdbAlertsSettingsBdbReplicaSrcSyncerGeneralError](docs/AllOfdbAlertsSettingsBdbReplicaSrcSyncerGeneralError.md)
 - [AllOfdbAlertsSettingsBdbShardNumRamValues](docs/AllOfdbAlertsSettingsBdbShardNumRamValues.md)
 - [AllOfdbAlertsSettingsBdbSize](docs/AllOfdbAlertsSettingsBdbSize.md)
 - [AllOfdbAlertsSettingsBdbSyncerConnectionError](docs/AllOfdbAlertsSettingsBdbSyncerConnectionError.md)
 - [AllOfdbAlertsSettingsBdbSyncerGeneralError](docs/AllOfdbAlertsSettingsBdbSyncerGeneralError.md)
 - [AnyOfactionsImportBodyDatasetImportSourcesItems](docs/AnyOfactionsImportBodyDatasetImportSourcesItems.md)
 - [AnyOfbdbBackupLocation](docs/AnyOfbdbBackupLocation.md)
 - [AnyOfbdbDatasetImportSourcesItems](docs/AnyOfbdbDatasetImportSourcesItems.md)
 - [AnyOfbdbsUidBody](docs/AnyOfbdbsUidBody.md)
 - [AnyOfbootstrap](docs/AnyOfbootstrap.md)
 - [AnyOfbootstrapDnsSuffixesSlavesItems](docs/AnyOfbootstrapDnsSuffixesSlavesItems.md)
 - [AnyOfldapMappingBdbsEmailAlerts](docs/AnyOfldapMappingBdbsEmailAlerts.md)
 - [AnyOfnodeIdentityIdentityExternalAddrItems](docs/AnyOfnodeIdentityIdentityExternalAddrItems.md)
 - [AnyOfuserBdbsEmailAlerts](docs/AnyOfuserBdbsEmailAlerts.md)
 - [Bdb](docs/Bdb.md)
 - [BdbAuthenticationSslClientCerts](docs/BdbAuthenticationSslClientCerts.md)
 - [BdbAzureBlobStorage](docs/BdbAzureBlobStorage.md)
 - [BdbBackgroundOp](docs/BdbBackgroundOp.md)
 - [BdbBigstoreRamWeights](docs/BdbBigstoreRamWeights.md)
 - [BdbEndpoints](docs/BdbEndpoints.md)
 - [BdbError](docs/BdbError.md)
 - [BdbGoogleStorage](docs/BdbGoogleStorage.md)
 - [BdbGroup](docs/BdbGroup.md)
 - [BdbImportFailureReason](docs/BdbImportFailureReason.md)
 - [BdbModuleList](docs/BdbModuleList.md)
 - [BdbMountPointStorage](docs/BdbMountPointStorage.md)
 - [BdbRdbUrl](docs/BdbRdbUrl.md)
 - [BdbRolesPermissions](docs/BdbRolesPermissions.md)
 - [BdbS3Storage](docs/BdbS3Storage.md)
 - [BdbSftpStorage](docs/BdbSftpStorage.md)
 - [BdbShardKeyRegex](docs/BdbShardKeyRegex.md)
 - [BdbShardsBlueprint](docs/BdbShardsBlueprint.md)
 - [BdbShardsBlueprintInner](docs/BdbShardsBlueprintInner.md)
 - [BdbSnapshotPolicy](docs/BdbSnapshotPolicy.md)
 - [BdbSwiftStorage](docs/BdbSwiftStorage.md)
 - [BdbSyncSources](docs/BdbSyncSources.md)
 - [BdbSyncString](docs/BdbSyncString.md)
 - [BdbSyncerSources](docs/BdbSyncerSources.md)
 - [BdbSyncerSourcesInner](docs/BdbSyncerSourcesInner.md)
 - [BdbTags](docs/BdbTags.md)
 - [BdbsUidBody](docs/BdbsUidBody.md)
 - [Bootstrap](docs/Bootstrap.md)
 - [BootstrapCloud](docs/BootstrapCloud.md)
 - [BootstrapCloudAzure](docs/BootstrapCloudAzure.md)
 - [BootstrapCloudEc2](docs/BootstrapCloudEc2.md)
 - [BootstrapCredentials](docs/BootstrapCredentials.md)
 - [BootstrapDnsSuffixes](docs/BootstrapDnsSuffixes.md)
 - [CheckResult](docs/CheckResult.md)
 - [CheckResultNodes](docs/CheckResultNodes.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterAlertSettings](docs/ClusterAlertSettings.md)
 - [ClusterIdentity](docs/ClusterIdentity.md)
 - [ClusterInfo](docs/ClusterInfo.md)
 - [ClusterSettings](docs/ClusterSettings.md)
 - [Crdb](docs/Crdb.md)
 - [CrdbLocalDatabases](docs/CrdbLocalDatabases.md)
 - [Credentials](docs/Credentials.md)
 - [CronExpression](docs/CronExpression.md)
 - [DbAlertsSettings](docs/DbAlertsSettings.md)
 - [DbCommand](docs/DbCommand.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse406](docs/InlineResponse406.md)
 - [InlineResponse4061](docs/InlineResponse4061.md)
 - [InstanceId](docs/InstanceId.md)
 - [InstanceInfo](docs/InstanceInfo.md)
 - [JobScheduler](docs/JobScheduler.md)
 - [JobSchedulerBackupJobSettings](docs/JobSchedulerBackupJobSettings.md)
 - [JobSchedulerCertRotationJobSettings](docs/JobSchedulerCertRotationJobSettings.md)
 - [JobSchedulerLogRotationJobSettings](docs/JobSchedulerLogRotationJobSettings.md)
 - [JobSchedulerNodeChecksJobSettings](docs/JobSchedulerNodeChecksJobSettings.md)
 - [JobSchedulerRedisCleanupJobSettings](docs/JobSchedulerRedisCleanupJobSettings.md)
 - [JobSchedulerRotateCcsJobSettings](docs/JobSchedulerRotateCcsJobSettings.md)
 - [JwtAuthorize](docs/JwtAuthorize.md)
 - [Ldap](docs/Ldap.md)
 - [LdapMapping](docs/LdapMapping.md)
 - [LdapQuery](docs/LdapQuery.md)
 - [Module](docs/Module.md)
 - [ModuleModuleDependencies](docs/ModuleModuleDependencies.md)
 - [Node](docs/Node.md)
 - [NodeIdentity](docs/NodeIdentity.md)
 - [NodeIdentityIdentity](docs/NodeIdentityIdentity.md)
 - [NodeIdentityLimits](docs/NodeIdentityLimits.md)
 - [NodeIdentityPaths](docs/NodeIdentityPaths.md)
 - [NodeSupportedDatabaseVersions](docs/NodeSupportedDatabaseVersions.md)
 - [OneOfactionsRecoverBody](docs/OneOfactionsRecoverBody.md)
 - [OneOfbdbEndpointIpItems](docs/OneOfbdbEndpointIpItems.md)
 - [OneOfbdbEndpointsAddrItems](docs/OneOfbdbEndpointsAddrItems.md)
 - [OneOfbdbImportFailureReason](docs/OneOfbdbImportFailureReason.md)
 - [OneOfnodeExternalAddr](docs/OneOfnodeExternalAddr.md)
 - [Policy](docs/Policy.md)
 - [Proxy](docs/Proxy.md)
 - [RecoveryPlan](docs/RecoveryPlan.md)
 - [RecoveryPlanDataFiles](docs/RecoveryPlanDataFiles.md)
 - [RedisAcl](docs/RedisAcl.md)
 - [Role](docs/Role.md)
 - [ServicesConfiguration](docs/ServicesConfiguration.md)
 - [ServicesConfigurationCmServer](docs/ServicesConfigurationCmServer.md)
 - [ServicesConfigurationCrdbCoordinator](docs/ServicesConfigurationCrdbCoordinator.md)
 - [ServicesConfigurationCrdbWorker](docs/ServicesConfigurationCrdbWorker.md)
 - [ServicesConfigurationMdnsServer](docs/ServicesConfigurationMdnsServer.md)
 - [ServicesConfigurationPdnsServer](docs/ServicesConfigurationPdnsServer.md)
 - [ServicesConfigurationSaslauthd](docs/ServicesConfigurationSaslauthd.md)
 - [ServicesConfigurationStatsArchiver](docs/ServicesConfigurationStatsArchiver.md)
 - [Shard](docs/Shard.md)
 - [ShardBackup](docs/ShardBackup.md)
 - [ShardLoading](docs/ShardLoading.md)
 - [ShardSync](docs/ShardSync.md)
 - [Suffix](docs/Suffix.md)
 - [Task](docs/Task.md)
 - [TaskErrors](docs/TaskErrors.md)
 - [UidPasswordsBody](docs/UidPasswordsBody.md)
 - [UidPasswordsBody1](docs/UidPasswordsBody1.md)
 - [UidPasswordsBody2](docs/UidPasswordsBody2.md)
 - [User](docs/User.md)
 - [UsersPasswordBody](docs/UsersPasswordBody.md)
 - [UsersPasswordBody1](docs/UsersPasswordBody1.md)

## Documentation For Authorization


## YWRtaW5AcmVkaXNsYWJzLmNvbTppbXRoZWFkbWlu

- **Type**: HTTP basic authentication


## Author

matthew.royal@redis.com
