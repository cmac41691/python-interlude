# Week 4 Reflection 2026-02-28       

This week focused on integration rather than isolated implementation. I built a stateful CLI that persists data using JSON and verified that it behaves correctly across restarts.

During development I encountered indentation errors, NameErrors from undefined variables, and a critical state bug where duplicate data = {} initialization silently erased loaded data. Fixing this reinforced the importance of having a single source of truth for application state.

I implemented a data_modified (dirty flag) system to control when the application saves. This ensured persistence only occurs when the state actually changes. I tested the lifecycle by running update → quit and then restarting to confirm data stability without unintended overwrites.

This week helped me shift from writing small scripts to thinking in terms of application flow, state lifecycle, and controlled shutdown behavior. It was a small but meaningful step toward backend-level thinking.