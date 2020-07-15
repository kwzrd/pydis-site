from django.db import models

from pydis_site.apps.api.models.mixins import ModelReprMixin, ModelTimestampMixin


class AllowList(ModelTimestampMixin, ModelReprMixin, models.Model):
    """An item that is either allowed or denied."""

    AllowListType = models.TextChoices(
        'AllowListType',
        'GUILD_INVITE_ID '
        'FILE_FORMAT '
        'DOMAIN_NAME '
        'WORD_WATCHLIST '
    )
    type = models.CharField(
        max_length=50,
        help_text="The type of allowlist this is on.",
        choices=AllowListType.choices,
    )
    allowed = models.BooleanField(
        help_text="Whether this item is on the allowlist or the denylist."
    )
    content = models.TextField(
        help_text="The data to add to the allowlist."
    )

    class Meta:
        """Metaconfig for this model."""

        db_table = 'allow_list'

        # This constraint ensures only one allowlist with the same content
        # can exist per type.This means that we cannot have both an allow
        # and a deny for the same item, and we cannot have duplicates of the
        # same item.
        constraints = [
            models.UniqueConstraint(fields=['content', 'type'], name='unique_allowlist'),
        ]
