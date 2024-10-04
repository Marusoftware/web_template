# Marusoftware Web Template
This is template of Web App project in Marusoftware.
Consisted with these components/concepts:

- environment   
docker   
dev: one click devcontainer(ubuntu-slim)   
prod: distroless
- backend   
fastapi + uvicorn API server   
ORM: tortoise ORM(with aerich migration tool)   
Auth: passwd,passkey, sso with otp
- client   
sveltekit(ts, static adapter)   
UI: flowbite-svelte(tailwind CSS available)   
API client: openapi-ts
- db   
postgresql(over 5.0)
