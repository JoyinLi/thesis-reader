# Generic Agent Adapter

Use `LOOP.md` and `CONTRACT.md` as the source of truth.

The runtime must:

- start with triage for newly supplied research sources unless the user skips it;
- preserve human gates;
- keep per-source state outside the installed loop directory;
- generate a Paper Knowledge Package after verified reading and discussion;
- ask before passing the package into `research-knowledge-base`.

Do not make platform-specific assumptions in the core loop.
