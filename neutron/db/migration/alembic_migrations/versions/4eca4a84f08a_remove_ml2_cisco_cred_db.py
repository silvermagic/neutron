# Copyright 2014 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""Remove ML2 Cisco Credentials DB

Revision ID: 4eca4a84f08a
Revises: 33c3db036fe4
Create Date: 2014-04-10 19:32:46.697189

"""

# revision identifiers, used by Alembic.
revision = '4eca4a84f08a'
down_revision = '33c3db036fe4'


from alembic import op

from neutron.db import migration


def upgrade(active_plugins=None, options=None):
    op.execute('DROP TABLE IF EXISTS cisco_ml2_credentials')


def downgrade(active_plugins=None, options=None):
    if op.get_bind().engine.dialect.name == 'postgresql':
        migration.create_table_if_not_exist_psql(
            'cisco_ml2_credentials',
            ("(credential_id VARCHAR(255) NULL,"
             "tenant_id VARCHAR(255) NOT NULL,"
             "credential_name VARCHAR(255) NOT NULL,"
             "user_name VARCHAR(255) NULL,"
             "password VARCHAR(255) NULL,"
             "PRIMARY KEY (tenant_id, credential_name))"))
    else:
        op.execute('CREATE TABLE IF NOT EXISTS cisco_ml2_credentials( '
                   'credential_id VARCHAR(255) NULL,'
                   'tenant_id VARCHAR(255) NOT NULL,'
                   'credential_name VARCHAR(255) NOT NULL,'
                   'user_name VARCHAR(255) NULL,'
                   'password VARCHAR(255) NULL,'
                   'PRIMARY KEY (tenant_id, credential_name))')
