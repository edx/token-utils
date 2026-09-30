Change Log
##########

..
   All enhancements and patches to token_utils will be documented
   in this file.  It adheres to the structure of https://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (https://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
**********

*

[0.4.0] - 2026-09-28
************************************************

Added
=====

* Added support for Python 3.12

Removed
=======

* Dropped support for Python 3.8; ``python_requires`` is now ``>=3.11``

Changed
=======

* Upgraded requirements, including pyjwt 2.15. A malformed token signature may now raise
  ``jwt.DecodeError`` (the parent of ``InvalidSignatureError``) instead of ``InvalidSignatureError``

[0.3.0] - 2025-06-11
************************************************

Changed
=======

* Replaced pyjwkest package with pyjwt for JWT token handling

[0.2.1] - 2022-12-16
************************************************

Added
=====

* Fixed changelog formatting error

[0.2.0] - 2022-12-15
************************************************

Added
=====

* Added API function to sign access token
* Added API function to unpack access token

[0.1.0] - 2022-08-23
************************************************

Added
=====

* First release on PyPI.
