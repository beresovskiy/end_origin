end-summary directive for reStructuredText
==========================================

This plugin is complementary to `summary` plugin and cannot run without it.

Plugin `summary` allows to define post summary by inserting `<!-- PELICAN_END_SUMMARY -->` tag into the post body, effectively marking everything above its position (except rare cases when you make use of `<!-- PELICAN_BEGIN_SUMMARY -->` marker).

Unfortunately, in reStructuredText the syntax for inserting such marker is overly verbose:

```rst
.. raw:: html

    <!-- PELICAN_END_SUMMARY -->
```

This plugin allows to replace whole code snippet above with the following line:

```rst
.. end-summary::
```

In order to use this plugin, add `end_summary` to your `PLUGINS` list.