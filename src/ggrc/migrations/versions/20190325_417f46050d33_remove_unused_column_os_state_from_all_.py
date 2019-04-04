# Copyright (C) 2019 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
remove unused column os state from all tables

Create Date: 2019-03-25 14:21:42.080300
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name


from alembic import op

# revision identifiers, used by Alembic.
revision = '417f46050d33'
down_revision = '048e54271df8'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  # ### commands auto generated by Alembic - please adjust! ###
  op.drop_column('access_groups', 'os_state')
  op.drop_column('assessments', 'os_state')
  op.drop_column('clauses', 'os_state')
  op.drop_column('controls', 'os_state')
  op.drop_column('data_assets', 'os_state')
  op.drop_column('directives', 'os_state')
  op.drop_column('facilities', 'os_state')
  op.drop_column('issues', 'os_state')
  op.drop_column('key_reports', 'os_state')
  op.drop_column('markets', 'os_state')
  op.drop_column('metrics', 'os_state')
  op.drop_column('objectives', 'os_state')
  op.drop_column('org_groups', 'os_state')
  op.drop_column('product_groups', 'os_state')
  op.drop_column('products', 'os_state')
  op.drop_column('programs', 'os_state')
  op.drop_column('projects', 'os_state')
  op.drop_column('requirements', 'os_state')
  op.drop_column('risks', 'os_state')
  op.drop_column('systems', 'os_state')
  op.drop_column('technology_environments', 'os_state')
  op.drop_column('threats', 'os_state')
  op.drop_column('vendors', 'os_state')
  # ### end Alembic commands ###


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
  raise NotImplementedError("Downgrade is not supported")