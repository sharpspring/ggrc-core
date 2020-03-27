# Copyright (C) 2020 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""Module for Contract object."""

import sqlalchemy as sa

from ggrc import db
from ggrc.fulltext import mixin as ft_mixins
from ggrc.models import comment
from ggrc.models import mixins
from ggrc.models import object_document
from ggrc.models import object_person
from ggrc.models import reflection
from ggrc.models import relationship


class Contract(mixins.synchronizable.Synchronizable,
               mixins.synchronizable.RoleableSynchronizable,
               mixins.WithExternalCreatedBy,
               comment.ExternalCommentable,
               mixins.BusinessObject,
               mixins.CustomAttributable,
               mixins.Folderable,
               mixins.LastDeprecatedTimeboxed,
               mixins.TestPlanned,
               mixins.WithWorkflowState,
               mixins.base.ContextRBAC,
               object_document.PublicDocumentable,
               object_person.Personable,
               relationship.Relatable,
               mixins.Base,
               ft_mixins.Indexed,
               db.Model):
  """Contract model."""

  __tablename__ = "contracts"

  kind = db.Column(db.String)

  VALID_KINDS = (
      "Contract",
  )

  _api_attrs = reflection.ApiAttributes(
      "kind",
  )

  _fulltext_attrs = [
      "kind",
  ]

  _sanitize_html = []

  _include_links = []

  _aliases = {
      "kind": None,
      "documents_file": None,
  }

  @sa.orm.validates("kind")
  def validate_kind(self, key, value):
    """Validate a value set to `kind` field.

    In order to be valid, the passed value `value` should be present in
    `Contract.VALID_KINDS` class field.

    Args:
      key (str): A field name, equals to "kind".
      value (Any): A value assigned to a field.

    Returns:
      A validated value.

    Raises:
      ValueError: a `value` is an invalid value for a `key` column.
    """
    if not value:
      return None
    if value not in self.VALID_KINDS:
      message = "Invalid value '{}' for attribute {}.{}.".format(
                value, self.__class__.__name__, key)
      raise ValueError(message)
    return value

  @classmethod
  def eager_query(cls, **kwargs):
    """Return `sqlalchemy.Query` query used for object eager loading."""
    query = super(Contract, cls).eager_query(**kwargs)
    return cls.eager_inclusions(query, cls._include_links)

  @classmethod
  def indexed_query(cls):
    """Return `sqlalchemy.Query` query used for object indexing."""
    return super(Contract, cls).indexed_query().options(
        sa.orm.Load(cls).load_only(
            "kind",
        ),
    )