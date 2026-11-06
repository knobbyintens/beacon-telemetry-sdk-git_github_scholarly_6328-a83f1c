# Release Documentation Policy

- Each release line owns its documentation. Documents are revision-scoped: a
  function reference is only valid for the source tree of the line it ships with.
- Never backport or duplicate a reference document whose line numbers were
  computed from a different revision.
- When a reference is refreshed, commit it on the line that contains the
  implementation it describes.
