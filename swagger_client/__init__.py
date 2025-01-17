# coding: utf-8

# flake8: noqa

"""
    Redis Enterprise API

    REST API Specifications[¶](#rest-api-specifications \"Permalink to this headline\") =================================================================================  Key Concepts[¶](#key-concepts \"Permalink to this headline\") -----------------------------------------------------------  ### Clusters[¶](#clusters \"Permalink to this headline\")  Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.  Protocol and Headers[¶](#protocol-and-headers \"Permalink to this headline\") ---------------------------------------------------------------------------  ### JSON Requests and Responses[¶](#json-requests-and-responses \"Permalink to this headline\")  The Redis Labs REST API uses the JavaScript Object Notation (JSON) for requests and responses.  Some responses may have an empty body, but indicate the response with standard HTTP codes. For more information, see RFC 4627 ([http://www.ietf.org/rfc/rfc4627.txt](http://www.ietf.org/rfc/rfc4627.txt)) and www.json.org.  Both requests and responses may include zero or more objects.  In case the request is for a single entity, the response shall return a single JSON object, or none. In case the request if for a list of entities, the response shall return a single JSON array with 0 or more elements.  Requests may be delivered with some JSON object fields missing. In this case, these fields will be assigned default values (often indicating they are not in use).  ### Request Headers[¶](#request-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Accept | application/json | | Content-Length | Length (in bytes) of request message. | | Content-Type | application/json |   ### Response Headers[¶](#response-headers \"Permalink to this headline\")  The Redis Labs REST API supports the following HTTP headers:  | Header | Supported/Required Values | |---|---| | Content-Type | application/json | | Content-Length | Length (in bytes) of request message. |   API Versions[¶](#api-versions \"Permalink to this headline\") -----------------------------------------------------------  All RLEC API operations are versioned, in order to minimize the impact of backwards-incompatible API changes and to coordinate between different versions operating in parallel.  Authentication[¶](#authentication \"Permalink to this headline\") ---------------------------------------------------------------  Authentication to RLEC API occurs via [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Provide your RLEC username and password as the basic auth credentials.  All calls must be made over SSL, to port 9443.  Example Request:  ```bash curl \\-u \"demo@redislabs.com:password\" https://localhost:9443/v1/bdbs ```  Common Responses[¶](#common-responses \"Permalink to this headline\") -------------------------------------------------------------------  The following are common responses which may be returned in some cases regardless of any specific request.  | Response | Condition / Required handling | |---|---| | 503 (Service Unavailable) | Contacted node is currently not a member of any active cluster. | | 505 (HTTP Version Not Supported) | An unsupported X-API-Version was used, see API Versions above. |   # noqa: E501

    OpenAPI spec version: 6.2.4-55
    Contact: matthew.royal@redis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.actions_api import ActionsApi
from swagger_client.api.backup_api import BackupApi
from swagger_client.api.backups_api import BackupsApi
from swagger_client.api.bdbs_api import BdbsApi
from swagger_client.api.cluster_api import ClusterApi
from swagger_client.api.crdbs_api import CrdbsApi
from swagger_client.api.default_api import DefaultApi
from swagger_client.api.shards_api import ShardsApi
from swagger_client.api.users_api import UsersApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.action import Action
from swagger_client.models.action_cluster import ActionCluster
from swagger_client.models.action_cluster_change_master import ActionClusterChangeMaster
from swagger_client.models.action_node import ActionNode
from swagger_client.models.action_node_clone_node_settings import ActionNodeCloneNodeSettings
from swagger_client.models.action_node_enslave_node import ActionNodeEnslaveNode
from swagger_client.models.action_node_maintenance_off import ActionNodeMaintenanceOff
from swagger_client.models.action_node_maintenance_on import ActionNodeMaintenanceOn
from swagger_client.models.actions_export_body import ActionsExportBody
from swagger_client.models.actions_import_body import ActionsImportBody
from swagger_client.models.actions_recover_body import ActionsRecoverBody
from swagger_client.models.alert_settings_with_threshold import AlertSettingsWithThreshold
from swagger_client.models.all_ofactions_export_body_export_location import AllOfactionsExportBodyExportLocation
from swagger_client.models.all_ofbdb_crdt_sources import AllOfbdbCrdtSources
from swagger_client.models.all_ofbdb_crdt_sync import AllOfbdbCrdtSync
from swagger_client.models.all_ofbdb_import_failure_reason import AllOfbdbImportFailureReason
from swagger_client.models.all_ofbdb_replica_sources import AllOfbdbReplicaSources
from swagger_client.models.all_ofbdb_replica_sync import AllOfbdbReplicaSync
from swagger_client.models.all_ofbdb_snapshot_policy import AllOfbdbSnapshotPolicy
from swagger_client.models.all_ofbdb_sync import AllOfbdbSync
from swagger_client.models.all_ofcluster_alert_settings_cluster_certs_about_to_expire import AllOfclusterAlertSettingsClusterCertsAboutToExpire
from swagger_client.models.all_ofcluster_alert_settings_node_cpu_utilization import AllOfclusterAlertSettingsNodeCpuUtilization
from swagger_client.models.all_ofcluster_alert_settings_node_ephemeral_storage import AllOfclusterAlertSettingsNodeEphemeralStorage
from swagger_client.models.all_ofcluster_alert_settings_node_free_flash import AllOfclusterAlertSettingsNodeFreeFlash
from swagger_client.models.all_ofcluster_alert_settings_node_internal_certs_about_to_expire import AllOfclusterAlertSettingsNodeInternalCertsAboutToExpire
from swagger_client.models.all_ofcluster_alert_settings_node_memory import AllOfclusterAlertSettingsNodeMemory
from swagger_client.models.all_ofcluster_alert_settings_node_net_throughput import AllOfclusterAlertSettingsNodeNetThroughput
from swagger_client.models.all_ofcluster_alert_settings_node_persistent_storage import AllOfclusterAlertSettingsNodePersistentStorage
from swagger_client.models.all_ofdb_alerts_settings_bdb_backup_delayed import AllOfdbAlertsSettingsBdbBackupDelayed
from swagger_client.models.all_ofdb_alerts_settings_bdb_crdt_src_high_syncer_lag import AllOfdbAlertsSettingsBdbCrdtSrcHighSyncerLag
from swagger_client.models.all_ofdb_alerts_settings_bdb_crdt_src_syncer_connection_error import AllOfdbAlertsSettingsBdbCrdtSrcSyncerConnectionError
from swagger_client.models.all_ofdb_alerts_settings_bdb_crdt_src_syncer_general_error import AllOfdbAlertsSettingsBdbCrdtSrcSyncerGeneralError
from swagger_client.models.all_ofdb_alerts_settings_bdb_high_latency import AllOfdbAlertsSettingsBdbHighLatency
from swagger_client.models.all_ofdb_alerts_settings_bdb_high_syncer_lag import AllOfdbAlertsSettingsBdbHighSyncerLag
from swagger_client.models.all_ofdb_alerts_settings_bdb_high_throughput import AllOfdbAlertsSettingsBdbHighThroughput
from swagger_client.models.all_ofdb_alerts_settings_bdb_long_running_action import AllOfdbAlertsSettingsBdbLongRunningAction
from swagger_client.models.all_ofdb_alerts_settings_bdb_low_throughput import AllOfdbAlertsSettingsBdbLowThroughput
from swagger_client.models.all_ofdb_alerts_settings_bdb_ram_dataset_overhead import AllOfdbAlertsSettingsBdbRamDatasetOverhead
from swagger_client.models.all_ofdb_alerts_settings_bdb_ram_values import AllOfdbAlertsSettingsBdbRamValues
from swagger_client.models.all_ofdb_alerts_settings_bdb_replica_src_high_syncer_lag import AllOfdbAlertsSettingsBdbReplicaSrcHighSyncerLag
from swagger_client.models.all_ofdb_alerts_settings_bdb_replica_src_syncer_connection_error import AllOfdbAlertsSettingsBdbReplicaSrcSyncerConnectionError
from swagger_client.models.all_ofdb_alerts_settings_bdb_replica_src_syncer_general_error import AllOfdbAlertsSettingsBdbReplicaSrcSyncerGeneralError
from swagger_client.models.all_ofdb_alerts_settings_bdb_shard_num_ram_values import AllOfdbAlertsSettingsBdbShardNumRamValues
from swagger_client.models.all_ofdb_alerts_settings_bdb_size import AllOfdbAlertsSettingsBdbSize
from swagger_client.models.all_ofdb_alerts_settings_bdb_syncer_connection_error import AllOfdbAlertsSettingsBdbSyncerConnectionError
from swagger_client.models.all_ofdb_alerts_settings_bdb_syncer_general_error import AllOfdbAlertsSettingsBdbSyncerGeneralError
from swagger_client.models.any_ofactions_import_body_dataset_import_sources_items import AnyOfactionsImportBodyDatasetImportSourcesItems
from swagger_client.models.any_ofbdb_backup_location import AnyOfbdbBackupLocation
from swagger_client.models.any_ofbdb_dataset_import_sources_items import AnyOfbdbDatasetImportSourcesItems
from swagger_client.models.any_ofbdbs_uid_body import AnyOfbdbsUidBody
from swagger_client.models.any_ofbootstrap import AnyOfbootstrap
from swagger_client.models.any_ofbootstrap_dns_suffixes_slaves_items import AnyOfbootstrapDnsSuffixesSlavesItems
from swagger_client.models.any_ofldap_mapping_bdbs_email_alerts import AnyOfldapMappingBdbsEmailAlerts
from swagger_client.models.any_ofnode_identity_identity_external_addr_items import AnyOfnodeIdentityIdentityExternalAddrItems
from swagger_client.models.any_ofuser_bdbs_email_alerts import AnyOfuserBdbsEmailAlerts
from swagger_client.models.bdb import Bdb
from swagger_client.models.bdb_authentication_ssl_client_certs import BdbAuthenticationSslClientCerts
from swagger_client.models.bdb_azure_blob_storage import BdbAzureBlobStorage
from swagger_client.models.bdb_background_op import BdbBackgroundOp
from swagger_client.models.bdb_bigstore_ram_weights import BdbBigstoreRamWeights
from swagger_client.models.bdb_endpoints import BdbEndpoints
from swagger_client.models.bdb_error import BdbError
from swagger_client.models.bdb_google_storage import BdbGoogleStorage
from swagger_client.models.bdb_group import BdbGroup
from swagger_client.models.bdb_import_failure_reason import BdbImportFailureReason
from swagger_client.models.bdb_module_list import BdbModuleList
from swagger_client.models.bdb_mount_point_storage import BdbMountPointStorage
from swagger_client.models.bdb_rdb_url import BdbRdbUrl
from swagger_client.models.bdb_roles_permissions import BdbRolesPermissions
from swagger_client.models.bdb_s3_storage import BdbS3Storage
from swagger_client.models.bdb_sftp_storage import BdbSftpStorage
from swagger_client.models.bdb_shard_key_regex import BdbShardKeyRegex
from swagger_client.models.bdb_shards_blueprint import BdbShardsBlueprint
from swagger_client.models.bdb_shards_blueprint_inner import BdbShardsBlueprintInner
from swagger_client.models.bdb_snapshot_policy import BdbSnapshotPolicy
from swagger_client.models.bdb_swift_storage import BdbSwiftStorage
from swagger_client.models.bdb_sync_sources import BdbSyncSources
from swagger_client.models.bdb_sync_string import BdbSyncString
from swagger_client.models.bdb_syncer_sources import BdbSyncerSources
from swagger_client.models.bdb_syncer_sources_inner import BdbSyncerSourcesInner
from swagger_client.models.bdb_tags import BdbTags
from swagger_client.models.bdbs_uid_body import BdbsUidBody
from swagger_client.models.bootstrap import Bootstrap
from swagger_client.models.bootstrap_cloud import BootstrapCloud
from swagger_client.models.bootstrap_cloud_azure import BootstrapCloudAzure
from swagger_client.models.bootstrap_cloud_ec2 import BootstrapCloudEc2
from swagger_client.models.bootstrap_credentials import BootstrapCredentials
from swagger_client.models.bootstrap_dns_suffixes import BootstrapDnsSuffixes
from swagger_client.models.check_result import CheckResult
from swagger_client.models.check_result_nodes import CheckResultNodes
from swagger_client.models.cluster import Cluster
from swagger_client.models.cluster_alert_settings import ClusterAlertSettings
from swagger_client.models.cluster_identity import ClusterIdentity
from swagger_client.models.cluster_info import ClusterInfo
from swagger_client.models.cluster_settings import ClusterSettings
from swagger_client.models.crdb import Crdb
from swagger_client.models.crdb_local_databases import CrdbLocalDatabases
from swagger_client.models.credentials import Credentials
from swagger_client.models.cron_expression import CronExpression
from swagger_client.models.db_alerts_settings import DbAlertsSettings
from swagger_client.models.db_command import DbCommand
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response406 import InlineResponse406
from swagger_client.models.inline_response4061 import InlineResponse4061
from swagger_client.models.instance_id import InstanceId
from swagger_client.models.instance_info import InstanceInfo
from swagger_client.models.job_scheduler import JobScheduler
from swagger_client.models.job_scheduler_backup_job_settings import JobSchedulerBackupJobSettings
from swagger_client.models.job_scheduler_cert_rotation_job_settings import JobSchedulerCertRotationJobSettings
from swagger_client.models.job_scheduler_log_rotation_job_settings import JobSchedulerLogRotationJobSettings
from swagger_client.models.job_scheduler_node_checks_job_settings import JobSchedulerNodeChecksJobSettings
from swagger_client.models.job_scheduler_redis_cleanup_job_settings import JobSchedulerRedisCleanupJobSettings
from swagger_client.models.job_scheduler_rotate_ccs_job_settings import JobSchedulerRotateCcsJobSettings
from swagger_client.models.jwt_authorize import JwtAuthorize
from swagger_client.models.ldap import Ldap
from swagger_client.models.ldap_mapping import LdapMapping
from swagger_client.models.ldap_query import LdapQuery
from swagger_client.models.module import Module
from swagger_client.models.module_module_dependencies import ModuleModuleDependencies
from swagger_client.models.node import Node
from swagger_client.models.node_identity import NodeIdentity
from swagger_client.models.node_identity_identity import NodeIdentityIdentity
from swagger_client.models.node_identity_limits import NodeIdentityLimits
from swagger_client.models.node_identity_paths import NodeIdentityPaths
from swagger_client.models.node_supported_database_versions import NodeSupportedDatabaseVersions
from swagger_client.models.one_ofactions_recover_body import OneOfactionsRecoverBody
from swagger_client.models.one_ofbdb_endpoint_ip_items import OneOfbdbEndpointIpItems
from swagger_client.models.one_ofbdb_endpoints_addr_items import OneOfbdbEndpointsAddrItems
from swagger_client.models.one_ofbdb_import_failure_reason import OneOfbdbImportFailureReason
from swagger_client.models.one_ofnode_external_addr import OneOfnodeExternalAddr
from swagger_client.models.policy import Policy
from swagger_client.models.proxy import Proxy
from swagger_client.models.recovery_plan import RecoveryPlan
from swagger_client.models.recovery_plan_data_files import RecoveryPlanDataFiles
from swagger_client.models.redis_acl import RedisAcl
from swagger_client.models.role import Role
from swagger_client.models.services_configuration import ServicesConfiguration
from swagger_client.models.services_configuration_cm_server import ServicesConfigurationCmServer
from swagger_client.models.services_configuration_crdb_coordinator import ServicesConfigurationCrdbCoordinator
from swagger_client.models.services_configuration_crdb_worker import ServicesConfigurationCrdbWorker
from swagger_client.models.services_configuration_mdns_server import ServicesConfigurationMdnsServer
from swagger_client.models.services_configuration_pdns_server import ServicesConfigurationPdnsServer
from swagger_client.models.services_configuration_saslauthd import ServicesConfigurationSaslauthd
from swagger_client.models.services_configuration_stats_archiver import ServicesConfigurationStatsArchiver
from swagger_client.models.shard import Shard
from swagger_client.models.shard_backup import ShardBackup
from swagger_client.models.shard_loading import ShardLoading
from swagger_client.models.shard_sync import ShardSync
from swagger_client.models.suffix import Suffix
from swagger_client.models.task import Task
from swagger_client.models.task_errors import TaskErrors
from swagger_client.models.uid_passwords_body import UidPasswordsBody
from swagger_client.models.uid_passwords_body1 import UidPasswordsBody1
from swagger_client.models.uid_passwords_body2 import UidPasswordsBody2
from swagger_client.models.user import User
from swagger_client.models.users_password_body import UsersPasswordBody
from swagger_client.models.users_password_body1 import UsersPasswordBody1
