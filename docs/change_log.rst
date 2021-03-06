Change Log
==========

The following is a log of all user-facing changes to stem, both released and
unreleased. For a monthly report on work being done see my `development log
<http://www.atagar.com/log.php>`_.

* :ref:`versioning`
* :ref:`unreleased`
* :ref:`version_1.0`

.. _versioning:

Versioning
----------

Stem uses `semantic versioning <http://semver.org/>`_, which means that
**versions consist of three numbers** (such as '**1.2.4**'). These are used to
convey the kind of backward compatibility a release has...

 * The first value is the **major version**. This changes infrequently, and
   indicates that backward incompatible changes have been made (such as the
   removal of deprecated functions).

 * The second value is the **minor version**. This is the most common kind of
   release, and denotes that the improvements are backward compatible.

 * The third value is the **patch version**. When a stem release has a major
   issue another release is made which fixes just that problem. These do not
   contain substantial improvements or new features. This value is sometimes
   left off to indicate all releases with a given major/minor version.

.. _unreleased:

Unreleased
----------

The following are only available within stem's `git repository
<download.html>`_.

 * **Controller**

  * :class:`~stem.response.events.AddrMapEvent` support for the new CACHED argument (:trac:`8596`, `spec <https://gitweb.torproject.org/torspec.git/commitdiff/25b0d43>`_)

 * **Website**

  * Overhaul of stem's `download page <download.html>`_. This included several
    improvements, most notably the addition of PyPI, FreeBSD, and RedHat.
  * Replaced default sphinx header with a navbar menu.
  * Added this change log.
  * Settled on a `logo
    <http://www.wpclipart.com/plants/assorted/P/plant_stem.png.html>`_ for
    stem.

.. _version_1.0:

Version 1.0
-----------

This was the `initial release of stem
<https://blog.torproject.org/blog/stem-release-10>`_, made on **March 26th,
2013**.

 * **Version 1.0.1** (March 27th, 2013) - fixed an issue where installing with
   python 3.x (python3 setup.py install) resulted in a stacktrace

